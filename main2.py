import sqlite3

connection = sqlite3.connect("test17.db")
print("BD create or open successful")
connection.close()

create_genders_query = """
CREATE TABLE IF NOT EXISTS genders (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
"""

create_user_query = """
CREATE TABLE IF NOT EXISTS users (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30) NOT NULL,
email VARCHAR(50) UNIQUE NOT NULL,
password VARCHAR(30) NOT NULL,
age INTEGER,
gender_id INTEGER,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (gender_id) REFERENCES genders (id)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);
"""

create_contacts_query = """
CREATE TABLE IF NOT EXISTS contacts (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name VARCHAR(30) NOT NULL,
email VARCHAR(50) NOT NULL,
phone VARCHAR(30) NOT NULL,
favorite BOOLEAN DEFAULT FALSE,
user_id INT NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (user_id) REFERENCES users (id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);
"""

create_customers_query = """CREATE TABLE IF NOT EXISTS Customers (
CustomerID INTEGER NOT NULL PRIMARY KEY, 
CustomerName VARCHAR(50) NOT NULL,
ContactName VARCHAR(30) NOT NULL,
Address VARCHAR(100) NOT NULL,
City VARCHAR(50) NOT NULL,
PostalCode VARCHAR(30) NOT NULL,
Country  VARCHAR(50) NOT NULL,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""


connection = sqlite3.connect("test17.db")
connection.execute(create_genders_query)
connection.execute(create_user_query)
connection.execute(create_contacts_query)
connection.execute(create_customers_query)
print("Table created successful")
connection.close()

connection = sqlite3.connect("test17.db")
insert_query_gender = """INSERT INTO genders (name)
VALUES ('male'), ('female');
"""
connection.execute(insert_query_gender)
connection.commit()

connection = sqlite3.connect("test17.db")
insert_users_query ="""
INSERT INTO users (name, email, password, age, gender_id)
VALUES ('Boris', 'boris@test.com', 'password', 23, 1),
('Alina', 'alina@test.com', 'password', 32, 2),
('Maksim', 'maksim@test.com', 'password', 40, 1);
 """

insert_contacts_query = """
INSERT INTO contacts (name, email, phone, favorite, user_id)
VALUES ('Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
('Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
('Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
('Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
('Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, 1);
 """


insert_Customers_query = """
INSERT INTO Customers (CustomerID, CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES (89, 'White Clover Markets', 'Karl Jablonski', '305 - 14th Ave. S.Suite 3B', 'Seattle', '98128', 'USA'),
(90,'Wilman Kala', 'Matti Karttunen', 'Keskuskatu 45', 'Helsinki', '21240', 'Finland'),
(91, 'Wolski', 'Zbyszek', 'ul.Filtrowa 68', 'Walla', '01-012', 'Poland');
 """

connection.execute(insert_users_query)
connection.execute(insert_contacts_query)
connection.execute(insert_Customers_query)
connection.commit()
connection.close()

connection = sqlite3.connect("test17.db")

for d in connection.execute("""SELECT * FROM users WHERE age > 25;"""):
    print(d)

print("*" * 40)
print()

for d in connection.execute("""SELECT * FROM contacts WHERE favorite = 1;"""):
    print(d)