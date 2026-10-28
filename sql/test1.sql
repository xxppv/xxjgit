CREATE DATABASE test_db;
USE test_db;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20),
    age INT
);
INSERT INTO users (name, age) VALUES ('张三', 20), ('李四', 22);