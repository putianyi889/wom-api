"""Bounded, independently closable subscriptions to server events."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncIterator, Callable
from types import TracebackType

from .exceptions import EventOverflow, WomError
from .types import Event


class EventStream(AsyncIterator[Event]):
    """Async event iterator. Use an async context manager to release it early."""

    def __init__(
        self,
        names: tuple[str, ...],
        size: int,
        release: Callable[[EventStream], None],
    ) -> None:
        if size < 1:
            raise ValueError("max_queue_size must be positive")
        self._names = names
        self._queue: asyncio.Queue[Event | WomError | None] = asyncio.Queue(size)
        self._release = release
        self._closed = False

    def _publish(self, event: Event) -> None:
        if self._closed or (self._names and event.name not in self._names):
            return
        try:
            self._queue.put_nowait(event)
        except asyncio.QueueFull:
            self._finish(EventOverflow("Event buffer filled; create a new subscription"))

    def _finish(self, error: WomError | None = None) -> None:
        if self._closed:
            return
        self._closed = True
        self._release(self)
        while not self._queue.empty():
            self._queue.get_nowait()
        self._queue.put_nowait(error)

    async def __anext__(self) -> Event:
        if self._closed and self._queue.empty():
            raise StopAsyncIteration
        item = await self._queue.get()
        if isinstance(item, WomError):
            raise item
        if item is None:
            raise StopAsyncIteration
        return item

    async def close(self) -> None:
        """Unsubscribe and stop iteration, discarding buffered events."""
        self._finish()

    async def __aenter__(self) -> EventStream:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()
