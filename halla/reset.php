<?php

    include 'db_connect.php';

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $password = $_POST['password'];
        $confirm_password = $_POST['confirm_password'];
        $token = $_GET['token'];

        if ($password !== $confirm_password) {
            $error = "Passwords do not match!";
        } else {
            // Hash the password
            $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

            // Example: lookup user via token (you’d need a password_reset table with tokens)
            $sql = "UPDATE users SET password=? WHERE email=(SELECT email FROM password_resets WHERE token=?)";
            $stmt = $conn->prepare($sql);
            $stmt->bind_param("ss", $hashedPassword, $token);

            if ($stmt->execute()) {
                $success = "Password has been reset successfully.";
            } else {
                $error = "Something went wrong, try again.";
            }
        }
    }

?>


<!DOCTYPE html>

    <html>

        <head>

            <title>Reset Password - wassup?</title>

            <style>

                body {
                    background: rgb(182, 240, 255);
                }
                .padding {
                    padding: 20px;
                    border: none;
                    width: 40vw;
                    height: 50vh;
                    border-radius: 30px;
                    box-shadow: 0px 0px 30px 0px rgba(0,0,0,0.1);
                    display: grid;
                    justify-content: center;
                    align-items: center;
                    margin: 0 auto;
                    background: white;
                }
                .paddingAlign {
                    margin-top: 100px;
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
                }
                button:hover {
                    background-color: rgb(120, 190, 255);
                }
                a {
                    color: black;
                    text-decoration: none;
                    font-size: 14px;
                    text-align: center;
                    display: block;
                    margin-top: 10px;
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

                <?php if (!empty($error)): ?>
                    <div class="padding">
                        <div class="error"><?php echo $error; ?></div>
                        <a href="forgot_password.php">Try again</a>
                    </div>
                <?php elseif (!empty($success)): ?>
                    <div class="padding">
                        <div class="success"><?php echo $success; ?></div>
                    </div>
                <?php else: ?>
                    <form class="padding" method="POST" action="/halla/reset.php?token=<?php echo htmlspecialchars($token); ?>">
                        <h2 style="text-align: center;">Reset Password</h2>
                        
                        <input type="password" name="password" placeholder="New Password:" required> <br>

                        <input type="password" name="confirm_password" placeholder="Confirm New Password:" required> <br>

                        <button type="submit">Reset Password</button>
                    </form>
                <?php endif; ?>

            </div>

        </body>

    </html>