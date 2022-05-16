from pydantic import BaseModel


class DefaultOutputSchema(BaseModel):
    message: str
