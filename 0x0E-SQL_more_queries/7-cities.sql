-- create cities
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- activate the database
USE hbtn_0d_usa;
-- create the cities table
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id));