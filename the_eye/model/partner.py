from the_eye.settings.config import db


class Partner(db.Model):
    __tablename__ = 'partner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    api_token = db.Column(db.String(32), nullable=False, unique=True, index=True)