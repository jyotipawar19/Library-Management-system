CREATE DATABASE IF NOT EXISTS library_management;
USE library_management;

CREATE TABLE IF NOT EXISTS books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    year_published INT,
    status VARCHAR(20) DEFAULT 'Available'
);
