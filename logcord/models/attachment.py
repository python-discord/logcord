from pydantic import BaseModel, Field, HttpUrl


class Attachment(BaseModel):
    """The model schema for a Discord attachment."""
    id: int = Field(ge=0)

    filename: str
    size: int = Field(ge=1)

    url: HttpUrl
    proxy_url: HttpUrl

    height: int = Field(ge=1)
    width: int = Field(ge=1)
