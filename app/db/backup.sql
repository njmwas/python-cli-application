PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
-- CREATE TABLE alembic_version (
-- 	version_num VARCHAR(32) NOT NULL, 
-- 	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
-- );
-- INSERT INTO alembic_version VALUES('d32d432cbc25');
-- CREATE TABLE categories (
-- 	id INTEGER NOT NULL, 
-- 	name VARCHAR, 
-- 	description TEXT, 
-- 	discout VARCHAR, "createdAt" DATETIME, 
-- 	PRIMARY KEY (id)
-- );
-- INSERT INTO categories VALUES(1,'Food','Delicasies','0','2025-05-23 10:14:10.842329');
-- INSERT INTO categories VALUES(2,'Electronics','Boom boom','0','2025-05-23 10:14:10.842329');
-- CREATE TABLE products (
-- 	id INTEGER NOT NULL, 
-- 	name VARCHAR, 
-- 	price FLOAT, 
-- 	quantity INTEGER, 
-- 	category_id INTEGER, 
-- 	PRIMARY KEY (id), 
-- 	FOREIGN KEY(category_id) REFERENCES categories (id)
-- );
INSERT INTO products VALUES(1,'Peperony Pizza',1000.0,100,1);
INSERT INTO products VALUES(2,'Githeri',100.0,200,1);
-- CREATE TABLE product_details (
-- 	product_id INTEGER NOT NULL, 
-- 	manufacturer VARCHAR(100), 
-- 	warranty_period INTEGER, 
-- 	expiry_date DATE, 
-- 	barcode VARCHAR(50), 
-- 	PRIMARY KEY (product_id), 
-- 	FOREIGN KEY(product_id) REFERENCES products (id)
-- );
COMMIT;
