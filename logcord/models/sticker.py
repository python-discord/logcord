from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field


class _StickerType(IntEnum):
    """The different format types of Discord stickers."""
    png = 0
    apng = 1
    lottie = 2


class Sticker(BaseModel):
    """The model schema for a Discord sticker."""
    id: int = Field(ge=0)
    pack_id: int = Field(ge=0)

    name: str
    description: str
    tags: list[str]

    asset: str
    preview_asset: Optional[str]

    format_type: _StickerType
