<?php
include 'wassup_db.php';

$error = '';
$success = '';

if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $full_name = trim($_POST['full_name']);
    $email = trim($_POST['email']);
    $cell_number = trim($_POST['cell_number']);
    $password = $_POST['password'];
    $confirm_password = $_POST['confirm_password'];
    
    if (!empty($full_name) && !empty($email) && !empty($password) && !empty($confirm_password)) {
        if ($password === $confirm_password) {
            if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
                // Check if email already exists
                $stmt = $conn->prepare("SELECT id FROM users WHERE email = ?");
                $stmt->bind_param("s", $email);
                $stmt->execute();
                $result = $stmt->get_result();
                
                if ($result->num_rows == 0) {
                    // Hash password
                    $hashed_password = password_hash($password, PASSWORD_DEFAULT);
                    
                    // Insert user into database
                    $stmt = $conn->prepare("INSERT INTO users (full_name, email, cell_number, password) VALUES (?, ?, ?, ?)");
                    $stmt->bind_param("ssss", $full_name, $email, $cell_number, $hashed_password);
                    
                    if ($stmt->execute()) {
                        $success = "Account created successfully! You can now <a href='login.php'>login</a>.";
                    } else {
                        $error = "Error creating account. Please try again.";
                    }
                } else {
                    $error = "Email already exists.";
                }
                
                $stmt->close();
            } else {
                $error = "Invalid email format.";
            }
        } else {
            $error = "Passwords do not match.";
        }
    } else {
        $error = "Please fill in all required fields.";
    }
}
?>

<!DOCTYPE html>

    <html>

        <head>

            <title>Register - wassup?</title>

            <style>

                body {
                    background: rgb(182, 240, 255);
                }

                .padding {
                    padding: 20px;
                    border: none;
                    width: 40vw;
                    height: auto;
                    min-height: 70vh;
                    border-radius: 30px;
                    box-shadow: 0px 0px 30px 0px rgba(0,0,0,0.1);
                    display: grid;
                    justify-content: center;
                    align-items: center;
                    margin: 0 auto;
                    background: white;
                }

                .paddingAlign {
                    margin-top: 40px;
                }

                .appName {
                    padding: 10px;
                    height: 5vh;
                    border: none;
                    background-color: rgb(145, 207, 255);
                    width: 100%;
                    margin-top: -10px;
                    text-align: center;
                    color: white;
                    font-size: 30px;
                    margin-left: -10px;
                }

                input {
                    width: 30vw;
                    height: 5vh;
                    border-radius: 10px;
                    border: none;
                    background-color: transparent;
                    border-bottom: 1px solid rgb(145, 207, 255);
                    padding: 5px 10px;
                    margin: 5px 0;
                } 

                input:focus {
                    outline: none;
                    border-bottom: 3px solid rgb(145, 207, 255);
                }

                button {
                    width: 30vw;
                    height: 5vh;
                    border-radius: 10px;
                    border: none;
                    background-color: rgb(145, 207, 255);
                    color: white;
                    font-weight: bold;
                    cursor: pointer;
                    transition: background-color 0.3s;
                    margin-top: 10px;
                }

                button:hover {
                    background-color: rgb(120, 190, 255);
                }

                a {
                    color: black;
                    margin-left: 36%;
                    text-decoration: none;
                    font-size: 14px;
                }

                a:hover {
                    text-decoration: underline;
                }

                .error {
                    color: red;
                    text-align: center;
                    margin-bottom: 10px;
                }
                
                .success {
                    color: green;
                    text-align: center;
                    margin-bottom: 10px;
                }

            </style>

        </head>

        <body>

            <h1 class="appName">wassup</h1>

            <div class="paddingAlign">

                <form class="padding" method="POST" action="/halla/signIn.php">

                    <h2 style="text-align: center;">Create an account</h2>
                    
                    <?php if (!empty($error)): ?>
                        <div class="error"><?php echo $error; ?></div>
                    <?php endif; ?>
                    
                    <?php if (!empty($success)): ?>
                        <div class="success"><?php echo $success; ?></div>
                    <?php endif; ?>
                    
                    <input type="text" name="full_name" placeholder="Full Name:" required> <br>
                    
                    <input type="email" name="email" placeholder="Email:" required> <br>

                    <input type="tel" name="cell_number" placeholder="Cell number:"> <br>

                    <input type="password" name="password" placeholder="Password:" required> <br>

                    <input type="password" name="confirm_password" placeholder="Confirm Password:" required> <br>
                    <a href="/halla/logIn.php">Log in to your account</a> <br>

                    <a href="/halla/reset.php">Forgot password?</a> <br>

                    <button type="submit">Sign Up</button>

                </form>

            </div>
            
        </body>

    </html>