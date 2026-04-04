-- =============================================
-- COMPLEX POSTGRESQL SCHEMA (NO JSON, ENGLISH)
-- WITH MASSIVE DATA GENERATION
-- =============================================

-- Drop existing tables if you want to reset
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- =============================================
-- TABLE DEFINITIONS
-- =============================================

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    full_name TEXT,
    email TEXT UNIQUE,
    country TEXT,
    city TEXT,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE user_role (
    user_id INT REFERENCES users(id),
    role_id INT REFERENCES roles(id),
    assigned_at TIMESTAMP DEFAULT now(),
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id),
    name TEXT,
    description TEXT,
    price NUMERIC(12,2)
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    full_name TEXT,
    email TEXT,
    phone TEXT,
    country TEXT,
    city TEXT
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    order_date TIMESTAMP DEFAULT now(),
    status TEXT,
    notes TEXT
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    product_id INT REFERENCES products(id),
    quantity INT,
    unit_price NUMERIC(12,2)
);

CREATE TABLE carriers (
    id SERIAL PRIMARY KEY,
    name TEXT,
    country TEXT,
    city TEXT
);

CREATE TABLE shipments (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    carrier_id INT REFERENCES carriers(id),
    shipped_at TIMESTAMP,
    delivered_at TIMESTAMP,
    status TEXT
);

CREATE TABLE order_history (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    previous_status TEXT,
    new_status TEXT,
    changed_by INT REFERENCES users(id),
    changed_at TIMESTAMP DEFAULT now()
);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id),
    method TEXT,
    amount NUMERIC(12,2),
    paid_at TIMESTAMP
);

-- =============================================
-- MASSIVE INSERTS
-- =============================================

-- Users
INSERT INTO users (full_name, email, country, city, created_at)
SELECT
    'User ' || i,
    'user' || i || '@example.com',
    (ARRAY['Argentina','USA','Spain','Germany','Brazil'])[ (random()*4 + 1)::int ],
    (ARRAY['CityA','CityB','CityC','CityD'])[ (random()*3 + 1)::int ],
    now() - (random() * interval '365 days')
FROM generate_series(1, 50000) AS s(i);

-- Roles
INSERT INTO roles (name, description)
VALUES
('admin', 'System administrator'),
('manager', 'Business manager'),
('operator', 'Operations user'),
('viewer', 'Read-only user');

-- User-Role relations
INSERT INTO user_role (user_id, role_id, assigned_at)
	select id,
		(random()*3 + 1)::int,
    now() - (random() * interval '200 days')
	from users;


-- Categories
INSERT INTO categories (name, description)
SELECT
    'Category ' || i,
    'Auto-generated category ' || i
FROM generate_series(1, 200) AS s(i);

-- Products
INSERT INTO products (category_id, name, description, price)
SELECT
    (random()*199 + 1)::int,
    'Product ' || i,
    'Description for product ' || i,
    (random()*500 + 10)::numeric(12,2)
FROM generate_series(1, 300000) AS s(i);

-- Customers
INSERT INTO customers (full_name, email, phone, country, city)
SELECT
    'Customer ' || i,
    'customer' || i || '@example.com',
    '+1-555-' || (1000 + i),
    (ARRAY['Argentina','USA','Spain','Germany','Brazil'])[ (random()*4 + 1)::int ],
    (ARRAY['CityA','CityB','CityC','CityD'])[ (random()*3 + 1)::int ]
FROM generate_series(1, 80000) AS s(i);

-- Orders
INSERT INTO orders (customer_id, order_date, status, notes)
SELECT
    (random()*79999 + 1)::int,
    now() - (random() * interval '180 days'),
    (ARRAY['pending','completed','cancelled','processing'])[ (random()*3 + 1)::int ],
    'Auto-generated order ' || i
FROM generate_series(1, 500000) AS s(i);

-- Order Items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT
    (random()*499999 + 1)::int,
    (random()*299999 + 1)::int,
    (random()*10 + 1)::int,
    (random()*300 + 1)::numeric(12,2)
FROM generate_series(1, 1500000) AS s(i);

-- Carriers
INSERT INTO carriers (name, country, city)
SELECT
    'Carrier ' || i,
    (ARRAY['Argentina','USA','Spain'])[ (random()*2 + 1)::int ],
    (ARRAY['CityA','CityB','CityC'])[ (random()*2 + 1)::int ]
FROM generate_series(1, 100) AS s(i);

-- Shipments
INSERT INTO shipments (order_id, carrier_id, shipped_at, delivered_at, status)
SELECT
    (random()*499999 + 1)::int,
    (random()*99 + 1)::int,
    now() - (random() * interval '100 days'),
    now() - (random() * interval '50 days'),
    (ARRAY['shipped','in transit','delivered'])[ (random()*2 + 1)::int ]
FROM generate_series(1, 400000) AS s(i);

-- Order History
INSERT INTO order_history (order_id, previous_status, new_status, changed_by, changed_at)
SELECT
    (random()*499999 + 1)::int,
    (ARRAY['pending','processing','completed','cancelled'])[ (random()*3 + 1)::int ],
    (ARRAY['pending','processing','completed','cancelled'])[ (random()*3 + 1)::int ],
    (random()*49999 + 1)::int,
    now() - (random() * interval '90 days')
FROM generate_series(1, 600000) AS s(i);

-- Payments
INSERT INTO payments (order_id, method, amount, paid_at)
SELECT
    (random()*499999 + 1)::int,
    (ARRAY['credit_card','debit_card','cash','transfer'])[ (random()*3 + 1)::int ],
    (random()*400 + 5)::numeric(12,2),
    now() - (random() * interval '120 days')
FROM generate_series(1, 500000) AS s(i);

-- =============================================
-- DONE
-- =============================================
