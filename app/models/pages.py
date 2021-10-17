"""Database models for static pages"""
from app import db


class Static(db.Model):
    """Represents a static page in the database."""
    content = db.Column(db.Text)
    description = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    language = db.relationship('Language', backref='language', uselist=False)
    type = db.Column(db.Integer)

    def __repr__(self):
        return '<StaticPage {}>'.format(self.description)
