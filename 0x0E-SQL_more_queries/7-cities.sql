-- Creates the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates the cities table if it doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, -- Auto-generated ID
    state_id INT NOT NULL, -- State ID (foreign key)
    name VARCHAR(256) NOT NULL, -- City name (cannot be null)
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states (id) -- State ID references states table
);
