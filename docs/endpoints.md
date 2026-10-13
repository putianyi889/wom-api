# Endpoint catalogue

Generated from frontend version **1036**; **236** controllers. Each method is async and returns the original JSON value.

All methods accept `payload=None`, keyword-only `server=None`, `timeout=None`, and `**params`. Parameter names in `params` use the original camelCase wire names. A mapping is necessary if a wire field collides with `payload`, `server`, or `timeout`.

Field lists below are observations from browser call sites, **not** required-field schemas. Different requests may use different subsets; unknown or dynamic shapes are stated explicitly. Empty response field lists mean the browser callback did not reveal a destructured shape. Account, chat, game and administrator actions need the corresponding server permissions. Inclusion does not grant access.

Types below describe **observed or inferred JSON types**, not exhaustive server contracts. `frontend syntax` means literals or explicit JavaScript conversions; `live sample` means type-only schemas merged from successful public requests/responses. `JsonValue` with `unresolved` means a field's concrete type is unknown. A type observed in one sample can have other variants that have not been seen. `None` alone means only null was observed, not that null is the only valid value. None is a value, not evidence that a field is optional.

Types use Python notation: `int`, `int | float` (JSON number), `bool`, `str`, `None`, `list[T]`, and `dict[str, JsonValue]`. A path such as `result[].id` describes an array item's field. Date/time strings remain `str`. Live sampling is opt-in; documentation builds are offline. [Type evidence and update procedure](research/README.md#field-type-evidence).

## actualise_queue

Controller: `ActualiseQueueWS`. Role: **watcher**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `inQueue`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `inQueue` | `JsonValue` | unresolved |

## admin_add_chat_ban

Controller: `AdminAddChatBanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `comment`, `period`, `pmBan`, `resetUsername`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `comment` | `JsonValue` | unresolved |
| `period` | `JsonValue` | unresolved |
| `pmBan` | `JsonValue` | unresolved |
| `resetUsername` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_add_chat_ip_ban

Controller: `AdminAddChatIpBanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `ip`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ip` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_add_premium

Controller: `AdminAddPremiumWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_add_royale_ip

Controller: `AdminAddRoyaleIpWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `ip`

Observed response fields: `isExist`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ip` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isExist` | `JsonValue` | unresolved |

## admin_add_website_ip_ban

Controller: `AdminAddWebsiteIpBanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `ip`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ip` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_cancel_account_deletion

Controller: `AdminCancelAccountDeletionWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_cancel_exchanges

Controller: `AdminCancelExchangesWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_delete_game

Controller: `AdminDeleteGameWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `gameId`

Observed response fields: `gameId`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |

## admin_delete_royale_ip

Controller: `AdminDeleteRoyaleIpWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `ip`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ip` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_exchange_ban

Controller: `AdminExchangeBanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `comment`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `comment` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_exchange_unban

Controller: `AdminExchangeUnbanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `comment`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `comment` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_chat_bans

Controller: `AdminGetChatBansWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: `banInfo`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `banInfo` | `JsonValue` | unresolved |

## admin_get_data

Controller: `AdminGetDataWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `sessionsLimit`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `sessionsLimit` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_device_data

Controller: `AdminGetDeviceDataWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `deviceId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `deviceId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_elo_data

Controller: `AdminGetEloDataWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `period`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `period` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_ip_data

Controller: `AdminGetIpDataWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `ip`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ip` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_market_log

Controller: `AdminGetMarketLogWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_royale_ips

Controller: `AdminGetRoyaleIpsWS`. Role: **main**.

Requires administrator permission.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## admin_get_same_devices

Controller: `AdminGetSameDevicesWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`, `yearLimit`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |
| `yearLimit` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_talent_stats

Controller: `AdminGetTalentStatsWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `expFrom`, `expTo`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `expFrom` | `JsonValue` | unresolved |
| `expTo` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_get_team_members

Controller: `AdminGetTeamMembersWS`. Role: **main**.

Requires administrator permission.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## admin_get_username_changelogs

Controller: `AdminGetUsernameChangelogsWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_make_payment

Controller: `AdminMakePaymentWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `invoiceId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `invoiceId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_make_transfer

Controller: `AdminMakeTransferWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `coins`, `itemAmount`, `itemCode`, `itemType`, `message`, `toId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `coins` | `int \| float` | frontend syntax |
| `itemAmount` | `int \| float` | frontend syntax |
| `itemCode` | `JsonValue` | unresolved |
| `itemType` | `JsonValue` | unresolved |
| `message` | `JsonValue` | unresolved |
| `toId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_market_ban

Controller: `AdminMarketBanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `comment`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `comment` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_market_unban

Controller: `AdminMarketUnbanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `comment`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `comment` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_reject_withdrawal

Controller: `AdminRejectWithdrawalWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `id`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `id` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_remove_chat_ip_ban

Controller: `AdminRemoveChatIpBanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `ip`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ip` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_remove_website_ip_ban

Controller: `AdminRemoveWebsiteIpBanWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `ip`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ip` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_report

Controller: `AdminReportWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `banIp`, `comment`, `gameId`, `userIds`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `banIp` | `JsonValue` | unresolved |
| `comment` | `JsonValue` | unresolved |
| `gameId` | `JsonValue` | unresolved |
| `userIds` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_reset_public_info

Controller: `AdminResetPublicInfoWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_reset_talents

Controller: `AdminResetTalentsWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_reset_username

Controller: `AdminResetUsernameWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_success_withdrawal

Controller: `AdminSuccessWithdrawalWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `id`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `id` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## admin_undo_disenchant

Controller: `AdminUndoDisenchantWS`. Role: **main**.

Requires administrator permission.

Observed request shapes:

- `talentId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `talentId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## analyse_board

Controller: `AnalyseBoardWS`. Role: **hint**.

Observed request shapes:

- `gameId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## april_ban

Controller: `AprilBanWS`. Role: **main**.

Observed request shapes:

- `userId`

Observed response fields: `isLimitReached`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isLimitReached` | `JsonValue` | unresolved |

## block_user

Controller: `BlockUserWS`. Role: **chat**.

Observed request shapes:

- `blockedId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `blockedId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## boost_item

Controller: `BoostItemWS`. Role: **main**.

Observed request shapes:

- `isUnlimited`, `itemType`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isUnlimited` | `JsonValue` | unresolved |
| `itemType` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## burn_item

Controller: `BurnItemWS`. Role: **main**.

Observed request shapes:

- `itemType`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `itemType` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## buy_essence

Controller: `BuyEssenceWS`. Role: **main**.

Observed request shapes:

- `amount`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `amount` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## buy_event_shop_slot

Controller: `BuyEventShopSlotWS`. Role: **main**.

Observed request shapes:

- `amount`, `slotId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `amount` | `JsonValue` | unresolved |
| `slotId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## buy_game_hint

Controller: `BuyGameHintWS`. Role: **main**.

Observed request shapes:

- `gameId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## buy_store_slot

Controller: `BuyStoreSlotWS`. Role: **main**.

Observed request shapes:

- `perfectItemType`, `slotId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `perfectItemType` | `JsonValue` | unresolved |
| `slotId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## buy_talent_coins

Controller: `BuyTalentCoinsWS`. Role: **main**.

Observed request shapes:

- `amount`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `amount` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## buy_talent_slot

Controller: `BuyTalentSlotWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## buy_trade

Controller: `BuyTradeWS`. Role: **main**.

Observed request shapes:

- `amount`, `expectedPrice`, `tradeId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `amount` | `JsonValue` | unresolved |
| `expectedPrice` | `JsonValue` | unresolved |
| `tradeId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## cancel_exchange

Controller: `CancelExchangeWS`. Role: **main**.

Observed request shapes:

- `exchangeId`

Observed response fields: `exchangeId`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `exchangeId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `exchangeId` | `JsonValue` | unresolved |

## cancel_trade

Controller: `CancelTradeWS`. Role: **main**.

Observed request shapes:

- `tradeId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `tradeId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## cancel_watch

Controller: `CancelWatchWS`. Role: **watcher**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## cancel_withdrawal

Controller: `CancelWithdrawalWS`. Role: **main**.

Observed request shapes:

- `id`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `id` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## change_event_shop_gem

Controller: `ChangeEventShopGemWS`. Role: **main**.

Observed request shapes:

- `mod`, `slotId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `mod` | `JsonValue` | unresolved |
| `slotId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## change_event_shop_property

Controller: `ChangeEventShopPropertyWS`. Role: **main**.

Observed request shapes:

- `mod`, `slotId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `mod` | `JsonValue` | unresolved |
| `slotId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## change_hidden_mode

Controller: `ChangeHiddenModeWS`. Role: **main**.

Observed request shapes:

- `hidden`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `hidden` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## change_lobby

Controller: `ChangeLobbyWS`. Role: **main**.

Observed request shapes:

- `champId`, `champSlot`, `code`; observed literals: `{"champId": null, "champSlot": null}`
- `code`, `state`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `champId` | `None` | frontend syntax; only null observed |
| `champSlot` | `None` | frontend syntax; only null observed |
| `code` | `JsonValue` | unresolved |
| `state` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## change_shop_gem

Controller: `ChangeShopGemWS`. Role: **main**.

Observed request shapes:

- `mod`, `slotId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `mod` | `JsonValue` | unresolved |
| `slotId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## change_shop_property

Controller: `ChangeShopPropertyWS`. Role: **main**.

Observed request shapes:

- `mod`, `slotId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `mod` | `JsonValue` | unresolved |
| `slotId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## change_special_offer_product

Controller: `ChangeSpecialOfferProductWS`. Role: **main**.

Observed request shapes:

- `product`, `specialOfferId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `product` | `JsonValue` | unresolved |
| `specialOfferId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## check_active_arena

Controller: `CheckActiveArenaWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `activeArenaId`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `activeArenaId` | `JsonValue` | unresolved |

## check_arena_finished

Controller: `CheckArenaFinishedWS`. Role: **main**.

Observed request shapes:

- `arenaId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `arenaId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## check_champ_reward_issued

Controller: `CheckChampRewardIssuedWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `isIssued`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isIssued` | `JsonValue` | unresolved |

## check_champ_reward

Controller: `CheckChampRewardWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `reward`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `reward` | `JsonValue` | unresolved |

## check_event_compensation

Controller: `CheckEventCompensationWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `comp`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `comp` | `JsonValue` | unresolved |

## check_exchanges_exist

Controller: `CheckExchangesExistWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## check_maintenance

Controller: `CheckMaintenanceWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## check_paid_invoice

Controller: `CheckPaidInvoiceWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## check_password_reset_hash

Controller: `CheckPasswordResetHashWS`. Role: **main**.

Observed request shapes:

- `hash`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `hash` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## check_pvp_season_reward

Controller: `CheckPvpSeasonRewardWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `operation`, `pvpSeasonReward`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `operation` | `JsonValue` | unresolved |
| `pvpSeasonReward` | `JsonValue` | unresolved |

## check_season_reward

Controller: `CheckSeasonRewardWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `operation`, `seasonCountAll`, `seasonPosition`, `userStat`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `operation` | `JsonValue` | unresolved |
| `seasonCountAll` | `JsonValue` | unresolved |
| `seasonPosition` | `JsonValue` | unresolved |
| `userStat` | `JsonValue` | unresolved |

## check_special_offers

Controller: `CheckSpecialOffersWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `specialOffers`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `specialOffers` | `JsonValue` | unresolved |

## check_success_exchanges

Controller: `CheckSuccessExchangesWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `count`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |

## check_success_trades

Controller: `CheckSuccessTradesWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `count`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |

## close_channel

Controller: `CloseChannelWS`. Role: **chat**.

Observed request shapes:

- `channelId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `channelId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## collect_daily_login_reward

Controller: `CollectDailyLoginRewardWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `JsonValue` (unresolved).

Response type: `JsonValue` (unresolved).

## collect_quest

Controller: `CollectQuestWS`. Role: **main**.

Observed request shapes:

- `questId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `questId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## collect_sent_friend_quest

Controller: `CollectSentFriendQuestWS`. Role: **main**.

Observed request shapes:

- `friendQuestId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `friendQuestId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## collect_trade

Controller: `CollectTradeWS`. Role: **main**.

Observed request shapes:

- `tradeId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `tradeId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## confirm_exchange

Controller: `ConfirmExchangeWS`. Role: **main**.

Observed request shapes:

- `exchangeData`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `exchangeData` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## create_channel

Controller: `CreateChannelWS`. Role: **chat**.

Observed request shapes:

- `withUserId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `withUserId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## create_invoice

Controller: `CreateInvoiceWS`. Role: **main**.

Observed request shapes:

- `coins`, `currency`, `isDiscount`, `itemAmount`, `itemType`, `lang`, `paymentMethod`, `product`, `productName`, `slotId`, `specialOfferId`; observed literals: `{"specialOfferId": null}`
- `coins`, `currency`, `isDiscount`, `itemAmount`, `itemType`, `lang`, `paymentMethod`, `product`, `productName`, `slotId`, `specialOfferId`; observed literals: `{"coins": 0, "itemType": null, "itemAmount": 0, "slotId": null, "isDiscount": false}`
- `coins`, `currency`, `isDiscount`, `itemAmount`, `itemType`, `lang`, `paymentMethod`, `product`, `productName`, `slotId`, `specialOfferId`; observed literals: `{"coins": null, "itemType": null, "itemAmount": null, "slotId": null, "specialOfferId": null, "isDiscount": false}`
- `coins`, `currency`, `isDiscount`, `itemAmount`, `itemType`, `lang`, `paymentMethod`, `product`, `productName`, `slotId`, `specialOfferId`; observed literals: `{"coins": 0, "itemType": null, "itemAmount": 0, "slotId": null, "specialOfferId": null, "isDiscount": false}`

Observed response fields: `approvalUrl`, `product`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `coins` | `int \| None` | frontend syntax |
| `currency` | `JsonValue` | unresolved |
| `isDiscount` | `bool` | frontend syntax |
| `itemAmount` | `int \| None` | frontend syntax |
| `itemType` | `None` | frontend syntax; only null observed |
| `lang` | `JsonValue` | unresolved |
| `paymentMethod` | `JsonValue` | unresolved |
| `product` | `JsonValue` | unresolved |
| `productName` | `JsonValue` | unresolved |
| `slotId` | `None` | frontend syntax; only null observed |
| `specialOfferId` | `None` | frontend syntax; only null observed |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `approvalUrl` | `JsonValue` | unresolved |
| `product` | `JsonValue` | unresolved |

## create_lobby

Controller: `CreateLobbyWS`. Role: **main**.

Observed request shapes:

- `champId`, `champSlot`, `mines`, `ng`, `sizeX`, `sizeY`, `user1Id`, `user2Id`, `winsRequired`

Observed response fields: `lobbyCode`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `champId` | `JsonValue` | unresolved |
| `champSlot` | `JsonValue` | unresolved |
| `mines` | `JsonValue` | unresolved |
| `ng` | `JsonValue` | unresolved |
| `sizeX` | `JsonValue` | unresolved |
| `sizeY` | `JsonValue` | unresolved |
| `user1Id` | `JsonValue` | unresolved |
| `user2Id` | `JsonValue` | unresolved |
| `winsRequired` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `lobbyCode` | `JsonValue` | unresolved |

## create_withdrawal

Controller: `CreateWithdrawalWS`. Role: **main**.

Observed request shapes:

- `amountStr`, `email`, `wallet`

Observed response fields: `hash`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `amountStr` | `JsonValue` | unresolved |
| `email` | `JsonValue` | unresolved |
| `wallet` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `hash` | `JsonValue` | unresolved |

## delete_account

Controller: `DeleteAccountWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## delete_friend_quest

Controller: `DeleteFriendQuestWS`. Role: **main**.

Observed request shapes:

- `questId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `questId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## disassemble_item

Controller: `DisassembleItemWS`. Role: **main**.

Observed request shapes:

- `itemType`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `itemType` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## disenchant_custom_talent

Controller: `DisenchantCustomTalentWS`. Role: **main**.

Observed request shapes:

- `talentId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `talentId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## downgrade_quest

Controller: `DowngradeQuestWS`. Role: **main**.

Observed request shapes:

- `questId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `questId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## enter_game

Controller: `EnterGameWS`. Role: **main**.

Observed request shapes:

- `gameId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## equip_item

Controller: `EquipItemWS`. Role: **main**.

Observed request shapes:

- `itemType`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `itemType` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## exchange_talent_coin

Controller: `ExchangeTalentCoinWS`. Role: **main**.

Observed request shapes:

- `isHp`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isHp` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## fetch_arena_best_result_table

Controller: `FetchArenaBestResultTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `arenaLevel`, `arenaType`, `country`, `season`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `arena`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.arenaLevel` | `JsonValue` | unresolved |
| `params.arenaType` | `JsonValue` | unresolved |
| `params.country` | `JsonValue` | unresolved |
| `params.season` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_arena_table

Controller: `FetchArenaTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `level`, `type`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `arenas_title`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.level` | `JsonValue` | unresolved |
| `params.type` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_best_result_table

Controller: `FetchBestResultTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `level`, `mines`, `nfOnly`, `season`, `sizeX`, `sizeY`, `sortBy`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `/ng`, `seo_title_ranking_all_time`, `seo_title_ng_ranking`, `seo_description_ranking_all_time`, `seo_description_ng_ranking`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.level` | `JsonValue` | unresolved |
| `params.mines` | `JsonValue` | unresolved |
| `params.nfOnly` | `JsonValue` | unresolved |
| `params.season` | `JsonValue` | unresolved |
| `params.sizeX` | `JsonValue` | unresolved |
| `params.sizeY` | `JsonValue` | unresolved |
| `params.sortBy` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_champ_best_result_table

Controller: `FetchChampBestResultTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `champId`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.champId` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_chat_message_table

Controller: `FetchChatMessageTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `channelId`, `template`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `Chat history`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.channelId` | `JsonValue` | unresolved |
| `params.template` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_exchange_table

Controller: `FetchExchangeTableWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `JsonValue` (unresolved).

Response type: `JsonValue` (unresolved).

## fetch_level_stat_table

Controller: `FetchLevelStatTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `season`, `sortBy`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `seo_title_statistics`, `seo_description_statistics`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.season` | `JsonValue` | unresolved |
| `params.sortBy` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_nft_table

Controller: `FetchNftTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_players_online_table

Controller: `FetchPlayersOnlineTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `seo_title_players_online`, `seo_description_players_online`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_quest_table

Controller: `FetchQuestTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `quests_title`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_trade_table

Controller: `FetchTradeTableWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `JsonValue` (unresolved).

Response type: `JsonValue` (unresolved).

## fetch_user_result_my_table

Controller: `FetchUserResultMyTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `isAllGames`, `isAllSizes`, `isNoReplays`, `level`, `mines`, `nfOnly`, `season`, `sizeX`, `sizeY`, `sortBy`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `/ng`, `seo_title_my_games`, `seo_title_ng_my_games`, `seo_description_my_games`, `seo_description_ng_my_games`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.isAllGames` | `JsonValue` | unresolved |
| `params.isAllSizes` | `JsonValue` | unresolved |
| `params.isNoReplays` | `JsonValue` | unresolved |
| `params.level` | `JsonValue` | unresolved |
| `params.mines` | `JsonValue` | unresolved |
| `params.nfOnly` | `JsonValue` | unresolved |
| `params.season` | `JsonValue` | unresolved |
| `params.sizeX` | `JsonValue` | unresolved |
| `params.sizeY` | `JsonValue` | unresolved |
| `params.sortBy` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_user_result_news_table

Controller: `FetchUserResultNewsTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `reward`, `season`, `sortBy`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `rewards_list_title`, `seo_title_news`, `seo_description_news`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.reward` | `JsonValue` | unresolved |
| `params.season` | `JsonValue` | unresolved |
| `params.sortBy` | `JsonValue` | unresolved |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## fetch_user_stat_table

Controller: `FetchUserStatTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `brLevel`, `country`, `season`, `sortBy`, `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Observed default table sort keys: `event`, `eventItems`, `score`, `timePoints`, `exp`, `quality`, `mastery`, `ws`, `diff`, `end`, `wins`, `coinsAll`, `gemsAll`, `ticketScoreAll`, `questScoreAll`, `activityTotal`, `arenaCoinsAll`, `rewardsAll`, `effPoints`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax, live sample |
| `limit` | `int` | frontend syntax, live sample |
| `offset` | `int` | frontend syntax, live sample |
| `params` | `dict[str, JsonValue]` | frontend syntax, live sample |
| `params.brLevel` | `int \| None` | frontend syntax, live sample |
| `params.country` | `str \| None` | frontend syntax, live sample |
| `params.season` | `int` | live sample |
| `params.sortBy` | `str` | frontend syntax, live sample |
| `params.userId` | `int` | live sample |
| `url` | `str` | frontend syntax, live sample |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `int` | live sample |
| `initData` | `dict[str, JsonValue]` | live sample |
| `initData.userData` | `dict[str, JsonValue]` | live sample |
| `initData.userData.11711708` | `dict[str, JsonValue]` | live sample |
| `initData.userData.11711708.country` | `str` | live sample |
| `initData.userData.11711708.fromMobile` | `bool` | live sample |
| `initData.userData.11711708.id` | `int` | live sample |
| `initData.userData.11711708.online` | `bool` | live sample |
| `initData.userData.11711708.username` | `str` | live sample |
| `initData.userData.35024994` | `dict[str, JsonValue]` | live sample |
| `initData.userData.35024994.country` | `str` | live sample |
| `initData.userData.35024994.fromMobile` | `bool` | live sample |
| `initData.userData.35024994.id` | `int` | live sample |
| `initData.userData.35024994.online` | `bool` | live sample |
| `initData.userData.35024994.username` | `str` | live sample |
| `initData.userData.48108978` | `dict[str, JsonValue]` | live sample |
| `initData.userData.48108978.country` | `str` | live sample |
| `initData.userData.48108978.fromMobile` | `bool` | live sample |
| `initData.userData.48108978.id` | `int` | live sample |
| `initData.userData.48108978.online` | `bool` | live sample |
| `initData.userData.48108978.username` | `str` | live sample |
| `position` | `None` | live sample; only null observed |
| `rows` | `list[dict[str, JsonValue]]` | live sample |
| `rows[]` | `dict[str, JsonValue]` | live sample |
| `rows[].bbbv` | `int` | live sample |
| `rows[].bbbvs` | `int` | live sample |
| `rows[].duration` | `int` | live sample |
| `rows[].eff100` | `int` | live sample |
| `rows[].finishedAt` | `str` | live sample |
| `rows[].gameId` | `int` | live sample |
| `rows[].id` | `int` | live sample |
| `rows[].level` | `int` | live sample |
| `rows[].mines` | `int` | live sample |
| `rows[].mobile` | `int` | live sample |
| `rows[].nf` | `int` | live sample |
| `rows[].nfOnly` | `int` | live sample |
| `rows[].season` | `int` | live sample |
| `rows[].sizeX` | `int` | live sample |
| `rows[].sizeY` | `int` | live sample |
| `rows[].sortBy3bvs` | `int` | live sample |
| `rows[].userId` | `int` | live sample |
| `rows[].xid` | `int` | live sample |
| `url` | `str` | live sample |

## fetch_user_worth_table

Controller: `FetchUserWorthTableWS`. Role: **main**.

Observed request shapes:

- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 1, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 2, "limit": 0, "offset": 0}`
- `dataType`, `limit`, `offset`, `params`, `url`; observed literals: `{"dataType": 3}`

Observed response fields: `count`, `initData`, `position`, `rows`, `url`.

Observed nested `params` shapes:

- `userId`

Table `dataType`: 1 = count, 2 = current player position, 3 = rows.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `dataType` | `int` | frontend syntax |
| `limit` | `int` | frontend syntax |
| `offset` | `int` | frontend syntax |
| `params` | `dict[str, JsonValue]` | frontend syntax |
| `params.userId` | `JsonValue` | unresolved |
| `url` | `str` | frontend syntax |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `count` | `JsonValue` | unresolved |
| `initData` | `JsonValue` | unresolved |
| `position` | `JsonValue` | unresolved |
| `rows` | `JsonValue` | unresolved |
| `url` | `JsonValue` | unresolved |

## finish_arena

Controller: `FinishArenaWS`. Role: **main**.

Observed request shapes:

- `arenaId`, `goToArenaPage`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `arenaId` | `JsonValue` | unresolved |
| `goToArenaPage` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## game_click

Controller: `GameClickWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `JsonValue` (unresolved).

Response type: `JsonValue` (unresolved).

## generate_custom_talent

Controller: `GenerateCustomTalentWS`. Role: **main**.

Observed request shapes:

- `resourceType`
- `resourceType`; observed literals: `{"resourceType": "16"}`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `resourceType` | `str` | frontend syntax |

Response type: `JsonValue` (unresolved).

## generate_token

Controller: `GenerateTokenWS`. Role: **main**.

Observed request shapes:

- `questId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `questId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_active_duel

Controller: `GetActiveDuelWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `activeDuelId`, `activeLobbyCode`, `activeServer`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `activeDuelId` | `JsonValue` | unresolved |
| `activeLobbyCode` | `JsonValue` | unresolved |
| `activeServer` | `JsonValue` | unresolved |

## get_all_champs

Controller: `GetAllChampsWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_all_events

Controller: `GetAllEventsWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_arena_data

Controller: `GetArenaDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_arena_detail_data

Controller: `GetArenaDetailDataWS`. Role: **main**.

Observed request shapes:

- `arenaId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `arenaId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_auth_code

Controller: `GetAuthCodeWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `code`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `code` | `JsonValue` | unresolved |

## get_burn_data

Controller: `GetBurnDataWS`. Role: **main**.

Observed request shapes:

- `itemType`

Observed response fields: `burnEs`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `itemType` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `burnEs` | `JsonValue` | unresolved |

## get_champ_arena_data

Controller: `GetChampArenaDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_champ_lobbies

Controller: `GetChampLobbiesWS`. Role: **main**.

Observed request shapes:

- `champId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `champId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_contacts

Controller: `GetContactsWS`. Role: **chat**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_convert_log

Controller: `GetConvertLogWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_custom_talent_detail_data

Controller: `GetCustomTalentDetailDataWS`. Role: **main**.

Observed request shapes:

- `talentId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `talentId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_custom_talents_data

Controller: `GetCustomTalentsDataWS`. Role: **main**.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_difficulty

Controller: `GetDifficultyWS`. Role: **main**.

Observed request shapes:

- `isDuelNg`, `level`, `mines`, `sizeX`, `sizeY`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isDuelNg` | `JsonValue` | unresolved |
| `level` | `JsonValue` | unresolved |
| `mines` | `JsonValue` | unresolved |
| `sizeX` | `JsonValue` | unresolved |
| `sizeY` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_duel_info

Controller: `GetDuelInfoWS`. Role: **main**.

Observed request shapes:

- `duelId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `duelId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_economy_data

Controller: `GetEconomyDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_emc_data

Controller: `GetEmcDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_eq_quality

Controller: `GetEqQualityWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `eqQuality`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `eqQuality` | `JsonValue` | unresolved |

## get_equipment_data

Controller: `GetEquipmentDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_est_price

Controller: `GetEstPriceWS`. Role: **main**.

Observed request shapes:

- `coinClass`, `itemType`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `coinClass` | `JsonValue` | unresolved |
| `itemType` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_event_shop_data

Controller: `GetEventShopDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_exchange_detail_data

Controller: `GetExchangeDetailDataWS`. Role: **main**.

Observed request shapes:

- `exchangeId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `exchangeId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_game_series

Controller: `GetGameSeriesWS`. Role: **main**.

Observed request shapes:

- `category`, `gameId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `category` | `JsonValue` | unresolved |
| `gameId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_global_quest_positions

Controller: `GetGlobalQuestPositionsWS`. Role: **main**.

Observed request shapes:

- `globalQuestId`, `isLimit`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `globalQuestId` | `JsonValue` | unresolved |
| `isLimit` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_guides

Controller: `GetGuidesWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_help_page

Controller: `GetHelpPageWS`. Role: **main**.

Observed request shapes:

- `lang`, `page`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `lang` | `JsonValue` | unresolved |
| `page` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_hof_table

Controller: `GetHofTableWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_initiation_data

Controller: `GetInitiationDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_invoice_detail_data

Controller: `GetInvoiceDetailDataWS`. Role: **main**.

Observed request shapes:

- `hash`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `hash` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_invoices

Controller: `GetInvoicesWS`. Role: **main**.

Observed request shapes:

- `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_items_price

Controller: `GetItemsPriceWS`. Role: **main**.

Observed request shapes:

- `coins`, `isEssencePrice`, `items`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `coins` | `JsonValue` | unresolved |
| `isEssencePrice` | `JsonValue` | unresolved |
| `items` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_lobby_data

Controller: `GetLobbyDataWS`. Role: **main**.

Observed request shapes:

- `code`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `code` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_market_price

Controller: `GetMarketPriceWS`. Role: **main**.

Observed request shapes:

- `cat1`, `cat2`, `cat3`, `cat4`, `itemType`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `cat1` | `JsonValue` | unresolved |
| `cat2` | `JsonValue` | unresolved |
| `cat3` | `JsonValue` | unresolved |
| `cat4` | `JsonValue` | unresolved |
| `itemType` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_mercy_system

Controller: `GetMercySystemWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `mercySystem`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `mercySystem` | `JsonValue` | unresolved |

## get_mines_limit

Controller: `GetMinesLimitWS`. Role: **main**.

Observed request shapes:

- `mines`, `sizeX`, `sizeY`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `mines` | `JsonValue` | unresolved |
| `sizeX` | `JsonValue` | unresolved |
| `sizeY` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_new_exchange_data

Controller: `GetNewExchangeDataWS`. Role: **main**.

Observed request shapes:

- `buyerId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `buyerId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_new_trade_data

Controller: `GetNewTradeDataWS`. Role: **main**.

Observed request shapes:

- `category`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `category` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_nft

Controller: `GetNftWS`. Role: **main**.

Observed request shapes:

- `isUpdate`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isUpdate` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_players_online_count

Controller: `GetPlayersOnlineCountWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_players_online_map

Controller: `GetPlayersOnlineMapWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_pvp_data

Controller: `GetPvpDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_pvp_game_data

Controller: `GetPvpGameDataWS`. Role: **main**.

Observed request shapes:

- `gameId`

Observed response fields: `cells`, `clicks`, `state`, `time`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `cells` | `JsonValue` | unresolved |
| `clicks` | `JsonValue` | unresolved |
| `state` | `JsonValue` | unresolved |
| `time` | `JsonValue` | unresolved |

## get_quests

Controller: `GetQuestsWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_ranks_table

Controller: `GetRanksTableWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `ranksCount`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `ranksCount` | `dict[str, JsonValue]` | live sample |
| `ranksCount.count1` | `int` | live sample |
| `ranksCount.count100` | `int` | live sample |
| `ranksCount.count1000` | `int` | live sample |
| `ranksCount.count1100` | `int` | live sample |
| `ranksCount.count1200` | `int` | live sample |
| `ranksCount.count200` | `int` | live sample |
| `ranksCount.count300` | `int` | live sample |
| `ranksCount.count400` | `int` | live sample |
| `ranksCount.count500` | `int` | live sample |
| `ranksCount.count600` | `int` | live sample |
| `ranksCount.count700` | `int` | live sample |
| `ranksCount.count800` | `int` | live sample |
| `ranksCount.count900` | `int` | live sample |

## get_rates_graph_data

Controller: `GetRatesGraphDataWS`. Role: **main**.

Observed request shapes:

- `currency`, `dateFrom`, `item`

Observed response fields: `result`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `currency` | `JsonValue` | unresolved |
| `dateFrom` | `JsonValue` | unresolved |
| `item` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `result` | `JsonValue` | unresolved |

## get_recap

Controller: `GetRecapWS`. Role: **main**.

Observed request shapes:

- `userId`, `year`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |
| `year` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_rewards_table

Controller: `GetRewardsTableWS`. Role: **main**.

Observed request shapes:

- `season`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `season` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_scores_table

Controller: `GetScoresTableWS`. Role: **main**.

Observed request shapes:

- `level`, `season`, `step`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `level` | `JsonValue` | unresolved |
| `season` | `JsonValue` | unresolved |
| `step` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_send_friend_quest_data

Controller: `GetSendFriendQuestDataWS`. Role: **main**.

Observed request shapes:

- `friendId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `friendId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_servers_stats

Controller: `GetServersStatsWS`. Role: **main**.

Observed request shapes:

- `env`, `server`; observed literals: `{"env": "production"}`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `env` | `str` | frontend syntax |
| `server` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_sessions

Controller: `GetSessionsWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_shop_data

Controller: `GetShopDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_skill_points_table

Controller: `GetSkillPointsTableWS`. Role: **main**.

Observed request shapes:

- `type`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `type` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_stat_aggregate

Controller: `GetStatAggregateWS`. Role: **main**.

Observed request shapes:

- `season`, `userId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `season` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_talent_points_table

Controller: `GetTalentPointsTableWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_talents_data

Controller: `GetTalentsDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_trade_detail_data

Controller: `GetTradeDetailDataWS`. Role: **main**.

Observed request shapes:

- `tradeDetailVisit`, `tradeId`; observed literals: `{"tradeDetailVisit": true}`
- `tradeDetailVisit`, `tradeId`; observed literals: `{"tradeDetailVisit": false}`

Observed response fields: `trade`, `userCoins`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `tradeDetailVisit` | `bool` | frontend syntax |
| `tradeId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `trade` | `JsonValue` | unresolved |
| `userCoins` | `JsonValue` | unresolved |

## get_user_detail_data

Controller: `GetUserDetailDataWS`. Role: **main**.

Observed request shapes:

- `popupRandId`, `userId`
- `popupRandId`, `userId`; observed literals: `{"popupRandId": null}`

Observed response fields: `allTalentPoints`, `arenaResults`, `customTalentData`, `effResults`, `noUserStatExp`, `popupRandId`, `seasonUserStat`, `timeResults`, `tokensUsed`, `user`, `userStat`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `popupRandId` | `None` | frontend syntax, live sample; only null observed |
| `userId` | `int` | live sample |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `allTalentPoints` | `int` | live sample |
| `arenaResults` | `list[dict[str, JsonValue]]` | live sample |
| `arenaResults[]` | `dict[str, JsonValue]` | live sample |
| `arenaResults[].duration` | `int` | live sample |
| `arenaResults[].extraConf` | `None` | live sample; only null observed |
| `arenaResults[].finishedAt` | `str` | live sample |
| `arenaResults[].id` | `int` | live sample |
| `arenaResults[].mode` | `int` | live sample |
| `arenaResults[].operationRewardId` | `int` | live sample |
| `arenaResults[].operationTicketId` | `int` | live sample |
| `arenaResults[].penaltyTotal` | `int` | live sample |
| `arenaResults[].startedAt` | `str` | live sample |
| `arenaResults[].state` | `int` | live sample |
| `arenaResults[].type` | `int` | live sample |
| `arenaResults[].userId` | `int` | live sample |
| `customTalentData` | `dict[str, JsonValue]` | live sample |
| `effResults` | `dict[str, JsonValue]` | live sample |
| `effResults.1` | `dict[str, JsonValue]` | live sample |
| `effResults.1.bbbv` | `int` | live sample |
| `effResults.1.bbbvs` | `int` | live sample |
| `effResults.1.duration` | `int` | live sample |
| `effResults.1.eff100` | `int` | live sample |
| `effResults.1.finishedAt` | `str` | live sample |
| `effResults.1.gameId` | `int` | live sample |
| `effResults.1.id` | `int` | live sample |
| `effResults.1.level` | `int` | live sample |
| `effResults.1.mines` | `int` | live sample |
| `effResults.1.mobile` | `int` | live sample |
| `effResults.1.nf` | `int` | live sample |
| `effResults.1.nfOnly` | `int` | live sample |
| `effResults.1.season` | `int` | live sample |
| `effResults.1.sizeX` | `int` | live sample |
| `effResults.1.sizeY` | `int` | live sample |
| `effResults.1.sortBy3bvs` | `int` | live sample |
| `effResults.1.userId` | `int` | live sample |
| `effResults.2` | `dict[str, JsonValue]` | live sample |
| `effResults.2.bbbv` | `int` | live sample |
| `effResults.2.bbbvs` | `int` | live sample |
| `effResults.2.duration` | `int` | live sample |
| `effResults.2.eff100` | `int` | live sample |
| `effResults.2.finishedAt` | `str` | live sample |
| `effResults.2.gameId` | `int` | live sample |
| `effResults.2.id` | `int` | live sample |
| `effResults.2.level` | `int` | live sample |
| `effResults.2.mines` | `int` | live sample |
| `effResults.2.mobile` | `int` | live sample |
| `effResults.2.nf` | `int` | live sample |
| `effResults.2.nfOnly` | `int` | live sample |
| `effResults.2.season` | `int` | live sample |
| `effResults.2.sizeX` | `int` | live sample |
| `effResults.2.sizeY` | `int` | live sample |
| `effResults.2.sortBy3bvs` | `int` | live sample |
| `effResults.2.userId` | `int` | live sample |
| `effResults.3` | `dict[str, JsonValue]` | live sample |
| `effResults.3.bbbv` | `int` | live sample |
| `effResults.3.bbbvs` | `int` | live sample |
| `effResults.3.duration` | `int` | live sample |
| `effResults.3.eff100` | `int` | live sample |
| `effResults.3.finishedAt` | `str` | live sample |
| `effResults.3.gameId` | `int` | live sample |
| `effResults.3.id` | `int` | live sample |
| `effResults.3.level` | `int` | live sample |
| `effResults.3.mines` | `int` | live sample |
| `effResults.3.mobile` | `int` | live sample |
| `effResults.3.nf` | `int` | live sample |
| `effResults.3.nfOnly` | `int` | live sample |
| `effResults.3.season` | `int` | live sample |
| `effResults.3.sizeX` | `int` | live sample |
| `effResults.3.sizeY` | `int` | live sample |
| `effResults.3.sortBy3bvs` | `int` | live sample |
| `effResults.3.userId` | `int` | live sample |
| `noUserStatExp` | `int` | live sample |
| `popupRandId` | `None` | live sample; only null observed |
| `seasonUserStat` | `dict[str, JsonValue]` | live sample |
| `seasonUserStat.activityTotal` | `int` | live sample |
| `seasonUserStat.arenaCoinsAll` | `int` | live sample |
| `seasonUserStat.arenaDuration` | `None` | live sample; only null observed |
| `seasonUserStat.arenaPoints` | `int` | live sample |
| `seasonUserStat.arenaScore` | `int` | live sample |
| `seasonUserStat.bbbvActive` | `int` | live sample |
| `seasonUserStat.bbbvAll` | `int` | live sample |
| `seasonUserStat.boosts` | `None` | live sample; only null observed |
| `seasonUserStat.coins` | `int` | live sample |
| `seasonUserStat.coinsAll` | `int` | live sample |
| `seasonUserStat.coinsSeason` | `int` | live sample |
| `seasonUserStat.coinsSeasonScore` | `int` | live sample |
| `seasonUserStat.country` | `str` | live sample |
| `seasonUserStat.ct` | `None` | live sample; only null observed |
| `seasonUserStat.ctData` | `None` | live sample; only null observed |
| `seasonUserStat.diff` | `int` | live sample |
| `seasonUserStat.diffBbbv` | `int` | live sample |
| `seasonUserStat.diffDuration` | `int` | live sample |
| `seasonUserStat.diffFinishedAt` | `str` | live sample |
| `seasonUserStat.diffId` | `int` | live sample |
| `seasonUserStat.diffLevel` | `int` | live sample |
| `seasonUserStat.diffMines` | `int` | live sample |
| `seasonUserStat.diffScore` | `int` | live sample |
| `seasonUserStat.diffSizeX` | `int` | live sample |
| `seasonUserStat.diffSizeY` | `int` | live sample |
| `seasonUserStat.effBbbv` | `None` | live sample; only null observed |
| `seasonUserStat.effBbbvs` | `None` | live sample; only null observed |
| `seasonUserStat.effDuration` | `None` | live sample; only null observed |
| `seasonUserStat.effEff100` | `None` | live sample; only null observed |
| `seasonUserStat.effFinishedAt` | `None` | live sample; only null observed |
| `seasonUserStat.effId` | `None` | live sample; only null observed |
| `seasonUserStat.effLevel` | `None` | live sample; only null observed |
| `seasonUserStat.effMines` | `None` | live sample; only null observed |
| `seasonUserStat.effMobile` | `None` | live sample; only null observed |
| `seasonUserStat.effPoints` | `int` | live sample |
| `seasonUserStat.effScore` | `int` | live sample |
| `seasonUserStat.effSizeX` | `None` | live sample; only null observed |
| `seasonUserStat.effSizeY` | `None` | live sample; only null observed |
| `seasonUserStat.end1` | `int` | live sample |
| `seasonUserStat.end1Id` | `None` | live sample; only null observed |
| `seasonUserStat.end2` | `int` | live sample |
| `seasonUserStat.end2Id` | `None` | live sample; only null observed |
| `seasonUserStat.end3` | `int` | live sample |
| `seasonUserStat.end3Id` | `None` | live sample; only null observed |
| `seasonUserStat.endBestId` | `None` | live sample; only null observed |
| `seasonUserStat.endBestPoints` | `int` | live sample |
| `seasonUserStat.endDuration` | `None` | live sample; only null observed |
| `seasonUserStat.endFinishedAt` | `None` | live sample; only null observed |
| `seasonUserStat.endLevel` | `None` | live sample; only null observed |
| `seasonUserStat.endNHId` | `None` | live sample; only null observed |
| `seasonUserStat.endNHPoints` | `int` | live sample |
| `seasonUserStat.endScore` | `int` | live sample |
| `seasonUserStat.eq` | `None` | live sample; only null observed |
| `seasonUserStat.eventItems` | `int` | live sample |
| `seasonUserStat.eventItemsRank` | `int` | live sample |
| `seasonUserStat.exp` | `int` | live sample |
| `seasonUserStat.expAll` | `int` | live sample |
| `seasonUserStat.expScore` | `int` | live sample |
| `seasonUserStat.extraStat` | `dict[str, JsonValue]` | live sample |
| `seasonUserStat.extraStat.acg` | `int` | live sample |
| `seasonUserStat.extraStat.cg` | `int` | live sample |
| `seasonUserStat.extraStat.cq` | `int` | live sample |
| `seasonUserStat.extraStat.eg` | `int` | live sample |
| `seasonUserStat.extraStat.eig` | `int` | live sample |
| `seasonUserStat.extraStat.eiq` | `int` | live sample |
| `seasonUserStat.extraStat.eq` | `int` | live sample |
| `seasonUserStat.extraStat.g5` | `int` | live sample |
| `seasonUserStat.extraStat.g8` | `int` | live sample |
| `seasonUserStat.extraStat.qe` | `int` | live sample |
| `seasonUserStat.extraStat.qs` | `int` | live sample |
| `seasonUserStat.extraStat.t1` | `int` | live sample |
| `seasonUserStat.extraStat.t2` | `int` | live sample |
| `seasonUserStat.extraStat.t3` | `int` | live sample |
| `seasonUserStat.extraStat.t4` | `int` | live sample |
| `seasonUserStat.extraStat.t5` | `int` | live sample |
| `seasonUserStat.extraStat.t7` | `int` | live sample |
| `seasonUserStat.extraStat.t8` | `int` | live sample |
| `seasonUserStat.games` | `int` | live sample |
| `seasonUserStat.gemsAll` | `int` | live sample |
| `seasonUserStat.i5` | `int` | live sample |
| `seasonUserStat.id` | `int` | live sample |
| `seasonUserStat.items` | `dict[str, JsonValue]` | live sample |
| `seasonUserStat.items.112` | `int` | live sample |
| `seasonUserStat.items.114` | `int` | live sample |
| `seasonUserStat.items.121` | `int` | live sample |
| `seasonUserStat.items.123` | `int` | live sample |
| `seasonUserStat.items.132` | `int` | live sample |
| `seasonUserStat.items.141` | `int` | live sample |
| `seasonUserStat.items.143` | `int` | live sample |
| `seasonUserStat.items.148` | `int` | live sample |
| `seasonUserStat.items.15` | `int` | live sample |
| `seasonUserStat.items.157` | `int` | live sample |
| `seasonUserStat.items.161` | `int` | live sample |
| `seasonUserStat.items.162` | `int` | live sample |
| `seasonUserStat.items.165` | `int` | live sample |
| `seasonUserStat.items.168` | `int` | live sample |
| `seasonUserStat.items.171` | `int` | live sample |
| `seasonUserStat.items.174` | `int` | live sample |
| `seasonUserStat.items.178` | `int` | live sample |
| `seasonUserStat.items.181` | `int` | live sample |
| `seasonUserStat.items.182` | `int` | live sample |
| `seasonUserStat.items.183` | `int` | live sample |
| `seasonUserStat.items.185` | `int` | live sample |
| `seasonUserStat.items.192` | `int` | live sample |
| `seasonUserStat.items.194` | `int` | live sample |
| `seasonUserStat.items.490` | `int` | live sample |
| `seasonUserStat.items.491` | `int` | live sample |
| `seasonUserStat.items.492` | `int` | live sample |
| `seasonUserStat.items.493` | `int` | live sample |
| `seasonUserStat.items.494` | `int` | live sample |
| `seasonUserStat.items.495` | `int` | live sample |
| `seasonUserStat.items.496` | `int` | live sample |
| `seasonUserStat.items.497` | `int` | live sample |
| `seasonUserStat.items.498` | `int` | live sample |
| `seasonUserStat.items.499` | `int` | live sample |
| `seasonUserStat.items.5` | `int` | live sample |
| `seasonUserStat.items.500` | `int` | live sample |
| `seasonUserStat.items.501` | `int` | live sample |
| `seasonUserStat.items.544` | `int` | live sample |
| `seasonUserStat.items.8` | `int` | live sample |
| `seasonUserStat.j3` | `None` | live sample; only null observed |
| `seasonUserStat.lastSeason` | `int` | live sample |
| `seasonUserStat.mastery1` | `int` | live sample |
| `seasonUserStat.mastery1Duration` | `int` | live sample |
| `seasonUserStat.mastery1FinishedAt` | `str` | live sample |
| `seasonUserStat.mastery1Id` | `int` | live sample |
| `seasonUserStat.mastery1Points` | `int` | live sample |
| `seasonUserStat.mastery1Time` | `int` | live sample |
| `seasonUserStat.mastery2` | `int` | live sample |
| `seasonUserStat.mastery2Duration` | `None` | live sample; only null observed |
| `seasonUserStat.mastery2FinishedAt` | `None` | live sample; only null observed |
| `seasonUserStat.mastery2Id` | `None` | live sample; only null observed |
| `seasonUserStat.mastery2Time` | `None` | live sample; only null observed |
| `seasonUserStat.mastery3` | `int` | live sample |
| `seasonUserStat.mastery3Duration` | `None` | live sample; only null observed |
| `seasonUserStat.mastery3FinishedAt` | `None` | live sample; only null observed |
| `seasonUserStat.mastery3Id` | `None` | live sample; only null observed |
| `seasonUserStat.mastery3Time` | `None` | live sample; only null observed |
| `seasonUserStat.masteryId` | `int` | live sample |
| `seasonUserStat.masteryLId` | `int` | live sample |
| `seasonUserStat.masteryLPoints` | `int` | live sample |
| `seasonUserStat.masteryLTime` | `int` | live sample |
| `seasonUserStat.masteryLevel` | `int` | live sample |
| `seasonUserStat.masteryPoints` | `int` | live sample |
| `seasonUserStat.masteryScore` | `int` | live sample |
| `seasonUserStat.masteryTime` | `int` | live sample |
| `seasonUserStat.mmr` | `int` | live sample |
| `seasonUserStat.nfBbbv` | `None` | live sample; only null observed |
| `seasonUserStat.nfBbbvs` | `None` | live sample; only null observed |
| `seasonUserStat.nfDuration` | `None` | live sample; only null observed |
| `seasonUserStat.nfEff100` | `None` | live sample; only null observed |
| `seasonUserStat.nfFinishedAt` | `None` | live sample; only null observed |
| `seasonUserStat.nfId` | `None` | live sample; only null observed |
| `seasonUserStat.nfLevel` | `None` | live sample; only null observed |
| `seasonUserStat.nfMines` | `None` | live sample; only null observed |
| `seasonUserStat.nfMobile` | `None` | live sample; only null observed |
| `seasonUserStat.nfPoints` | `int` | live sample |
| `seasonUserStat.nfSizeX` | `None` | live sample; only null observed |
| `seasonUserStat.nfSizeY` | `None` | live sample; only null observed |
| `seasonUserStat.quality` | `int` | live sample |
| `seasonUserStat.qualityScore` | `int` | live sample |
| `seasonUserStat.questScoreAll` | `int` | live sample |
| `seasonUserStat.rep` | `int` | live sample |
| `seasonUserStat.rewards` | `list[int]` | live sample |
| `seasonUserStat.rewards[]` | `int` | live sample |
| `seasonUserStat.rewardsAll` | `int` | live sample |
| `seasonUserStat.rewardsScore` | `int` | live sample |
| `seasonUserStat.score` | `int` | live sample |
| `seasonUserStat.scoreRank` | `int` | live sample |
| `seasonUserStat.season` | `int` | live sample |
| `seasonUserStat.seasons` | `int` | live sample |
| `seasonUserStat.ticketScoreAll` | `int` | live sample |
| `seasonUserStat.timeAll` | `int` | live sample |
| `seasonUserStat.timeBbbv` | `int` | live sample |
| `seasonUserStat.timeBbbvs` | `int` | live sample |
| `seasonUserStat.timeDuration` | `int` | live sample |
| `seasonUserStat.timeEff100` | `int` | live sample |
| `seasonUserStat.timeFinishedAt` | `str` | live sample |
| `seasonUserStat.timeId` | `int` | live sample |
| `seasonUserStat.timeLevel` | `int` | live sample |
| `seasonUserStat.timeMines` | `int` | live sample |
| `seasonUserStat.timeMobile` | `bool` | live sample |
| `seasonUserStat.timePoints` | `int` | live sample |
| `seasonUserStat.timeScore` | `int` | live sample |
| `seasonUserStat.timeSizeX` | `int` | live sample |
| `seasonUserStat.timeSizeY` | `int` | live sample |
| `seasonUserStat.userId` | `int` | live sample |
| `seasonUserStat.username` | `str` | live sample |
| `seasonUserStat.wins1` | `int` | live sample |
| `seasonUserStat.wins11` | `int` | live sample |
| `seasonUserStat.wins12` | `int` | live sample |
| `seasonUserStat.wins13` | `int` | live sample |
| `seasonUserStat.wins13_14` | `int` | live sample |
| `seasonUserStat.wins14` | `int` | live sample |
| `seasonUserStat.wins15` | `int` | live sample |
| `seasonUserStat.wins2` | `int` | live sample |
| `seasonUserStat.wins3` | `int` | live sample |
| `seasonUserStat.wins4` | `int` | live sample |
| `seasonUserStat.wins50` | `int` | live sample |
| `seasonUserStat.winsAll` | `int` | live sample |
| `seasonUserStat.winsNf` | `int` | live sample |
| `seasonUserStat.winsScore` | `int` | live sample |
| `seasonUserStat.ws1` | `int` | live sample |
| `seasonUserStat.ws1Duration` | `int` | live sample |
| `seasonUserStat.ws1FinishedAt` | `str` | live sample |
| `seasonUserStat.ws1Id` | `int` | live sample |
| `seasonUserStat.ws1Time` | `int` | live sample |
| `seasonUserStat.ws2` | `int` | live sample |
| `seasonUserStat.ws2Duration` | `None` | live sample; only null observed |
| `seasonUserStat.ws2FinishedAt` | `None` | live sample; only null observed |
| `seasonUserStat.ws2Id` | `None` | live sample; only null observed |
| `seasonUserStat.ws2Time` | `None` | live sample; only null observed |
| `seasonUserStat.ws3` | `int` | live sample |
| `seasonUserStat.ws3Duration` | `None` | live sample; only null observed |
| `seasonUserStat.ws3FinishedAt` | `None` | live sample; only null observed |
| `seasonUserStat.ws3Id` | `None` | live sample; only null observed |
| `seasonUserStat.ws3Time` | `None` | live sample; only null observed |
| `seasonUserStat.wsId` | `int` | live sample |
| `seasonUserStat.wsLId` | `int` | live sample |
| `seasonUserStat.wsLPoints` | `int` | live sample |
| `seasonUserStat.wsLTime` | `int` | live sample |
| `seasonUserStat.wsLevel` | `int` | live sample |
| `seasonUserStat.wsPoints` | `int` | live sample |
| `seasonUserStat.wsScore` | `int` | live sample |
| `seasonUserStat.wsTime` | `int` | live sample |
| `seasonUserStat.xmmr` | `int` | live sample |
| `timeResults` | `dict[str, JsonValue]` | live sample |
| `timeResults.1` | `dict[str, JsonValue]` | live sample |
| `timeResults.1.bbbv` | `int` | live sample |
| `timeResults.1.bbbvs` | `int` | live sample |
| `timeResults.1.duration` | `int` | live sample |
| `timeResults.1.eff100` | `int` | live sample |
| `timeResults.1.finishedAt` | `str` | live sample |
| `timeResults.1.gameId` | `int` | live sample |
| `timeResults.1.id` | `int` | live sample |
| `timeResults.1.level` | `int` | live sample |
| `timeResults.1.mines` | `int` | live sample |
| `timeResults.1.mobile` | `int` | live sample |
| `timeResults.1.nf` | `int` | live sample |
| `timeResults.1.nfOnly` | `int` | live sample |
| `timeResults.1.season` | `int` | live sample |
| `timeResults.1.sizeX` | `int` | live sample |
| `timeResults.1.sizeY` | `int` | live sample |
| `timeResults.1.sortBy3bvs` | `int` | live sample |
| `timeResults.1.userId` | `int` | live sample |
| `timeResults.11` | `dict[str, JsonValue]` | live sample |
| `timeResults.11.bbbv` | `int` | live sample |
| `timeResults.11.bbbvs` | `int` | live sample |
| `timeResults.11.duration` | `int` | live sample |
| `timeResults.11.eff100` | `int` | live sample |
| `timeResults.11.finishedAt` | `str` | live sample |
| `timeResults.11.gameId` | `int` | live sample |
| `timeResults.11.id` | `int` | live sample |
| `timeResults.11.level` | `int` | live sample |
| `timeResults.11.mines` | `int` | live sample |
| `timeResults.11.mobile` | `int` | live sample |
| `timeResults.11.nf` | `int` | live sample |
| `timeResults.11.nfOnly` | `int` | live sample |
| `timeResults.11.season` | `int` | live sample |
| `timeResults.11.sizeX` | `int` | live sample |
| `timeResults.11.sizeY` | `int` | live sample |
| `timeResults.11.sortBy3bvs` | `int` | live sample |
| `timeResults.11.userId` | `int` | live sample |
| `timeResults.12` | `dict[str, JsonValue]` | live sample |
| `timeResults.12.bbbv` | `int` | live sample |
| `timeResults.12.bbbvs` | `int` | live sample |
| `timeResults.12.duration` | `int` | live sample |
| `timeResults.12.eff100` | `int` | live sample |
| `timeResults.12.finishedAt` | `str` | live sample |
| `timeResults.12.gameId` | `int` | live sample |
| `timeResults.12.id` | `int` | live sample |
| `timeResults.12.level` | `int` | live sample |
| `timeResults.12.mines` | `int` | live sample |
| `timeResults.12.mobile` | `int` | live sample |
| `timeResults.12.nf` | `int` | live sample |
| `timeResults.12.nfOnly` | `int` | live sample |
| `timeResults.12.season` | `int` | live sample |
| `timeResults.12.sizeX` | `int` | live sample |
| `timeResults.12.sizeY` | `int` | live sample |
| `timeResults.12.sortBy3bvs` | `int` | live sample |
| `timeResults.12.userId` | `int` | live sample |
| `timeResults.13` | `dict[str, JsonValue]` | live sample |
| `timeResults.13.bbbv` | `int` | live sample |
| `timeResults.13.bbbvs` | `int` | live sample |
| `timeResults.13.duration` | `int` | live sample |
| `timeResults.13.eff100` | `int` | live sample |
| `timeResults.13.finishedAt` | `str` | live sample |
| `timeResults.13.gameId` | `int` | live sample |
| `timeResults.13.id` | `int` | live sample |
| `timeResults.13.level` | `int` | live sample |
| `timeResults.13.mines` | `int` | live sample |
| `timeResults.13.mobile` | `int` | live sample |
| `timeResults.13.nf` | `int` | live sample |
| `timeResults.13.nfOnly` | `int` | live sample |
| `timeResults.13.season` | `int` | live sample |
| `timeResults.13.sizeX` | `int` | live sample |
| `timeResults.13.sizeY` | `int` | live sample |
| `timeResults.13.sortBy3bvs` | `int` | live sample |
| `timeResults.13.userId` | `int` | live sample |
| `timeResults.14` | `dict[str, JsonValue]` | live sample |
| `timeResults.14.bbbv` | `int` | live sample |
| `timeResults.14.bbbvs` | `int` | live sample |
| `timeResults.14.duration` | `int` | live sample |
| `timeResults.14.eff100` | `int` | live sample |
| `timeResults.14.finishedAt` | `str` | live sample |
| `timeResults.14.gameId` | `int` | live sample |
| `timeResults.14.id` | `int` | live sample |
| `timeResults.14.level` | `int` | live sample |
| `timeResults.14.mines` | `int` | live sample |
| `timeResults.14.mobile` | `int` | live sample |
| `timeResults.14.nf` | `int` | live sample |
| `timeResults.14.nfOnly` | `int` | live sample |
| `timeResults.14.season` | `int` | live sample |
| `timeResults.14.sizeX` | `int` | live sample |
| `timeResults.14.sizeY` | `int` | live sample |
| `timeResults.14.sortBy3bvs` | `int` | live sample |
| `timeResults.14.userId` | `int` | live sample |
| `timeResults.2` | `dict[str, JsonValue]` | live sample |
| `timeResults.2.bbbv` | `int` | live sample |
| `timeResults.2.bbbvs` | `int` | live sample |
| `timeResults.2.duration` | `int` | live sample |
| `timeResults.2.eff100` | `int` | live sample |
| `timeResults.2.finishedAt` | `str` | live sample |
| `timeResults.2.gameId` | `int` | live sample |
| `timeResults.2.id` | `int` | live sample |
| `timeResults.2.level` | `int` | live sample |
| `timeResults.2.mines` | `int` | live sample |
| `timeResults.2.mobile` | `int` | live sample |
| `timeResults.2.nf` | `int` | live sample |
| `timeResults.2.nfOnly` | `int` | live sample |
| `timeResults.2.season` | `int` | live sample |
| `timeResults.2.sizeX` | `int` | live sample |
| `timeResults.2.sizeY` | `int` | live sample |
| `timeResults.2.sortBy3bvs` | `int` | live sample |
| `timeResults.2.userId` | `int` | live sample |
| `timeResults.3` | `dict[str, JsonValue]` | live sample |
| `timeResults.3.bbbv` | `int` | live sample |
| `timeResults.3.bbbvs` | `int` | live sample |
| `timeResults.3.duration` | `int` | live sample |
| `timeResults.3.eff100` | `int` | live sample |
| `timeResults.3.finishedAt` | `str` | live sample |
| `timeResults.3.gameId` | `int` | live sample |
| `timeResults.3.id` | `int` | live sample |
| `timeResults.3.level` | `int` | live sample |
| `timeResults.3.mines` | `int` | live sample |
| `timeResults.3.mobile` | `int` | live sample |
| `timeResults.3.nf` | `int` | live sample |
| `timeResults.3.nfOnly` | `int` | live sample |
| `timeResults.3.season` | `int` | live sample |
| `timeResults.3.sizeX` | `int` | live sample |
| `timeResults.3.sizeY` | `int` | live sample |
| `timeResults.3.sortBy3bvs` | `int` | live sample |
| `timeResults.3.userId` | `int` | live sample |
| `timeResults.50` | `dict[str, JsonValue]` | live sample |
| `timeResults.50.bbbv` | `int` | live sample |
| `timeResults.50.bbbvs` | `int` | live sample |
| `timeResults.50.diff` | `int` | live sample |
| `timeResults.50.duration` | `int` | live sample |
| `timeResults.50.eff100` | `int` | live sample |
| `timeResults.50.finishedAt` | `str` | live sample |
| `timeResults.50.gameId` | `int` | live sample |
| `timeResults.50.hasGems` | `bool` | live sample |
| `timeResults.50.hasTickets` | `bool` | live sample |
| `timeResults.50.hints` | `int` | live sample |
| `timeResults.50.id` | `int` | live sample |
| `timeResults.50.isFirstTime` | `bool` | live sample |
| `timeResults.50.isNewRecord` | `bool` | live sample |
| `timeResults.50.items` | `dict[str, JsonValue]` | live sample |
| `timeResults.50.items.10` | `int` | live sample |
| `timeResults.50.items.531` | `int` | live sample |
| `timeResults.50.items.546` | `int` | live sample |
| `timeResults.50.level` | `int` | live sample |
| `timeResults.50.mines` | `int` | live sample |
| `timeResults.50.mobile` | `int` | live sample |
| `timeResults.50.newRankScore` | `None` | live sample; only null observed |
| `timeResults.50.nf` | `bool` | live sample |
| `timeResults.50.reward` | `None` | live sample; only null observed |
| `timeResults.50.season` | `int` | live sample |
| `timeResults.50.sizeX` | `int` | live sample |
| `timeResults.50.sizeY` | `int` | live sample |
| `timeResults.50.userId` | `int` | live sample |
| `tokensUsed` | `dict[str, JsonValue]` | live sample |
| `tokensUsed.1` | `int` | live sample |
| `tokensUsed.2` | `int` | live sample |
| `tokensUsed.3` | `int` | live sample |
| `tokensUsed.4` | `int` | live sample |
| `tokensUsed.5` | `int` | live sample |
| `tokensUsed.6` | `int` | live sample |
| `tokensUsed.7` | `int` | live sample |
| `tokensUsed.8` | `int` | live sample |
| `user` | `dict[str, JsonValue]` | live sample |
| `user.country` | `str` | live sample |
| `user.deletedBy` | `None` | live sample; only null observed |
| `user.eliteAt` | `str` | live sample |
| `user.fromMobile` | `bool` | live sample |
| `user.id` | `int` | live sample |
| `user.info` | `str` | live sample |
| `user.online` | `bool` | live sample |
| `user.username` | `str` | live sample |
| `userStat` | `dict[str, JsonValue]` | live sample |
| `userStat.activityTotal` | `int` | live sample |
| `userStat.arenaCoinsAll` | `int` | live sample |
| `userStat.arenaDuration` | `int` | live sample |
| `userStat.arenaPoints` | `int` | live sample |
| `userStat.arenaScore` | `int` | live sample |
| `userStat.bbbvActive` | `int` | live sample |
| `userStat.bbbvAll` | `int` | live sample |
| `userStat.boosts` | `dict[str, JsonValue]` | live sample |
| `userStat.boosts.102102520` | `int` | live sample |
| `userStat.boosts.102102522` | `int` | live sample |
| `userStat.boosts.102102524` | `int` | live sample |
| `userStat.boosts.122523028` | `int` | live sample |
| `userStat.boosts.40841006` | `int` | live sample |
| `userStat.coins` | `int` | live sample |
| `userStat.coinsAll` | `int` | live sample |
| `userStat.coinsSeason` | `int` | live sample |
| `userStat.coinsSeasonScore` | `int` | live sample |
| `userStat.country` | `str` | live sample |
| `userStat.ct` | `None` | live sample; only null observed |
| `userStat.ctData` | `None` | live sample; only null observed |
| `userStat.diff` | `int` | live sample |
| `userStat.diffBbbv` | `int` | live sample |
| `userStat.diffDuration` | `int` | live sample |
| `userStat.diffFinishedAt` | `str` | live sample |
| `userStat.diffId` | `int` | live sample |
| `userStat.diffLevel` | `int` | live sample |
| `userStat.diffMines` | `int` | live sample |
| `userStat.diffScore` | `int` | live sample |
| `userStat.diffSizeX` | `int` | live sample |
| `userStat.diffSizeY` | `int` | live sample |
| `userStat.effBbbv` | `int` | live sample |
| `userStat.effBbbvs` | `int` | live sample |
| `userStat.effDuration` | `int` | live sample |
| `userStat.effEff100` | `int` | live sample |
| `userStat.effFinishedAt` | `str` | live sample |
| `userStat.effId` | `int` | live sample |
| `userStat.effLevel` | `int` | live sample |
| `userStat.effMines` | `int` | live sample |
| `userStat.effMobile` | `bool` | live sample |
| `userStat.effPoints` | `int` | live sample |
| `userStat.effScore` | `int` | live sample |
| `userStat.effSizeX` | `int` | live sample |
| `userStat.effSizeY` | `int` | live sample |
| `userStat.end1` | `int` | live sample |
| `userStat.end1Id` | `int` | live sample |
| `userStat.end2` | `int` | live sample |
| `userStat.end2Id` | `None` | live sample; only null observed |
| `userStat.end3` | `int` | live sample |
| `userStat.end3Id` | `None` | live sample; only null observed |
| `userStat.endBestId` | `int` | live sample |
| `userStat.endBestPoints` | `int` | live sample |
| `userStat.endDuration` | `int` | live sample |
| `userStat.endFinishedAt` | `str` | live sample |
| `userStat.endLevel` | `int` | live sample |
| `userStat.endNHId` | `None` | live sample; only null observed |
| `userStat.endNHPoints` | `int` | live sample |
| `userStat.endScore` | `int` | live sample |
| `userStat.eq` | `dict[str, JsonValue]` | live sample |
| `userStat.eq.0` | `str` | live sample |
| `userStat.eq.1` | `str` | live sample |
| `userStat.eq.2` | `str` | live sample |
| `userStat.eq.3` | `str` | live sample |
| `userStat.eq.4` | `str` | live sample |
| `userStat.eventItems` | `int` | live sample |
| `userStat.exp` | `int` | live sample |
| `userStat.expAll` | `int` | live sample |
| `userStat.expScore` | `int` | live sample |
| `userStat.extraStat` | `dict[str, JsonValue]` | live sample |
| `userStat.extraStat.a1` | `int` | live sample |
| `userStat.extraStat.a2` | `int` | live sample |
| `userStat.extraStat.a3` | `int` | live sample |
| `userStat.extraStat.a4` | `int` | live sample |
| `userStat.extraStat.a5` | `int` | live sample |
| `userStat.extraStat.a6` | `int` | live sample |
| `userStat.extraStat.a7` | `int` | live sample |
| `userStat.extraStat.a8` | `int` | live sample |
| `userStat.extraStat.aca` | `int` | live sample |
| `userStat.extraStat.acg` | `int` | live sample |
| `userStat.extraStat.acq` | `int` | live sample |
| `userStat.extraStat.arc10` | `int` | live sample |
| `userStat.extraStat.arc2` | `int` | live sample |
| `userStat.extraStat.arc3` | `int` | live sample |
| `userStat.extraStat.arc4` | `int` | live sample |
| `userStat.extraStat.arc5` | `int` | live sample |
| `userStat.extraStat.arc6` | `int` | live sample |
| `userStat.extraStat.arc7` | `int` | live sample |
| `userStat.extraStat.arc8` | `int` | live sample |
| `userStat.extraStat.arc9` | `int` | live sample |
| `userStat.extraStat.ca` | `int` | live sample |
| `userStat.extraStat.cg` | `int` | live sample |
| `userStat.extraStat.cq` | `int` | live sample |
| `userStat.extraStat.cs` | `int` | live sample |
| `userStat.extraStat.ea` | `int` | live sample |
| `userStat.extraStat.eg` | `int` | live sample |
| `userStat.extraStat.eia` | `int` | live sample |
| `userStat.extraStat.eic` | `int` | live sample |
| `userStat.extraStat.eig` | `int` | live sample |
| `userStat.extraStat.eiq` | `int` | live sample |
| `userStat.extraStat.eq` | `int` | live sample |
| `userStat.extraStat.g1` | `int` | live sample |
| `userStat.extraStat.g10` | `int` | live sample |
| `userStat.extraStat.g2` | `int` | live sample |
| `userStat.extraStat.g3` | `int` | live sample |
| `userStat.extraStat.g4` | `int` | live sample |
| `userStat.extraStat.g5` | `int` | live sample |
| `userStat.extraStat.g6` | `int` | live sample |
| `userStat.extraStat.g7` | `int` | live sample |
| `userStat.extraStat.g8` | `int` | live sample |
| `userStat.extraStat.g9` | `int` | live sample |
| `userStat.extraStat.qd` | `int` | live sample |
| `userStat.extraStat.qe` | `int` | live sample |
| `userStat.extraStat.qs` | `int` | live sample |
| `userStat.extraStat.t1` | `int` | live sample |
| `userStat.extraStat.t2` | `int` | live sample |
| `userStat.extraStat.t3` | `int` | live sample |
| `userStat.extraStat.t4` | `int` | live sample |
| `userStat.extraStat.t5` | `int` | live sample |
| `userStat.extraStat.t6` | `int` | live sample |
| `userStat.extraStat.t7` | `int` | live sample |
| `userStat.extraStat.t8` | `int` | live sample |
| `userStat.games` | `int` | live sample |
| `userStat.gemsAll` | `int` | live sample |
| `userStat.i5` | `int` | live sample |
| `userStat.id` | `int` | live sample |
| `userStat.items` | `dict[str, JsonValue]` | live sample |
| `userStat.items.10` | `int` | live sample |
| `userStat.items.102102520` | `int` | live sample |
| `userStat.items.102102522` | `int` | live sample |
| `userStat.items.102102524` | `int` | live sample |
| `userStat.items.114` | `int` | live sample |
| `userStat.items.118` | `int` | live sample |
| `userStat.items.122523028` | `int` | live sample |
| `userStat.items.128` | `int` | live sample |
| `userStat.items.138` | `int` | live sample |
| `userStat.items.15` | `int` | live sample |
| `userStat.items.157` | `int` | live sample |
| `userStat.items.16` | `int` | live sample |
| `userStat.items.161` | `int` | live sample |
| `userStat.items.168` | `int` | live sample |
| `userStat.items.17` | `int` | live sample |
| `userStat.items.174` | `int` | live sample |
| `userStat.items.178` | `int` | live sample |
| `userStat.items.18` | `int` | live sample |
| `userStat.items.182` | `int` | live sample |
| `userStat.items.188` | `int` | live sample |
| `userStat.items.191` | `int` | live sample |
| `userStat.items.192` | `int` | live sample |
| `userStat.items.2` | `int` | live sample |
| `userStat.items.3` | `int` | live sample |
| `userStat.items.30` | `int` | live sample |
| `userStat.items.31` | `int` | live sample |
| `userStat.items.316` | `int` | live sample |
| `userStat.items.32` | `int` | live sample |
| `userStat.items.33` | `int` | live sample |
| `userStat.items.358` | `int` | live sample |
| `userStat.items.359` | `int` | live sample |
| `userStat.items.361` | `int` | live sample |
| `userStat.items.362` | `int` | live sample |
| `userStat.items.365` | `int` | live sample |
| `userStat.items.370` | `int` | live sample |
| `userStat.items.371` | `int` | live sample |
| `userStat.items.372` | `int` | live sample |
| `userStat.items.373` | `int` | live sample |
| `userStat.items.374` | `int` | live sample |
| `userStat.items.375` | `int` | live sample |
| `userStat.items.376` | `int` | live sample |
| `userStat.items.377` | `int` | live sample |
| `userStat.items.378` | `int` | live sample |
| `userStat.items.379` | `int` | live sample |
| `userStat.items.380` | `int` | live sample |
| `userStat.items.381` | `int` | live sample |
| `userStat.items.391` | `int` | live sample |
| `userStat.items.392` | `int` | live sample |
| `userStat.items.394` | `int` | live sample |
| `userStat.items.395` | `int` | live sample |
| `userStat.items.396` | `int` | live sample |
| `userStat.items.4` | `int` | live sample |
| `userStat.items.403` | `int` | live sample |
| `userStat.items.404` | `int` | live sample |
| `userStat.items.405` | `int` | live sample |
| `userStat.items.406` | `int` | live sample |
| `userStat.items.407` | `int` | live sample |
| `userStat.items.408` | `int` | live sample |
| `userStat.items.40841006` | `int` | live sample |
| `userStat.items.410` | `int` | live sample |
| `userStat.items.418` | `int` | live sample |
| `userStat.items.419` | `int` | live sample |
| `userStat.items.420` | `int` | live sample |
| `userStat.items.421` | `int` | live sample |
| `userStat.items.422` | `int` | live sample |
| `userStat.items.423` | `int` | live sample |
| `userStat.items.424` | `int` | live sample |
| `userStat.items.425` | `int` | live sample |
| `userStat.items.426` | `int` | live sample |
| `userStat.items.43` | `int` | live sample |
| `userStat.items.430` | `int` | live sample |
| `userStat.items.431` | `int` | live sample |
| `userStat.items.432` | `int` | live sample |
| `userStat.items.433` | `int` | live sample |
| `userStat.items.434` | `int` | live sample |
| `userStat.items.435` | `int` | live sample |
| `userStat.items.436` | `int` | live sample |
| `userStat.items.437` | `int` | live sample |
| `userStat.items.438` | `int` | live sample |
| `userStat.items.439` | `int` | live sample |
| `userStat.items.440` | `int` | live sample |
| `userStat.items.441` | `int` | live sample |
| `userStat.items.445` | `int` | live sample |
| `userStat.items.448` | `int` | live sample |
| `userStat.items.45` | `int` | live sample |
| `userStat.items.450` | `int` | live sample |
| `userStat.items.453` | `int` | live sample |
| `userStat.items.454` | `int` | live sample |
| `userStat.items.455` | `int` | live sample |
| `userStat.items.46` | `int` | live sample |
| `userStat.items.463` | `int` | live sample |
| `userStat.items.465` | `int` | live sample |
| `userStat.items.466` | `int` | live sample |
| `userStat.items.470` | `int` | live sample |
| `userStat.items.478` | `int` | live sample |
| `userStat.items.480` | `int` | live sample |
| `userStat.items.481` | `int` | live sample |
| `userStat.items.482` | `int` | live sample |
| `userStat.items.483` | `int` | live sample |
| `userStat.items.485` | `int` | live sample |
| `userStat.items.486` | `int` | live sample |
| `userStat.items.490` | `int` | live sample |
| `userStat.items.491` | `int` | live sample |
| `userStat.items.492` | `int` | live sample |
| `userStat.items.493` | `int` | live sample |
| `userStat.items.494` | `int` | live sample |
| `userStat.items.495` | `int` | live sample |
| `userStat.items.496` | `int` | live sample |
| `userStat.items.497` | `int` | live sample |
| `userStat.items.498` | `int` | live sample |
| `userStat.items.499` | `int` | live sample |
| `userStat.items.5` | `int` | live sample |
| `userStat.items.500` | `int` | live sample |
| `userStat.items.501` | `int` | live sample |
| `userStat.items.508` | `int` | live sample |
| `userStat.items.51` | `int` | live sample |
| `userStat.items.511` | `int` | live sample |
| `userStat.items.512` | `int` | live sample |
| `userStat.items.525` | `int` | live sample |
| `userStat.items.526` | `int` | live sample |
| `userStat.items.528` | `int` | live sample |
| `userStat.items.531` | `int` | live sample |
| `userStat.items.532` | `int` | live sample |
| `userStat.items.544` | `int` | live sample |
| `userStat.items.6` | `int` | live sample |
| `userStat.items.63` | `int` | live sample |
| `userStat.items.64` | `int` | live sample |
| `userStat.items.65` | `int` | live sample |
| `userStat.items.66` | `int` | live sample |
| `userStat.items.67` | `int` | live sample |
| `userStat.items.7` | `int` | live sample |
| `userStat.items.8` | `int` | live sample |
| `userStat.items.9` | `int` | live sample |
| `userStat.j3` | `None` | live sample; only null observed |
| `userStat.lastSeason` | `int` | live sample |
| `userStat.mastery1` | `int` | live sample |
| `userStat.mastery1Duration` | `int` | live sample |
| `userStat.mastery1FinishedAt` | `str` | live sample |
| `userStat.mastery1Id` | `int` | live sample |
| `userStat.mastery1Points` | `int` | live sample |
| `userStat.mastery1Time` | `int` | live sample |
| `userStat.mastery2` | `int` | live sample |
| `userStat.mastery2Duration` | `int` | live sample |
| `userStat.mastery2FinishedAt` | `str` | live sample |
| `userStat.mastery2Id` | `int` | live sample |
| `userStat.mastery2Points` | `int` | live sample |
| `userStat.mastery2Time` | `int` | live sample |
| `userStat.mastery3` | `int` | live sample |
| `userStat.mastery3Duration` | `int` | live sample |
| `userStat.mastery3FinishedAt` | `str` | live sample |
| `userStat.mastery3Id` | `int` | live sample |
| `userStat.mastery3Points` | `int` | live sample |
| `userStat.mastery3Time` | `int` | live sample |
| `userStat.masteryId` | `int` | live sample |
| `userStat.masteryLId` | `int` | live sample |
| `userStat.masteryLPoints` | `int` | live sample |
| `userStat.masteryLTime` | `int` | live sample |
| `userStat.masteryLevel` | `int` | live sample |
| `userStat.masteryPoints` | `int` | live sample |
| `userStat.masteryScore` | `int` | live sample |
| `userStat.masteryTime` | `int` | live sample |
| `userStat.mmr` | `int` | live sample |
| `userStat.mmrRank` | `None` | live sample; only null observed |
| `userStat.nfBbbv` | `int` | live sample |
| `userStat.nfBbbvs` | `int` | live sample |
| `userStat.nfDuration` | `int` | live sample |
| `userStat.nfEff100` | `int` | live sample |
| `userStat.nfFinishedAt` | `str` | live sample |
| `userStat.nfId` | `int` | live sample |
| `userStat.nfLevel` | `int` | live sample |
| `userStat.nfMines` | `int` | live sample |
| `userStat.nfMobile` | `bool` | live sample |
| `userStat.nfPoints` | `int` | live sample |
| `userStat.nfSizeX` | `int` | live sample |
| `userStat.nfSizeY` | `int` | live sample |
| `userStat.quality` | `int` | live sample |
| `userStat.qualityScore` | `int` | live sample |
| `userStat.questScoreAll` | `int` | live sample |
| `userStat.rep` | `int` | live sample |
| `userStat.rewards` | `list[int]` | live sample |
| `userStat.rewards[]` | `int` | live sample |
| `userStat.rewardsAll` | `int` | live sample |
| `userStat.rewardsScore` | `int` | live sample |
| `userStat.score` | `int` | live sample |
| `userStat.scoreRank` | `int` | live sample |
| `userStat.season` | `int` | live sample |
| `userStat.seasons` | `int` | live sample |
| `userStat.ticketScoreAll` | `int` | live sample |
| `userStat.timeAll` | `int` | live sample |
| `userStat.timeBbbv` | `int` | live sample |
| `userStat.timeBbbvs` | `int` | live sample |
| `userStat.timeDuration` | `int` | live sample |
| `userStat.timeEff100` | `int` | live sample |
| `userStat.timeFinishedAt` | `str` | live sample |
| `userStat.timeId` | `int` | live sample |
| `userStat.timeLevel` | `int` | live sample |
| `userStat.timeMines` | `int` | live sample |
| `userStat.timeMobile` | `bool` | live sample |
| `userStat.timePoints` | `int` | live sample |
| `userStat.timeScore` | `int` | live sample |
| `userStat.timeSizeX` | `int` | live sample |
| `userStat.timeSizeY` | `int` | live sample |
| `userStat.userId` | `int` | live sample |
| `userStat.username` | `str` | live sample |
| `userStat.wins1` | `int` | live sample |
| `userStat.wins11` | `int` | live sample |
| `userStat.wins12` | `int` | live sample |
| `userStat.wins13` | `int` | live sample |
| `userStat.wins13_14` | `int` | live sample |
| `userStat.wins14` | `int` | live sample |
| `userStat.wins15` | `int` | live sample |
| `userStat.wins2` | `int` | live sample |
| `userStat.wins3` | `int` | live sample |
| `userStat.wins4` | `int` | live sample |
| `userStat.wins50` | `int` | live sample |
| `userStat.winsAll` | `int` | live sample |
| `userStat.winsNf` | `int` | live sample |
| `userStat.winsScore` | `int` | live sample |
| `userStat.ws1` | `int` | live sample |
| `userStat.ws1Duration` | `int` | live sample |
| `userStat.ws1FinishedAt` | `str` | live sample |
| `userStat.ws1Id` | `int` | live sample |
| `userStat.ws1Points` | `int` | live sample |
| `userStat.ws1Time` | `int` | live sample |
| `userStat.ws2` | `int` | live sample |
| `userStat.ws2Duration` | `int` | live sample |
| `userStat.ws2FinishedAt` | `str` | live sample |
| `userStat.ws2Id` | `int` | live sample |
| `userStat.ws2Points` | `int` | live sample |
| `userStat.ws2Time` | `int` | live sample |
| `userStat.ws3` | `int` | live sample |
| `userStat.ws3Duration` | `int` | live sample |
| `userStat.ws3FinishedAt` | `str` | live sample |
| `userStat.ws3Id` | `int` | live sample |
| `userStat.ws3Points` | `int` | live sample |
| `userStat.ws3Time` | `int` | live sample |
| `userStat.wsId` | `int` | live sample |
| `userStat.wsLId` | `int` | live sample |
| `userStat.wsLPoints` | `int` | live sample |
| `userStat.wsLTime` | `int` | live sample |
| `userStat.wsLevel` | `int` | live sample |
| `userStat.wsPoints` | `int` | live sample |
| `userStat.wsScore` | `int` | live sample |
| `userStat.wsTime` | `int` | live sample |
| `userStat.xmmr` | `int` | live sample |

## get_user_info

Controller: `GetUserInfoWS`. Role: **main**.

Observed request shapes:

- `userId`

Observed response fields: `user`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `int` | live sample |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `user` | `dict[str, JsonValue]` | live sample |
| `user.country` | `str` | live sample |
| `user.id` | `int` | live sample |
| `user.username` | `str \| None` | live sample |

## get_user_items

Controller: `GetUserItemsWS`. Role: **main**.

Observed request shapes:

- `userId`

Observed response fields: `items`, `userCoins`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `items` | `JsonValue` | unresolved |
| `userCoins` | `JsonValue` | unresolved |

## get_wallet_data

Controller: `GetWalletDataWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## get_watchers

Controller: `GetWatchersWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Observed request shapes:

- `g`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `g` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_wheel_data

Controller: `GetWheelDataWS`. Role: **main**.

Observed request shapes:

- `initRender`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `initRender` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_withdrawal_detail_data

Controller: `GetWithdrawalDetailDataWS`. Role: **main**.

Observed request shapes:

- `hash`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `hash` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## get_worth_graph_data

Controller: `GetWorthGraphDataWS`. Role: **main**.

Observed request shapes:

- `currency`, `dateFrom`, `userId`

Observed response fields: `result`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `currency` | `JsonValue` | unresolved |
| `dateFrom` | `JsonValue` | unresolved |
| `userId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `result` | `JsonValue` | unresolved |

## init_billing

Controller: `InitBillingWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `bonuses`, `premiumTo`, `rates`, `ratesYesterday`, `specialOffers`, `userExp`, `userItems`, `userScore`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `bonuses` | `JsonValue` | unresolved |
| `premiumTo` | `JsonValue` | unresolved |
| `rates` | `JsonValue` | unresolved |
| `ratesYesterday` | `JsonValue` | unresolved |
| `specialOffers` | `JsonValue` | unresolved |
| `userExp` | `JsonValue` | unresolved |
| `userItems` | `JsonValue` | unresolved |
| `userScore` | `JsonValue` | unresolved |

## init_chat

Controller: `InitChatWS`. Role: **chat**.

Observed request shapes:

- `generalChannels`, `needNotesChannel`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `generalChannels` | `JsonValue` | unresolved |
| `needNotesChannel` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## join_game

Controller: `JoinGameWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Observed request shapes:

- `c`, `g`, `h`, `u`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `c` | `JsonValue` | unresolved |
| `g` | `JsonValue` | unresolved |
| `h` | `JsonValue` | unresolved |
| `u` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## join_queue

Controller: `JoinQueueWS`. Role: **watcher**.

Observed request shapes:

- `lobbyCode`, `mode`, `server`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `lobbyCode` | `JsonValue` | unresolved |
| `mode` | `JsonValue` | unresolved |
| `server` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## leave_game

Controller: `LeaveGameWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## leave_queue

Controller: `LeaveQueueWS`. Role: **watcher**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## load_more

Controller: `LoadMoreWS`. Role: **chat**.

Observed request shapes:

- `channelId`, `fromMessageId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `channelId` | `JsonValue` | unresolved |
| `fromMessageId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## make_vip_purchase

Controller: `MakeVipPurchaseWS`. Role: **main**.

Observed request shapes:

- `coins`, `isDiscount`, `itemAmount`, `itemType`, `slotId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `coins` | `JsonValue` | unresolved |
| `isDiscount` | `JsonValue` | unresolved |
| `itemAmount` | `JsonValue` | unresolved |
| `itemType` | `JsonValue` | unresolved |
| `slotId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## mark_message

Controller: `MarkMessageWS`. Role: **chat**.

Observed request shapes:

- `channelId`, `id`, `mark`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `channelId` | `JsonValue` | unresolved |
| `id` | `JsonValue` | unresolved |
| `mark` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## new_game

Controller: `NewGameWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `JsonValue` (unresolved).

Response type: `JsonValue` (unresolved).

## observe_duel

Controller: `ObserveDuelWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Observed request shapes:

- `d`, `fi`, `u`; observed literals: `{"fi": true}`
- `d`, `fi`, `u`; observed literals: `{"fi": false}`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `d` | `JsonValue` | unresolved |
| `fi` | `bool` | frontend syntax |
| `u` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## participate_in_global_quest

Controller: `ParticipateInGlobalQuestWS`. Role: **main**.

Observed request shapes:

- `globalQuestId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `globalQuestId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## pay_with_wallet

Controller: `PayWithWalletWS`. Role: **main**.

Observed request shapes:

- `invoiceId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `invoiceId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## quit_duel

Controller: `QuitDuelWS`. Role: **main**.

Observed request shapes:

- `duelId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `duelId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## refresh_store_slots

Controller: `RefreshStoreSlotsWS`. Role: **main**.

Observed request shapes:

- `expectedPrice`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `expectedPrice` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## remove_message

Controller: `RemoveMessageWS`. Role: **chat**.

Observed request shapes:

- `id`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `id` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## replace_club_quest

Controller: `ReplaceClubQuestWS`. Role: **main**.

Observed request shapes:

- `questId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `questId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## replace_quest

Controller: `ReplaceQuestWS`. Role: **main**.

Observed request shapes:

- `questId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `questId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## report_chat_abuse

Controller: `ReportChatAbuseWS`. Role: **chat**.

Observed request shapes:

- `messageId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `messageId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## report_fail

Controller: `ReportFailWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Observed request shapes:

- `g`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `g` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## report_game_abuse

Controller: `ReportGameAbuseWS`. Role: **main**.

Observed request shapes:

- `gameId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## report_user_abuse

Controller: `ReportUserAbuseWS`. Role: **main**.

Observed request shapes:

- `abusedId`, `exchangeId`
- `abusedId`, `exchangeId`; observed literals: `{"exchangeId": null}`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `abusedId` | `JsonValue` | unresolved |
| `exchangeId` | `None` | frontend syntax; only null observed |

Response type: `JsonValue` (unresolved).

## request_hint

Controller: `RequestHintWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Observed request shapes:

- `g`, `ip`, `ph`, `pi`, `po`, `tb`, `tp`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `g` | `JsonValue` | unresolved |
| `ip` | `JsonValue` | unresolved |
| `ph` | `JsonValue` | unresolved |
| `pi` | `JsonValue` | unresolved |
| `po` | `JsonValue` | unresolved |
| `tb` | `JsonValue` | unresolved |
| `tp` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## reset_talents

Controller: `ResetTalentsWS`. Role: **main**.

Observed request shapes:

- `expectedPrice`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `expectedPrice` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## save_custom_talents

Controller: `SaveCustomTalentsWS`. Role: **main**.

Observed request shapes:

- `newCt`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `newCt` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## save_exchange

Controller: `SaveExchangeWS`. Role: **main**.

Observed request shapes:

- `buyerCoins`, `buyerId`, `buyerItems`, `exchangeId`, `sellerCoins`, `sellerItems`

Observed response fields: `exchangeId`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `buyerCoins` | `JsonValue` | unresolved |
| `buyerId` | `JsonValue` | unresolved |
| `buyerItems` | `JsonValue` | unresolved |
| `exchangeId` | `JsonValue` | unresolved |
| `sellerCoins` | `JsonValue` | unresolved |
| `sellerItems` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `exchangeId` | `JsonValue` | unresolved |

## save_fp

Controller: `SaveFpWS`. Role: **main**.

Observed request shapes:

- `fingerprint`, `session`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `fingerprint` | `JsonValue` | unresolved |
| `session` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## save_nft

Controller: `SaveNftWS`. Role: **main**.

Observed request shapes:

- `colors`, `flags`, `sizeX`, `sizeY`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `colors` | `JsonValue` | unresolved |
| `flags` | `JsonValue` | unresolved |
| `sizeX` | `JsonValue` | unresolved |
| `sizeY` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## save_talents

Controller: `SaveTalentsWS`. Role: **main**.

Observed request shapes:

- `newTalents`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `newTalents` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## save_trade

Controller: `SaveTradeWS`. Role: **main**.

Observed request shapes:

- `amount`, `itemType`, `price`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `amount` | `JsonValue` | unresolved |
| `itemType` | `JsonValue` | unresolved |
| `price` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## search_user

Controller: `SearchUserWS`. Role: **main**.

Observed request shapes:

- `isFinal`, `query`; observed literals: `{"isFinal": false}`
- `isFinal`, `query`; observed literals: `{"isFinal": true}`

Observed response fields: `isActive`, `result`, `userId`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isFinal` | `bool` | frontend syntax, live sample |
| `query` | `str` | live sample |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isActive` | `bool` | live sample |
| `result` | `list[dict[str, JsonValue]]` | live sample |
| `result[]` | `dict[str, JsonValue]` | live sample |
| `result[].country` | `str` | live sample |
| `result[].id` | `int` | live sample |
| `result[].username` | `str` | live sample |
| `userId` | `int \| None` | live sample |

## send_friend_quest

Controller: `SendFriendQuestWS`. Role: **main**.

Observed request shapes:

- `friendId`, `friendQuestIds`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `friendId` | `JsonValue` | unresolved |
| `friendQuestIds` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## send_message

Controller: `SendMessageWS`. Role: **chat**.

Observed request shapes:

- `channelId`, `text`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `channelId` | `JsonValue` | unresolved |
| `text` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## send_password_reset_email

Controller: `SendPasswordResetEmailWS`. Role: **main**.

Observed request shapes:

- `email`, `lang`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `email` | `JsonValue` | unresolved |
| `lang` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## set_channel_favorite

Controller: `SetChannelFavoriteWS`. Role: **chat**.

Observed request shapes:

- `channelId`, `isFavorite`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `channelId` | `JsonValue` | unresolved |
| `isFavorite` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## set_exchanges_as_viewed

Controller: `SetExchangesAsViewedWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `None`.

Response type: `JsonValue` (unresolved).

## set_friend_favorite

Controller: `SetFriendFavoriteWS`. Role: **main**.

Observed request shapes:

- `friendId`, `isFavorite`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `friendId` | `JsonValue` | unresolved |
| `isFavorite` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## sign_in

Controller: `SignInWS`. Role: **main**.

The browser marks this action as closing a session.

Observed request shapes:

- `password`, `usernameOrEmail`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `password` | `JsonValue` | unresolved |
| `usernameOrEmail` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## spin_wheel

Controller: `SpinWheelWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `newBonus`, `quests`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `newBonus` | `JsonValue` | unresolved |
| `quests` | `JsonValue` | unresolved |

## start_arena

Controller: `StartArenaWS`. Role: **main**.

Observed request shapes:

- `arenaType`, `betaTest`, `colorBlindness`, `isRoyale`, `mode`, `standardSkin`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `arenaType` | `JsonValue` | unresolved |
| `betaTest` | `JsonValue` | unresolved |
| `colorBlindness` | `JsonValue` | unresolved |
| `isRoyale` | `JsonValue` | unresolved |
| `mode` | `JsonValue` | unresolved |
| `standardSkin` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## start_watch

Controller: `StartWatchWS`. Role: **watcher**.

Observed request shapes:

- `playerId`

Observed response fields: `gameId`, `server`, `user`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `playerId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `gameId` | `JsonValue` | unresolved |
| `server` | `JsonValue` | unresolved |
| `user` | `JsonValue` | unresolved |

## sync_lobby_state

Controller: `SyncLobbyStateWS`. Role: **main**.

Observed request shapes:

- `code`

Observed response fields: `lobby`, `player1InGame`, `player2InGame`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `code` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `lobby` | `JsonValue` | unresolved |
| `player1InGame` | `JsonValue` | unresolved |
| `player2InGame` | `JsonValue` | unresolved |

## terminate_session

Controller: `TerminateSessionWS`. Role: **main**.

The browser marks this action as closing a session.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: not resolved.

Request type: `JsonValue` (unresolved).

Response type: `JsonValue` (unresolved).

## toggle_hint

Controller: `ToggleHintWS`. Role: **game**.

Pass `server=` using the game metadata. The client cannot infer it from a game ID.

Observed request shapes:

- `g`, `t`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `g` | `JsonValue` | unresolved |
| `t` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## toggle_store_lock

Controller: `ToggleStoreLockWS`. Role: **main**.

Observed request shapes:

- `slotId`

Observed response fields: `slotId`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `slotId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `slotId` | `JsonValue` | unresolved |

## track_promo

Controller: `TrackPromoWS`. Role: **main**.

Observed request shapes:

- `action`, `country`, `promoId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `action` | `JsonValue` | unresolved |
| `country` | `JsonValue` | unresolved |
| `promoId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## track_view

Controller: `TrackViewWS`. Role: **main**.

Observed request shapes:

- `id`, `type`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `id` | `JsonValue` | unresolved |
| `type` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## unblock_user

Controller: `UnblockUserWS`. Role: **chat**.

Observed request shapes:

- `unblockedId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `unblockedId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## unequip_item

Controller: `UnequipItemWS`. Role: **main**.

Observed request shapes:

- `eqType`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `eqType` | `str` | frontend syntax |

Response type: `JsonValue` (unresolved).

## update_allow_friend_quests

Controller: `UpdateAllowFriendQuestsWS`. Role: **main**.

Observed request shapes:

- `allowFriendQuests`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `allowFriendQuests` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## update_profile

Controller: `UpdateProfileWS`. Role: **main**.

Observed request shapes:

- `data`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `data` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## update_recap

Controller: `UpdateRecapWS`. Role: **main**.

Observed request shapes:

- `userId`, `year`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `userId` | `JsonValue` | unresolved |
| `year` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## update_user_storage

Controller: `UpdateUserStorageWS`. Role: **main**.

Observed request shapes:

- `storage`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `storage` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## upgrade_custom_talent

Controller: `UpgradeCustomTalentWS`. Role: **main**.

Observed request shapes:

- `talentId`

Observed response fields: `talent`.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `talentId` | `JsonValue` | unresolved |

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `talent` | `JsonValue` | unresolved |

## upgrade_item

Controller: `UpgradeItemWS`. Role: **main**.

Observed request shapes:

- `itemType`, `propToUpgrade`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `itemType` | `JsonValue` | unresolved |
| `propToUpgrade` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## use_auth_code

Controller: `UseAuthCodeWS`. Role: **main**.

The browser marks this action as closing a session.

Observed request shapes:

- `code`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `code` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## use_password_reset_hash

Controller: `UsePasswordResetHashWS`. Role: **main**.

Observed request shapes:

- `data`, `hash`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `data` | `dict[str, JsonValue]` | frontend syntax |
| `data.password` | `JsonValue` | unresolved |
| `data.password_repeat` | `JsonValue` | unresolved |
| `hash` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## verify_game_state

Controller: `VerifyGameStateWS`. Role: **main**.

Observed request shapes:

- `cellClass`, `expectedClass`, `gameId`, `html`, `type`, `x`, `y`; observed literals: `{"type": "html", "cellClass": "", "expectedClass": ""}`
- `cellClass`, `expectedClass`, `gameId`, `html`, `type`, `x`, `y`; observed literals: `{"type": "style", "cellClass": "", "expectedClass": ""}`
- `cellClass`, `expectedClass`, `gameId`, `html`, `type`, `x`, `y`; observed literals: `{"type": "html", "html": ""}`
- `cellClass`, `expectedClass`, `gameId`, `html`, `type`, `x`, `y`; observed literals: `{"type": "positions", "y": "", "cellClass": "", "expectedClass": "", "html": ""}`
- `cellClass`, `expectedClass`, `gameId`, `html`, `type`, `x`, `y`; observed literals: `{"type": "ac", "y": "", "cellClass": "", "expectedClass": "", "html": ""}`
- `cellClass`, `expectedClass`, `gameId`, `html`, `type`, `x`, `y`; observed literals: `{"type": "trust", "html": ""}`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `cellClass` | `str` | frontend syntax |
| `expectedClass` | `str` | frontend syntax |
| `gameId` | `JsonValue` | unresolved |
| `html` | `str` | frontend syntax |
| `type` | `str` | frontend syntax |
| `x` | `JsonValue` | unresolved |
| `y` | `str` | frontend syntax |

Response type: `JsonValue` (unresolved).

## verify_gm

Controller: `VerifyGmWS`. Role: **main**.

Request shape: no inline object resolved; may be empty or constructed dynamically.

Observed response fields: `isCheat`.

Request type: `None`.

Response type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `isCheat` | `JsonValue` | unresolved |

## view_channel

Controller: `ViewChannelWS`. Role: **chat**.

Observed request shapes:

- `channelId`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `channelId` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).

## vote_guide

Controller: `VoteGuideWS`. Role: **main**.

Observed request shapes:

- `guideId`, `vote`

Observed response fields: not resolved.

Request type: `dict[str, JsonValue]`.

| Field path | Python type | Evidence |
| --- | --- | --- |
| `guideId` | `JsonValue` | unresolved |
| `vote` | `JsonValue` | unresolved |

Response type: `JsonValue` (unresolved).
