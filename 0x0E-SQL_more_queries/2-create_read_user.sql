-- creating a database and a user
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- grant select permission to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
