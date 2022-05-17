from flask import Blueprint
from the_eye.controller.event import AddEventhandler
from the_eye.decorators import validate_schema

from the_eye.schemas.common import DefaultOutputSchema
from the_eye.schemas.event import PostEventSchema

event_blueprint = Blueprint("event", __name__, url_prefix="/event")


@event_blueprint.route("/", methods=["POST"])
@validate_schema(PostEventSchema, DefaultOutputSchema)
def post_event(data: PostEventSchema):
    AddEventhandler(data.dict()).start()
    return {"message": "Processing event"}, 200
