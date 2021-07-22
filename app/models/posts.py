"""Database models for posts"""
from app import db
from app.models import languages


class TypeOfPost(db.Model):
    """Declares the types of post that exist"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True, nullable=False)

    def __repr__(self):
        return '<TypeOfPost {}>'.format(self.name)


class Post(db.Model):
    """A posted text in a blog or other place that allows texts
       to be displayed.
    """
    author = db.relationship('User', backref=db.backref('posts'), lazy=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    language = db.relationship('Language', backref=db.backref('languages'), lazy=True)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'))
    type = db.relationship('TypeOfPost', backref=db.backref('types_of_post'), lazy=True)
    type_id = db.Column(db.Integer, db.ForeignKey('type_of_post.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.id)
