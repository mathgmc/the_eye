from flask import Blueprint
from the_eye.controller import AddEventHandler
from the_eye.decorators import validate_schema
from the_eye.schemas import DefaultOutputSchema, PostEventSchema

event_blueprint = Blueprint("event", __name__, url_prefix="/event")


@event_blueprint.route("/", methods=["POST"])
@validate_schema(PostEventSchema, DefaultOutputSchema)
def post_event(data: PostEventSchema):
    AddEventHandler(data.dict()).start()
    return {"message": "Processing event"}, 200
