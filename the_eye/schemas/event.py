from datetime import datetime
from enum import Enum
from pydantic import BaseModel, UUID4
from pydantic.class_validators import validator


class EventCategory(Enum):
    PAGE_INTERACTION = "page interaction"
    FORM_INTERACTION = "form interaction"


class PostEventSchema(BaseModel):
    session_id: str
    category: str
    name: str
    data: dict
    timestamp: datetime

    @validator("timestamp")
    def timestamp_validator(cls, value):
        if value > datetime.utcnow():
            raise ValueError("Invalid timestamp")
        return value

    @validator("session_id")
    def session_id_validator(cls, value):
        UUID4(value)
        return value

    @validator("category")
    def session_id_validator(cls, value):
        # Keeping this field as str to easily add to the database
        EventCategory(value)
        return value
