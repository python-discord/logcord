from datetime import datetime

from pydantic import BaseModel, Field

from logcord.models.message import Message


class MessageLog(BaseModel):
    """The model schema for a message log."""

    id: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    messages: list[Message]
