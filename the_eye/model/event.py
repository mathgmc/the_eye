from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
from sqlalchemy.types import JSON

from the_eye.settings.config import db


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(36), nullable=False, index=True)
    category = db.Column(db.String(32), nullable=False, index=True)
    name = db.Column(db.String(32), nullable=False, index=True)
    data = db.Column(JSON, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    @classmethod
    def create_event(cls, **kwargs):
        func_error = "Error while trying to create event -"
        try:
            event = Event(**kwargs)
            db.session.add(event)
            db.session.commit()
            return "Success", 201
        except AssertionError as e:
            return f"{func_error} {e}", 400
        except Exception as e:
            return f"{func_error} {e}", 500
