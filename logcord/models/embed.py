from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class _EmbedAuthor(BaseModel):
    """The model schema for a Discord embed author."""

    name: Optional[str] = Field(max_length=256)
    url: Optional[HttpUrl]
    icon_url: Optional[HttpUrl]
    proxy_icon_url: Optional[HttpUrl]


class _EmbedField(BaseModel):
    """The model schema for a Discord embed field."""

    name: str = Field(max_length=256)
    value: str = Field(max_length=1024)
    inline: Optional[bool]


class _EmbedFooter(BaseModel):
    """The model schema for a Discord embed footer."""

    text: str = Field(max_length=2048)
    icon_url: Optional[HttpUrl]
    proxy_icon_url: Optional[HttpUrl]


class _EmbedImage(BaseModel):
    """The model schema for a Discord embed image."""

    url: Optional[HttpUrl]
    proxy_url: Optional[HttpUrl]
    height: Optional[int] = Field(ge=1)
    width: Optional[int] = Field(ge=1)


class _EmbedProvider(BaseModel):
    """The model schema for a Discord embed provider."""

    name: Optional[str]
    url: Optional[HttpUrl]


class _EmbedVideo(BaseModel):
    """The model schema for a Discord embed provider."""

    url: Optional[HttpUrl]
    height: Optional[int] = Field(ge=1)
    width: Optional[int] = Field(ge=1)


class Embed(BaseModel):
    """The model schema for a Discord embed."""

    title: Optional[str] = Field(max_length=256)
    description: Optional[str] = Field(max_length=2048)
    url: Optional[HttpUrl]
    timestamp: Optional[datetime]
    color: Optional[int]

    author: Optional[_EmbedAuthor]
    fields_: Optional[list[_EmbedField]] = Field(max_items=25, alias='fields')
    footer: Optional[_EmbedFooter]
    image: Optional[_EmbedImage]
    provider: Optional[_EmbedProvider]
    video: Optional[_EmbedVideo]
