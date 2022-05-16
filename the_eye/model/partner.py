from werkzeug.exceptions import NotFound
from the_eye.settings.config import db


class Partner(db.Model):
    __tablename__ = "partner"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    api_token = db.Column(db.String(36), nullable=False, unique=True, index=True)

    @classmethod
    def get_partner(cls, api_token):
        try:
            partner = Partner.query.filter_by(api_token=api_token).first()
            return partner, 200
        except NotFound as e:
            return None, 404
        except Exception as e:
            return None, 500
