CREATE TABLE IF NOT EXISTS Category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES Category(id)
);

CREATE TABLE IF NOT EXISTS Customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT
);

CREATE TABLE IF NOT EXISTS Cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER DEFAULT 1,
    FOREIGN KEY (customer_id) REFERENCES Customer(id),
    FOREIGN KEY (product_id) REFERENCES Product(id)
);

CREATE TABLE IF NOT EXISTS AdminUser (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);

ALTER TABLE Product ADD COLUMN stock INTEGER DEFAULT 0;

DELETE FROM Cart WHERE quantity = 0;

SELECT name, price FROM Product;

SELECT name, price FROM Product
WHERE id IN (
    SELECT product_id FROM Cart WHERE quantity > 2
);


SELECT * FROM Product WHERE price > 100;
SELECT * FROM Customer WHERE name LIKE 'A%';
SELECT * FROM Product WHERE stock < 10;

SELECT MAX(price) AS MaxPrice FROM Product;
SELECT MIN(price) AS MinPrice FROM Product;
SELECT COUNT(*) AS TotalCustomers FROM Customer;
