"""Flask app for Cupcakes"""

from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.app_context().push()

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "yumCupc@kes123"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def homepage():
    """render homepage"""
    return render_template('base.html')


@app.route('/api/cupcakes')
def all_cupcakes():
    """get data on all cupcakes"""
    cupcakes = [c.to_dict() for c in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """add new cupcakes and return details"""
    data = request.json
    cupcake = Cupcake(
        flavor=data['favlor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'],
    )

    db.session.add(cupcake)
    db.session.commit

    return (jsonify(cupcake=cupcake.to_dict()), 201)


@app.route('/api/cupcakes/<int:cupcake_int>')
def get_cupcake(cupcake_id):
    """show data on specific cupcake"""
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.to_dict())


@app.route('/api/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """update existing cupcake"""
    data = request.json
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    cupcake.flavor = data['flavor']
    cupcake.rating = data['rating']
    cupcake.size = data['size']
    cupcake.image = data['image']

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())


@app.route("/api/cupcakes/<int:cupcake_id>", methods=["DELETE"])
def remove_cupcake(cupcake_id):
    """delete cupcake and return message."""

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")
