CREATE DATABASE eye;
CREATE USER 'the_eye_app'@'%' IDENTIFIED WITH mysql_native_password BY 'theeye123';
GRANT ALL ON eye.* TO 'the_eye_app'@'%';

FLUSH PRIVILEGES ;
USE eye;