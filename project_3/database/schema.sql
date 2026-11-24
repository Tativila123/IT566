CREATE DATABASE IF NOT EXISTS expenses
    DEFAULT CHARACTER SET utf8
    COLLATE utf8_general_ci;

USE expenses;

CREATE TABLE categories (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50) NOT NULL
) ENGINE=InnoDB;

CREATE TABLE expenses (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fk_category INT UNSIGNED NOT NULL,
    `date` DATE NOT NULL,
    description VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (fk_category) REFERENCES categories(id)
) ENGINE=InnoDB;

INSERT INTO categories (category)
VALUES ('Food'), ('Rent'), ('Transportation'), ('Bills'), ('Others');