"""Sphinx + MyST + Furo: Markdown guides and Python API reference."""

from importlib.metadata import version as package_version

project = "wom-api"
author = "Tianyi Pu"
release = package_version("wom-api")
version = release
extensions = ["myst_parser", "sphinx.ext.autodoc", "sphinx.ext.napoleon"]
myst_heading_anchors = 3
html_theme = "furo"
exclude_patterns = ["_build"]
autodoc_typehints = "description"
nitpicky = False
