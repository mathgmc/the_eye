from flask import Blueprint
from the_eye.controller import AddEventHandler
from the_eye.decorators import login_required, validate_schema
from the_eye.schemas import DefaultOutputSchema, PostEventSchema
from the_eye.model import Partner

event_blueprint = Blueprint("event", __name__, url_prefix="/event")


@event_blueprint.route("/", methods=["POST"])
@validate_schema(PostEventSchema, DefaultOutputSchema)
@login_required
def post_event(partner: Partner, data: PostEventSchema):
    AddEventHandler(data.dict()).start()
    return {"message": "Processing event"}, 200
