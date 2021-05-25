"""Database models for all things related to a user."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login


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

    def __repr__(self):
        return '<User {}>'.format(self.nickname)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


@login.user_loader
def load_user(id):
    """Loads the user data through a given id."""
    return User.query.get(int(id))
