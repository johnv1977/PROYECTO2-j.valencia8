# https://flask-sqlalchemy.readthedocs.io/en/stable/quickstart/
from db import db
from flask import Blueprint, flash, redirect, render_template, url_for
from models.ingredient import Ingredient


ingredients_blueprint = Blueprint('ingredients', __name__, url_prefix='/ingredients')


@ingredients_blueprint.route("/")
def index():
    _ingredients = db.session.execute(db.select(Ingredient)).scalars().all()
    return render_template("ingredients/index.html", ingredients=_ingredients)


@ingredients_blueprint.route("/<int:id>")
def show(id: int):
    _ingredient = db.one_or_404(
        db.select(Ingredient).filter_by(id=id),
        description='Ingrediente no encontrado'
    )
    return render_template("ingredients/show.html", ingredient=_ingredient)


@ingredients_blueprint.route("/abastecer/<int:id>")
def supply(id: int):
    try:
        _ingredient = db.one_or_404(
            db.select(Ingredient).filter_by(id=id),
            description='Ingrediente no encontrado'
        )
        _ingredient.supply()

        db.session.add(_ingredient)
        db.session.commit()

        flash(f'Se abasteción el ingrediente {_ingredient.name}', 'success')
        return redirect(url_for('ingredients.index'))

    except Exception as error:
        flash(str(error), 'error')
        return redirect(url_for('ingredients.index'))
