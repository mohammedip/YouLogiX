"""Routes package for YouLogiX.

Define APIRouters in submodules and import them here if you want
to expose a single `router` for the application.
"""

from fastapi import APIRouter

router = APIRouter()

__all__ = ["router"]
