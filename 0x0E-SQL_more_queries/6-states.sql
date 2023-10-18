-- create database and table
--create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- activate database
USE hbtn_0d_usa;
-- create table
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
