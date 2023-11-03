-- MySQL Setup for DEV

CREATE USER IF NOT EXISTS 'jc_user'@'localhost' IDENTIFIED BY 'root';
CREATE DATABASE IF NOT EXISTS jc_db;
GRANT ALL PRIVILEGES ON jc_db.* TO 'jc_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'jc_user'@'localhost';
FLUSH PRIVILEGES;