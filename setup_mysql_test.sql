-- Create the database
CREATE TABLE IF NOT EXISTS hbnb_test_db;

-- Create the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

--Grant privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

--Grant SELECT privileges on the database performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush privilege to reload the grant table
FLUSH PRIVILEGES;
