from the_eye.model.event import Event
from the_eye.schemas.event import PostEventSchema


class EventController:
    def post(event: PostEventSchema):
        return Event.create_event(**event.dict())
