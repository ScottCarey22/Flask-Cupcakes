"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_CUPCAKE = 'https://thestayathomechef.com/wp-content/uploads/2017/12/Most-Amazing-Chocolate-Cupcakes-1-small.jpg'


def connect_db(app):
    """connect to db"""
    db.app = app
    db.init_app(app)


class Cupcake(db.Model):
    """Cupcake db"""

    __tablename__ = 'cupcakes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text, nullable=True, default=DEFAULT_CUPCAKE)
    rating = db.Column(db.Float, nullable=True)
