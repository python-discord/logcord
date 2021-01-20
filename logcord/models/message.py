from typing import Optional

from pydantic import BaseModel, Field

from logcord.models.attachment import Attachment
from logcord.models.embed import Embed
from logcord.models.sticker import Sticker


class Message(BaseModel):
    """The model schema for a Discord message."""

    id: int = Field(ge=0)

    author_id: int = Field(ge=0)
    author_name: str
    author_discriminator: int = Field(ge=1, le=9999)
    author_avatar_url: str = 'https://cdn.discordapp.com/embed/avatars/0.png'

    channel_id: int = Field(ge=0)

    content: str

    attachments: Optional[list[Attachment]]
    embeds: Optional[list[Embed]]
    stickers: Optional[list[Sticker]]
