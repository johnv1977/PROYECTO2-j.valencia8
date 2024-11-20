from db import db
from models.product import Product
from flask import Blueprint, flash, redirect, render_template, url_for


products_blueprint = Blueprint('products', __name__, url_prefix='/products')


@products_blueprint.route("/")
def index():
    _products = db.session.execute(db.select(Product)).scalars().all()
    return render_template("products/index.html", products=_products)


@products_blueprint.route("/<int:id>")
def show(id: int):
    _product = Product.query.get(id)
    return render_template("products/show.html", product=_product)


@products_blueprint.route("/register_sale/<int:id>")
def register_sale(id: int):
    _product = Product.query.get(id)
    _ingredients = _product.ingredients

    try:
        _product.register_sale()
        db.session.add(_product)

        for ingredient in _ingredients:
            db.session.add(ingredient)

        db.session.commit()

        flash(f'Se ha registrado una venta de {_product.name}', 'success')
        return redirect(url_for('app.index'))
    
    except ValueError as error:
        # estraer el mensaje de error
        flash(str(error), 'error')
        return redirect(url_for('app.index'))
