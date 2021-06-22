"""Database models for all things related to a user."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login
from app.models.tags import Tag

user_tags = db.Table(
    'user_tag', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))


class User(UserMixin, db.Model):
    """Represents a user in the database"""
    description = db.Column(db.Text)
    email = db.Column(db.String(127), index=True, unique=True, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    is_godmother = db.Column(db.Boolean, nullable=False, default=0)
    nickname = db.Column(db.String(255),
                         index=True,
                         unique=True,
                         nullable=False)
    password_hash = db.Column(db.String(128))
    pronoun = db.Column(db.String(50))
    role = db.Column(db.Integer, nullable=False, default=0)
    tags = db.relationship('Tag',
                           secondary=user_tags,
                           backref='user',
                           cascade='all')

    def __repr__(self):
        return '<User {}>'.format(self.nickname)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_tags(self):
        """Returns a comma separated list of tags for this user."""
        tag_list = [t.value for t in self.tags]
        return ','.join(tag_list)

    def set_tags(self, tag_field):
        """Splits a comma separated list of tags into its elements and adds
        them to the tag list.
        """
        tag_list = tag_field.split(',')
        self.tags.clear()
        for t in tag_list:
            new_tag = Tag.query.filter_by(value=t).first()
            if not new_tag:
                new_tag = Tag()
                new_tag.value = t.strip()
            self.tags.append(new_tag)


@login.user_loader
def load_user(id):
    """Loads the user data through a given id."""
    return User.query.get(int(id))
