-- Volcando estructura de base de datos para astro_db
CREATE DATABASE IF NOT EXISTS astro_db;
\c astro_db;

-- Volcando estructura para tabla astro_db.ingredients
CREATE TABLE IF NOT EXISTS ingredients (
  id SERIAL PRIMARY KEY,
  type VARCHAR(10) CHECK (type IN ('BASE', 'COMPLEMENT')),
  name VARCHAR(50),
  price INT,
  calories INT,
  is_vegetarian BOOLEAN,
  units FLOAT,
  extra_data JSON,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla astro_db.ingredients_products
CREATE TABLE IF NOT EXISTS ingredients_products (
  ingredient_id INT NOT NULL,
  product_id INT NOT NULL,
  PRIMARY KEY (ingredient_id, product_id),
  FOREIGN KEY (ingredient_id) REFERENCES ingredients (id),
  FOREIGN KEY (product_id) REFERENCES products (id)
);

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla astro_db.products
CREATE TABLE IF NOT EXISTS products (
  id SERIAL PRIMARY KEY,
  type VARCHAR(10) CHECK (type IN ('CUP', 'MILK_SHAKE')),
  name VARCHAR(50),
  price INT,
  extra_data JSON,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
