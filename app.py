from flask import Flask
from config import app_config, app_define_global_vars
from db import db, load_models, restart_db
# Controllers
from controllers.app_controller import app_blueprint, define_error_handlers
from controllers.ingredients_controller import ingredients_blueprint
from controllers.products_controller import products_blueprint
from data.example_data import data_ingredients, data_products


# Iniciar y configurar la aplicación
app = Flask(__name__, template_folder="views")
app_config(app)

# Iniciar la base de datos
db.init_app(app)
load_models()
restart_db(app)

# Insertar datos de ejemplos
data_ingredients(app, db)
data_products(app, db)

# Registrar las rutas
app.register_blueprint(app_blueprint)
app.register_blueprint(ingredients_blueprint)
app.register_blueprint(products_blueprint)

# Definir manejadores de errores en las rutas
define_error_handlers(app)

# Definir variables globales
app_define_global_vars(app)


if __name__ == "__main__":
    app.run(debug=True)
