from pydantic import BaseModel
import uuid

from datetime import datetime

from pydantic.fields import Field


class MessageBase(BaseModel):
    type_: str = Field(alias="type")
    body: dict
    destination: str
    deliver_after: datetime # = Field(alias="deliverAfter")


class MessageCreate(MessageBase):
    ...


class Message(MessageBase):
    id_: uuid.UUID = Field(alias="id")
    created_at: datetime # = Field(alias="createdAt")
    updated_at: datetime # = Field(alias="updatedAt")

    class Config:
        orm_mode = True
