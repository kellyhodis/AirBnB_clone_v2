-- Script that prepares a MySQL server:
-- Database: hbnb_dev_db
-- New user: hbnb_dev in localhost
-- Passowrd of hbnb_dev: hbnb_dev_pwd
-- hbnb_dev has all privileges on db hbnb_dev_db
-- hbnb_dev has SELECT privilege on db performance_schema
-- Does not fail if hbnb_dev_db or hbnb_dev already exists
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
ALTER USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
