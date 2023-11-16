-- Creates the database hbtn_0d_2
-- Creates the user user_0d_2
-- Grant usage on localhost for user_0d_2
-- Grant select privileges for user_0d_2 in hbtn_0d_2
-- Sets the password for user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
SET PASSWORD FOR 'user_0d_2'@'localhost' = 'user_0d_2_pwd';
