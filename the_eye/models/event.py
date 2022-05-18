import logging
from sqlalchemy.types import JSON
from sqlalchemy.exc import DataError
from the_eye.settings.config import db


class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(36), nullable=False, index=True)
    category = db.Column(db.String(32), nullable=False, index=True)
    name = db.Column(db.String(32), nullable=False, index=True)
    data = db.Column(JSON, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    partner_id = db.Column(db.Integer, db.ForeignKey("partner.id"), nullable=False)

    @classmethod
    def create_event(cls, **kwargs):
        try:
            event = Event(**kwargs)
            db.session.add(event)
            db.session.commit()
            return 201
        except DataError as e:
            logging.error(e.orig)
            return 400
        except Exception as e:
            logging.error(e)
            return 500
