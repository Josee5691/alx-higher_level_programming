-- create a user and grant previledges
-- create user
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- grant all previledges
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';
