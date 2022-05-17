from datetime import datetime
from pydantic import BaseModel, UUID4, constr, root_validator
from pydantic.class_validators import validator
from pydoc import locate

from the_eye.schemas import EventCategory


class PostEventSchema(BaseModel):
    session_id: constr(max_length=36)
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
    def category_validator(cls, value):
        # Keeping this field as str to easily add to the database
        EventCategory(value)
        return value

    @root_validator
    def payload_validator(cls, values):
        formated_category = values.get("category").title().replace(" ", "")
        # Validate Names
        enum_name = formated_category + "NamesEnum"
        names_enum_class = locate(f"the_eye.schemas.{enum_name}")
        if not names_enum_class:
            raise ValueError(
                f"There is no NamesEnum for this category: {enum_name} enum not found"
            )
        names_enum_class(values.get("name"))

        # Validate Data
        formated_name = values.get("name").title().replace(" ", "")
        model_name = f"{formated_category}{formated_name}Data"
        data_model_class = locate(f"the_eye.schemas.{model_name}")
        if not data_model_class:
            raise ValueError(
                f"There is no data model for this category+name: {model_name} model not found"
            )
        data_model_class(**values.get("data"))

        return values
