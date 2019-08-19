-- Script that prepares a MySQL server:
-- Database: hbnb_test_db
-- New user: hbnb_test in localhost
-- Password of hbnb_test: hbnb_test_pwd
-- hbnb_test has all privileges on db hbnb_test_db
-- hbnb_test has SELECT privilege on db performance_schema
-- Does not fail if hbnb_test or hbnb_test_db already exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost';
ALTER USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
