"""Database models for searchable tags"""
from app import db, login


class Tag(db.Model):
    """Represents a simple searchable tag in the database"""
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<Tag {}>'.format(self.value)
