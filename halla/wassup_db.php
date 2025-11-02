<?php

    $host = 'localhost';
    $username = 'root';
    $password = '';
    $database = 'wassup_db';

    $conn = new mysqli($host, $username, $password);

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $sql = "CREATE DATABASE IF NOT EXISTS $database";

    if ($conn->query($sql)) {
        $conn->select_db($database);
    } else {
        die("Error creating database: " . $conn->error);
    }

    $sql = "CREATE TABLE IF NOT EXISTS users (
        id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        email VARCHAR(255) UNIQUE NOT NULL,
        cell_number VARCHAR(20),
        password VARCHAR(255) NOT NULL,
        profile_picture VARCHAR(255) DEFAULT 'default_profile.jpg',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )";

    if (!$conn->query($sql)) {
        die("Error creating users table: " . $conn->error);
    }

    $sql = "CREATE TABLE IF NOT EXISTS posts (
        id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        user_id INT(11) UNSIGNED NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )";

    if (!$conn->query($sql)) {
        die("Error creating posts table: " . $conn->error);
    }

    $sql = "CREATE TABLE IF NOT EXISTS friendships (
        id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        user_id INT(11) UNSIGNED NOT NULL,
        friend_id INT(11) UNSIGNED NOT NULL,
        status ENUM('pending', 'accepted', 'rejected') DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (friend_id) REFERENCES users(id) ON DELETE CASCADE,
        UNIQUE KEY unique_friendship (user_id, friend_id)
    )";

    if (!$conn->query($sql)) {
        die("Error creating friendships table: " . $conn->error);
    }

    $sql = "CREATE TABLE IF NOT EXISTS messages (
        id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        sender_id INT(11) UNSIGNED NOT NULL,
        receiver_id INT(11) UNSIGNED NOT NULL,
        content TEXT NOT NULL,
        is_read TINYINT(1) DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (sender_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (receiver_id) REFERENCES users(id) ON DELETE CASCADE
    )";

    if (!$conn->query($sql)) {
        die("Error creating messages table: " . $conn->error);
    }

    $sql = "CREATE TABLE IF NOT EXISTS notifications (
        id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        user_id INT(11) UNSIGNED NOT NULL,
        content TEXT NOT NULL,
        is_read TINYINT(1) DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )";

    if (!$conn->query($sql)) {
        die("Error creating notifications table: " . $conn->error);
    }

    session_start();

?>