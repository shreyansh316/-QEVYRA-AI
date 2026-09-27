from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class ConversationCreate(BaseModel):
    title: str = Field(
        default="New conversation",
        min_length=1,
        max_length=200,
    )

    system_prompt: str | None = Field(
        default=None,
        max_length=10000,
    )


class ConversationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    title: str
    system_prompt: str | None
    created_at: datetime
    updated_at: datetime
