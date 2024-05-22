-- Create the hbtn_0d_usa database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT UNIQUE, -- Auto-generated ID
    name VARCHAR(256) NOT NULL -- State name (cannot be null)
);
