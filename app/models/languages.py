"""Database models for language support"""
from app import db


class Language(db.Model):
    """Represents a language definition in the database"""
    id = db.Column(db.Integer, primary_key=True)
    iso_code = db.Column(db.String(3), index=True, unique=True, nullable=False)
    name = db.Column(db.Text, unique=True)

    def __repr__(self):
        return '<Language {}>'.format(self.name)
