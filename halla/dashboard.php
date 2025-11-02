<?php

    include 'wassup_db.php';

    if (!isset($_SESSION['user_id'])) {
        header("Location: /halla/logIn.php");
        exit();
    }

    $user_id = $_SESSION['user_id'];
    $full_name = $_SESSION['full_name'];
    $email = $_SESSION['email'];

    if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['post_content'])) {
        $content = trim($_POST['post_content']);
        
        if (!empty($content)) {
            $stmt = $conn->prepare("INSERT INTO posts (user_id, content) VALUES (?, ?)");
            $stmt->bind_param("is", $user_id, $content);
            $stmt->execute();
            $stmt->close();
            
            header("Location: /halla/dashboard.php");
            exit();
        }
    }

    if (isset($_GET['add_friend'])) {
        $friend_id = intval($_GET['add_friend']);
        
        if ($friend_id != $user_id) {
            $stmt = $conn->prepare("SELECT id FROM friendships WHERE (user_id = ? AND friend_id = ?) OR (user_id = ? AND friend_id = ?)");
            $stmt->bind_param("iiii", $user_id, $friend_id, $friend_id, $user_id);
            $stmt->execute();
            $result = $stmt->get_result();
            
            if ($result->num_rows == 0) {
                $stmt = $conn->prepare("INSERT INTO friendships (user_id, friend_id, status) VALUES (?, ?, 'pending')");
                $stmt->bind_param("ii", $user_id, $friend_id);
                $stmt->execute();
                
                $notification_content = "$full_name sent you a friend request.";
                $stmt = $conn->prepare("INSERT INTO notifications (user_id, content) VALUES (?, ?)");
                $stmt->bind_param("is", $friend_id, $notification_content);
                $stmt->execute();
            }
            
            $stmt->close();
            
            header("Location: /halla/dashboard.php#search");
            exit();
        }
    }

    if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['message_content']) && isset($_POST['receiver_id'])) {
        $receiver_id = intval($_POST['receiver_id']);
        $message_content = trim($_POST['message_content']);
        
        if (!empty($message_content) && $receiver_id != $user_id) {
            $stmt = $conn->prepare("INSERT INTO messages (sender_id, receiver_id, content) VALUES (?, ?, ?)");
            $stmt->bind_param("iis", $user_id, $receiver_id, $message_content);
            $stmt->execute();
            $stmt->close();
            
            header("Location: /halla/dashboard.php#inbox");
            exit();
        }
    }

    if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['update_profile'])) {
        $new_full_name = trim($_POST['full_name']);
        $new_email = trim($_POST['email']);
        $new_password = $_POST['password'];
        $confirm_password = $_POST['confirm_password'];
        
        if (!empty($new_full_name)) {
            $stmt = $conn->prepare("UPDATE users SET full_name = ? WHERE id = ?");
            $stmt->bind_param("si", $new_full_name, $user_id);
            $stmt->execute();
            $stmt->close();
            
            $_SESSION['full_name'] = $new_full_name;
        }
        
        if (!empty($new_email) && filter_var($new_email, FILTER_VALIDATE_EMAIL)) {
            $stmt = $conn->prepare("SELECT id FROM users WHERE email = ? AND id != ?");
            $stmt->bind_param("si", $new_email, $user_id);
            $stmt->execute();
            $result = $stmt->get_result();
            
            if ($result->num_rows == 0) {
                $stmt = $conn->prepare("UPDATE users SET email = ? WHERE id = ?");
                $stmt->bind_param("si", $new_email, $user_id);
                $stmt->execute();
                $stmt->close();
                
                $_SESSION['email'] = $new_email;
            }
            
            $stmt->close();
        }
        
        if (!empty($new_password) && $new_password === $confirm_password) {
            $hashed_password = password_hash($new_password, PASSWORD_DEFAULT);
            $stmt = $conn->prepare("UPDATE users SET password = ? WHERE id = ?");
            $stmt->bind_param("si", $hashed_password, $user_id);
            $stmt->execute();
            $stmt->close();
        }
        
        if (isset($_FILES['profile_picture']) && $_FILES['profile_picture']['error'] == 0) {
            $allowed_types = ['image/jpeg', 'image/png', 'image/gif'];
            $file_type = $_FILES['profile_picture']['type'];
            
            if (in_array($file_type, $allowed_types)) {
                $upload_dir = 'uploads/';
                if (!is_dir($upload_dir)) {
                    mkdir($upload_dir, 0777, true);
                }
                
                $file_extension = pathinfo($_FILES['profile_picture']['name'], PATHINFO_EXTENSION);
                $file_name = 'profile_' . $user_id . '_' . time() . '.' . $file_extension;
                $file_path = $upload_dir . $file_name;
                
                if (move_uploaded_file($_FILES['profile_picture']['tmp_name'], $file_path)) {
                    $stmt = $conn->prepare("UPDATE users SET profile_picture = ? WHERE id = ?");
                    $stmt->bind_param("si", $file_name, $user_id);
                    $stmt->execute();
                    $stmt->close();
                }
            }
        }
        
        header("Location: /halla/dashboard.php#friend-requests");
        exit();
    }

    $posts = [];
    $stmt = $conn->prepare("
        SELECT p.*, u.full_name, u.email, u.profile_picture 
        FROM posts p 
        JOIN users u ON p.user_id = u.id 
        ORDER BY p.created_at DESC
    ");
    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_assoc()) {
        $posts[] = $row;
    }
    $stmt->close();

    $users = [];
    $search_term = '';
    if (isset($_GET['search']) && !empty($_GET['search'])) {
        $search_term = trim($_GET['search']);
        $stmt = $conn->prepare("
            SELECT id, full_name, email, profile_picture 
            FROM users 
            WHERE (full_name LIKE ? OR email LIKE ?) AND id != ?
        ");
        $search_param = "%$search_term%";
        $stmt->bind_param("ssi", $search_param, $search_param, $user_id);
    } else {
        $stmt = $conn->prepare("
            SELECT id, full_name, email, profile_picture 
            FROM users 
            WHERE id != ?
            LIMIT 10
        ");
        $stmt->bind_param("i", $user_id);
    }

    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_assoc()) {
        $friend_stmt = $conn->prepare("
            SELECT status 
            FROM friendships 
            WHERE (user_id = ? AND friend_id = ?) OR (user_id = ? AND friend_id = ?)
        ");
        $friend_stmt->bind_param("iiii", $user_id, $row['id'], $row['id'], $user_id);
        $friend_stmt->execute();
        $friend_result = $friend_stmt->get_result();
        
        if ($friend_result->num_rows > 0) {
            $friend_data = $friend_result->fetch_assoc();
            $row['friendship_status'] = $friend_data['status'];
        } else {
            $row['friendship_status'] = 'none';
        }
        
        $friend_stmt->close();
        $users[] = $row;
    }

    $stmt->close();

    $notifications = [];
    $stmt = $conn->prepare("SELECT * FROM notifications WHERE user_id = ? ORDER BY created_at DESC");
    $stmt->bind_param("i", $user_id);
    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_assoc()) {
        $notifications[] = $row;
    }
    $stmt->close();

    $conversations = [];
    $stmt = $conn->prepare("
        SELECT DISTINCT u.id, u.full_name, u.email, u.profile_picture 
        FROM users u 
        JOIN messages m ON (u.id = m.sender_id OR u.id = m.receiver_id) 
        WHERE (m.sender_id = ? OR m.receiver_id = ?) AND u.id != ?
        ORDER BY m.created_at DESC
    ");
    $stmt->bind_param("iii", $user_id, $user_id, $user_id);
    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_assoc()) {

        $msg_stmt = $conn->prepare("
            SELECT content, created_at 
            FROM messages 
            WHERE (sender_id = ? AND receiver_id = ?) OR (sender_id = ? AND receiver_id = ?) 
            ORDER BY created_at DESC 
            LIMIT 1
        ");
        $msg_stmt->bind_param("iiii", $user_id, $row['id'], $row['id'], $user_id);
        $msg_stmt->execute();
        $msg_result = $msg_stmt->get_result();
        
        if ($msg_result->num_rows > 0) {
            $msg_data = $msg_result->fetch_assoc();
            $row['last_message'] = $msg_data['content'];
            $row['last_message_time'] = $msg_data['created_at'];
        } else {
            $row['last_message'] = 'No messages yet';
            $row['last_message_time'] = '';
        }
        
        $msg_stmt->close();
        $conversations[] = $row;
    }
    $stmt->close();

    $selected_conversation = null;
    $conversation_messages = [];
    if (isset($_GET['conversation'])) {
        $conversation_id = intval($_GET['conversation']);
        
        $stmt = $conn->prepare("
            SELECT id, full_name, email, profile_picture 
            FROM users 
            WHERE id = ? AND (id IN (
                SELECT sender_id FROM messages WHERE receiver_id = ?
                UNION
                SELECT receiver_id FROM messages WHERE sender_id = ?
            ))
        ");
        $stmt->bind_param("iii", $conversation_id, $user_id, $user_id);
        $stmt->execute();
        $result = $stmt->get_result();
        
        if ($result->num_rows > 0) {
            $selected_conversation = $result->fetch_assoc();
            
            $msg_stmt = $conn->prepare("
                SELECT m.*, u.full_name as sender_name 
                FROM messages m 
                JOIN users u ON m.sender_id = u.id 
                WHERE (m.sender_id = ? AND m.receiver_id = ?) OR (m.sender_id = ? AND m.receiver_id = ?) 
                ORDER BY m.created_at ASC
            ");
            $msg_stmt->bind_param("iiii", $user_id, $conversation_id, $conversation_id, $user_id);
            $msg_stmt->execute();
            $msg_result = $msg_stmt->get_result();
            
            while ($msg_row = $msg_result->fetch_assoc()) {
                $conversation_messages[] = $msg_row;
            }
            
            $msg_stmt->close();
            
            $update_stmt = $conn->prepare("
                UPDATE messages 
                SET is_read = 1 
                WHERE sender_id = ? AND receiver_id = ? AND is_read = 0
            ");
            $update_stmt->bind_param("ii", $conversation_id, $user_id);
            $update_stmt->execute();
            $update_stmt->close();
        }
        
        $stmt->close();
    }

    $stmt = $conn->prepare("SELECT profile_picture FROM users WHERE id = ?");
    $stmt->bind_param("i", $user_id);
    $stmt->execute();
    $result = $stmt->get_result();
    $user_data = $result->fetch_assoc();
    $profile_picture = $user_data['profile_picture'];
    $stmt->close();

?>

<!DOCTYPE html>

    <html>

        <head>

            <title>wassup? - Social Media Platform</title>

            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

            <style>

                body {
                    background: rgb(182, 240, 255);
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }

                .appName {
                    padding: 10px;
                    border: none;
                    background-color: rgb(145, 207, 255);
                    width: 100%;
                    margin-top: -10px;
                    text-align: center;
                    font-size: 24px;
                    color: white;
                    text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
                }

                .icons {
                    padding: 20px;
                    height: 50px;
                    width: 100%;
                    background-color: rgb(255, 211, 128);
                    display: flex;
                    gap: 15%;
                    align-items: center;
                    justify-content: center;
                    position: sticky;
                    top: 0;
                    z-index: 100;
                }

                .iconsPos {
                    margin: -10px 0px 0px 0px;
                }

                .glyphicon {
                    width: 20px;
                    height: 20px;
                    color: white;
                }

                .iconPadding {
                    padding: 5px;
                    height: 50px;
                    width: 90px;
                    background-color: rgb(255, 197, 88);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 10px;
                    transition: all 0.3s ease;
                    cursor: pointer;
                }

                .iconPadding:hover {
                    background-color: rgb(255, 166, 0);
                    transform: translateY(-3px);
                }

                nav a.active {
                    background-color: rgb(255, 166, 0);
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                }

                .postSearch {
                    width: 150px;
                    box-sizing: border-box;
                    border: none;
                    border-radius: 15px;
                    border-bottom: 2px solid rgb(255, 208, 67);
                    font-size: 14px;
                    background-color: transparent;
                    background-position: 10px 10px; 
                    background-repeat: no-repeat;
                    padding: 12px 20px 12px 20px;
                    transition: width 0.4s ease-in-out;
                    margin-top: 10px;
                    margin-bottom: 10px;
                    background-color: rgba(255,255,255,0.7);
                } 
                
                .postSearch:focus {
                    width: 50%;
                    outline: none;
                    border-bottom: 2px solid orange;
                    background-color: white;
                }

                .Post {
                    padding: 20px;
                    height: auto;
                    min-height: 40vh;
                    width: 40vw;
                    background-color: white;
                    border: none;
                    border-radius: 20px;
                    border-bottom: 4px solid orange;
                    box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.1);
                    display: grid;
                    justify-content: center;
                    align-items: center;
                    margin: 20px auto;
                    position: relative;
                } 
                
                .postPos {
                    margin-top:20px;
                }

                .profile_picture {
                    height: 50px;
                    width: 50px;
                    padding: 10px;
                    border: 1px solid orange;
                    border-radius: 50%;
                    background-color: grey;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-left: -80%;
                    margin-top: -100px;
                    background-size: cover;
                    background-position: center;
                }

                .userOnPostInfo {
                    display: flex;
                    width: 0%;
                    margin-bottom: -40px;
                    margin-top: 15vh;
                }

                .userName {
                    margin-right: 20%;
                    margin-top: -95px;
                    color: #333;
                } 

                .usersPadding {
                    padding: 30px;
                    width: 50vw;
                    height: 80vh;
                    background-color: white;
                    box-shadow: 0px 0px 20px 0px rgba(0,0,0,0.1);
                    border: none;
                    border-radius: 20px;
                    margin-top: 30px;
                    margin-bottom: 20px;
                    margin: 20px auto;
                    overflow-y: auto;
                }

                .post-content {
                    margin-top: 20px;
                    padding: 15px;
                    border-top: 1px solid #eee;
                    color: #555;
                }

                .post-actions {
                    display: flex;
                    justify-content: space-around;
                    margin-top: 15px;
                    padding-top: 10px;
                    border-top: 1px solid #eee;
                }

                .post-action {
                    cursor: pointer;
                    color: #666;
                    transition: color 0.3s;
                }

                .post-action:hover {
                    color: orange;
                }

                .user-card {
                    display: flex;
                    align-items: center;
                    padding: 15px;
                    margin: 10px 0;
                    background-color: rgba(255,255,255,0.8);
                    border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }

                .user-card-img {
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    margin-right: 25px;
                    background-color: #ddd;
                    background-size: cover;
                }

                .user-card-info {
                    flex-grow: 1;
                }

                .add-friend-btn {
                    background-color: orange;
                    color: white;
                    border: none;
                    padding: 5px 10px;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }

                .add-friend-btn:hover {
                    background-color: rgb(255, 166, 0);
                }

                .add-friend-btn.requested {
                    background-color: #ccc;
                    cursor: default;
                }

                .message-container {
                    height: 600px;
                    overflow-y: auto;
                    margin-bottom: 20px;
                    padding: 10px;
                    background-color: #f9f9f9;
                    border-radius: 10px;
                }

                .message {
                    margin: 10px;
                    padding: 10px 15px;
                    border-radius: 15px;
                    max-width: 70%;
                    word-wrap: break-word;
                }

                .received {
                    background-color: #e5e5ea;
                    margin-right: auto;
                }

                .sent {
                    background-color: orange;
                    color: white;
                    margin-left: auto;
                }

                .message-input {
                    display: flex;
                    margin-top: 10px;
                }

                .message-input input {
                    flex-grow: 1;
                    padding: 10px;
                    border: 1px solid #ddd;
                    border-radius: 20px;
                    outline: none;
                }

                .message-input button {
                    margin-left: 10px;
                    background-color: orange;
                    color: white;
                    border: none;
                    border-radius: 20px;
                    padding: 0 20px;
                    cursor: pointer;
                }

                .notification-item {
                    padding: 15px;
                    margin: 10px 0;
                    background-color: rgba(255,255,255,0.8);
                    border-radius: 10px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }

                .notification-item:hover {
                    background-color: rgba(255,211,128,0.3);
                }

                .settings-form {
                    display: flex;
                    flex-direction: column;
                    gap: 15px;
                }

                .settings-form input, .settings-form textarea {
                    padding: 10px;
                    border: 1px solid #ddd;
                    border-radius: 5px;
                }

                .settings-form button {
                    background-color: orange;
                    color: white;
                    border: none;
                    padding: 10px;
                    border-radius: 5px;
                    cursor: pointer;
                }

                .post-form {
                    width: 70%;
                    margin: 0 auto;
                    margin-bottom: 30px;
                }

                .post-form textarea {
                    width: 100%;
                    padding: 15px;
                    border: 1px solid #ddd;
                    border-radius: 10px;
                    resize: none;
                    margin-bottom: 10px;
                }

                .post-form button {
                    background-color: orange;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 20px;
                    cursor: pointer;
                    float: right;
                }

            </style>

        </head>

        <body>
            
            <p class="appName"><b>wassup</b></p>

            <div class="iconsPos">
                <nav class="icons">
                    <a class="iconPadding" href="#home">
                        <i class="glyphicon glyphicon-home"></i>
                    </a>
                    
                    <a class="iconPadding" href="#search">
                        <i class="glyphicon glyphicon-search"></i>
                    </a>

                    <a class="iconPadding" href="#inbox">
                        <i class="glyphicon glyphicon-envelope"></i>
                    </a>
                    
                    <a class="iconPadding" href="#notifications">
                        <i class="glyphicon glyphicon-bell"></i>
                    </a>

                    <a class="iconPadding" href="#friend-requests">
                        <i class="glyphicon glyphicon-user"></i>
                    </a>
                    
                    <a class="iconPadding" href="logout.php" style="text-decoration: none; color: white;">
                        <i class="glyphicon glyphicon-log-out"></i>
                    </a>
                </nav>
            </div>

            <div id="home" class="page">
                <form method="GET" action="dashboard.php" style="text-align: center;">
                    <input class="postSearch" type="search" name="search" placeholder="Search post:..." value="<?php echo htmlspecialchars($search_term); ?>">
                </form>

                <div class="post-form">
                    <form method="POST" action="dashboard.php">
                        <textarea name="post_content" placeholder="What's on your mind?" rows="3" required></textarea>
                        <button type="submit">Post</button>
                        <div style="clear: both;"></div>
                    </form>
                </div>

                <div class="postPos">
                    <?php if (empty($posts)): ?>
                        <div class="Post" style="text-align: center;">
                            <p>No posts yet. Be the first to post something!</p>
                        </div>
                    <?php else: ?>
                        <?php foreach ($posts as $post): ?>
                            <div class="Post">
                                <div class="userOnPostInfo">
                                    <div class="profile_picture" style="background-image: url('uploads/<?php echo $post['profile_picture']; ?>');"></div> 
                                    <p class="userName"> 
                                        <u style="border-bottom: 2px solid orange"><?php echo htmlspecialchars($post['full_name']); ?></u> 
                                        <br> 
                                        <small><?php echo htmlspecialchars($post['email']); ?></small>
                                        <br>
                                        <small>Posted <?php echo date('M j, Y g:i A', strtotime($post['created_at'])); ?></small>
                                    </p> 
                                </div>
                                <div class="post-content">
                                    <?php echo nl2br(htmlspecialchars($post['content'])); ?>
                                </div>
                                <div class="post-actions">
                                    <span class="post-action"><i class="glyphicon glyphicon-thumbs-up"></i> Like</span>
                                    <span class="post-action"><i class="glyphicon glyphicon-comment"></i> Comment</span>
                                    <span class="post-action"><i class="glyphicon glyphicon-share"></i> Share</span>
                                </div>
                            </div>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </div>
            </div>

            <div id="search" class="page" style="display: none;">
                <form method="GET" action="dashboard.php#search" style="text-align: center;">
                    <input class="postSearch" type="search" name="search" placeholder="Search User:..." value="<?php echo htmlspecialchars($search_term); ?>">
                    <button type="submit" style="display:none;">Search</button>
                </form>
                
                <div class="usersPadding" id="searchResults">
                    <?php if (empty($users)): ?>
                        <p style="text-align: center;">No users found.</p>
                    <?php else: ?>
                        <?php foreach ($users as $user): ?>
                            <div class="user-card">
                                <div class="user-card-img" style="background-image: url('uploads/<?php echo $user['profile_picture']; ?>');"></div>
                                <div class="user-card-info">
                                    <strong><?php echo htmlspecialchars($user['full_name']); ?></strong>
                                    <p><?php echo htmlspecialchars($user['email']); ?></p>
                                </div>
                                <?php if ($user['friendship_status'] == 'none'): ?>
                                    <a href="dashboard.php?add_friend=<?php echo $user['id']; ?>#search" class="add-friend-btn">Add Friend</a>
                                <?php elseif ($user['friendship_status'] == 'pending'): ?>
                                    <button class="add-friend-btn requested">Request Sent</button>
                                <?php elseif ($user['friendship_status'] == 'accepted'): ?>
                                    <button class="add-friend-btn requested">Friends</button>
                                <?php endif; ?>
                            </div>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </div>
            </div>

            <div id="inbox" class="page" style="display: none;">
                <div class="usersPadding">
                    <div style="display: flex; height: 100%;">
                        <div style="width: 30%; border-right: 1px solid #eee; padding-right: 10px; overflow-y: auto;">
                            <h4>Conversations</h4>
                            <?php if (empty($conversations)): ?>
                                <p>No conversations yet.</p>
                            <?php else: ?>
                                <?php foreach ($conversations as $conversation): ?>
                                    <a href="dashboard.php?conversation=<?php echo $conversation['id']; ?>#inbox" style="text-decoration: none; color: inherit;">
                                        <div class="user-card" style="cursor: pointer; <?php echo ($selected_conversation && $selected_conversation['id'] == $conversation['id']) ? 'background-color: #fff3e0;' : ''; ?>">
                                            <div class="user-card-img" style="background-image: url('uploads/<?php echo $conversation['profile_picture']; ?>');"></div>
                                            <div class="user-card-info">
                                                <strong><?php echo htmlspecialchars($conversation['full_name']); ?></strong>
                                                <p><?php echo strlen($conversation['last_message']) > 30 ? substr($conversation['last_message'], 0, 30) . '...' : $conversation['last_message']; ?></p>
                                                <small style="color: #666;"><?php echo !empty($conversation['last_message_time']) ? date('M j, g:i A', strtotime($conversation['last_message_time'])) : ''; ?></small>
                                            </div>
                                        </div>
                                    </a>
                                <?php endforeach; ?>
                            <?php endif; ?>
                        </div>
                        
                        <div style="flex-grow: 1; padding-left: 15px; display: flex; flex-direction: column;">
                            <?php if ($selected_conversation): ?>
                                <div style="border-bottom: 1px solid #eee; padding-bottom: 10px; margin-bottom: 10px;">
                                    <h4><?php echo htmlspecialchars($selected_conversation['full_name']); ?></h4>
                                </div>
                                
                                <div class="message-container">
                                    <?php if (empty($conversation_messages)): ?>
                                        <p style="text-align: center; color: #666;">No messages yet. Start a conversation!</p>
                                    <?php else: ?>
                                        <?php foreach ($conversation_messages as $message): ?>
                                            <div class="message <?php echo $message['sender_id'] == $user_id ? 'sent' : 'received'; ?>">
                                                <?php echo nl2br(htmlspecialchars($message['content'])); ?>
                                                <div style="font-size: 0.8em; margin-top: 5px; opacity: 0.7;">
                                                    <?php echo date('g:i A', strtotime($message['created_at'])); ?>
                                                </div>
                                            </div>
                                        <?php endforeach; ?>
                                    <?php endif; ?>
                                </div>
                                
                                <form method="POST" action="dashboard.php#inbox" class="message-input">
                                    <input type="hidden" name="receiver_id" value="<?php echo $selected_conversation['id']; ?>">
                                    <input type="text" name="message_content" placeholder="Type a message..." required>
                                    <button type="submit"><i class="glyphicon glyphicon-send"></i></button>
                                </form>
                            <?php else: ?>
                                <div style="display: flex; justify-content: center; align-items: center; height: 100%;">
                                    <p>Select a conversation to start messaging</p>
                                </div>
                            <?php endif; ?>
                        </div>
                    </div>
                </div>
            </div>

            <div id="notifications" class="page" style="display: none;">
                <div class="usersPadding">
                    <h4>Notifications</h4>
                    
                    <?php if (empty($notifications)): ?>
                        <p>No notifications yet.</p>
                    <?php else: ?>
                        <?php foreach ($notifications as $notification): ?>
                            <div class="notification-item">
                                <?php echo htmlspecialchars($notification['content']); ?>
                                <small style="display: block; color: #666;"><?php echo date('M j, Y g:i A', strtotime($notification['created_at'])); ?></small>
                            </div>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </div>
            </div>

            <div id="friend-requests" class="page" style="display: none;">
                <div class="usersPadding">
                    <div style="text-align: center; margin-bottom: 20px;">
                        <div class="profile_picture" style="margin: 0 auto; width: 100px; height: 100px; background-image: url('uploads/<?php echo $profile_picture; ?>');"></div>
                        <h3><?php echo htmlspecialchars($full_name); ?></h3>
                        <p><?php echo htmlspecialchars($email); ?></p>
                    </div>
                    
                    <form method="POST" action="dashboard.php#friend-requests" class="settings-form" enctype="multipart/form-data">
                        <input type="hidden" name="update_profile" value="1">
                        <h4>Update Profile</h4>
                        <input type="text" name="full_name" placeholder="Full Name" value="<?php echo htmlspecialchars($full_name); ?>">
                        <input type="email" name="email" placeholder="Email" value="<?php echo htmlspecialchars($email); ?>">
                        <input type="password" name="password" placeholder="New Password">
                        <input type="password" name="confirm_password" placeholder="Confirm New Password">
                        <input type="file" id="profile-pic-upload" name="profile_picture" style="display: none;" accept="image/*">
                        <button type="button" onclick="document.getElementById('profile-pic-upload').click()">Change Profile Picture</button>
                        <button type="submit">Save Changes</button>
                    </form>
                    
                    <div class="post-form" style="margin-top: 30px;">
                        <form method="POST" action="dashboard.php#friend-requests">
                            <h4>Create a Post</h4>
                            <textarea name="post_content" placeholder="What's on your mind?" rows="4" required></textarea>
                            <button type="submit">Post</button>
                            <div style="clear: both;"></div>
                        </form>
                    </div>
                </div>
            </div>

            <script>

                document.addEventListener('DOMContentLoaded', function() {
                    const hash = window.location.hash;
                    if (hash) {
                        const pageId = hash.substring(1);
                        document.querySelectorAll('.page').forEach((page) => {
                            page.style.display = 'none';
                        });
                        
                        document.getElementById(pageId).style.display = 'block';
                        document.querySelectorAll('nav a').forEach((link) => {
                            link.classList.remove('active');
                            if (link.getAttribute('href') === hash) {
                                link.classList.add('active');
                            }
                        });
                    }
                });

                document.querySelectorAll('nav a').forEach((link) => {
                    link.addEventListener('click', (e) => {
                        if (link.getAttribute('href').startsWith('#')) {
                            e.preventDefault();
                            const pageId = link.getAttribute('href').substring(1);
                            document.querySelectorAll('.page').forEach((page) => {
                                page.style.display = 'none';
                            });

                            document.getElementById(pageId).style.display = 'block';
                            document.querySelectorAll('nav a').forEach((link) => {
                                link.classList.remove('active');
                            });
                            link.classList.add('active');
                            
                            window.location.hash = '#' + pageId;
                        }
                    });
                });

                document.getElementById('userSearch')?.addEventListener('input', function() {
                    const searchTerm = this.value.toLowerCase();
                    const userCards = document.querySelectorAll('.user-card');
                    
                    userCards.forEach(card => {
                        const name = card.querySelector('strong').textContent.toLowerCase();
                        const email = card.querySelector('p').textContent.toLowerCase();
                        
                        if (name.includes(searchTerm) || email.includes(searchTerm)) {
                            card.style.display = 'flex';
                        } else {
                            card.style.display = 'none';
                        }
                    });
                });

                const messageContainer = document.querySelector('.message-container');
                if (messageContainer) {
                    messageContainer.scrollTop = messageContainer.scrollHeight;
                }
            </script>
        </body>
    </html>