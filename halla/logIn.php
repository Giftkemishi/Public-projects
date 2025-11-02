<?php
    include 'wassup_db.php';

    $error = '';

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $email = trim($_POST['email']);
        $password = $_POST['password'];
        
        if (!empty($email) && !empty($password)) {
            $stmt = $conn->prepare("SELECT id, full_name, email, password FROM users WHERE email = ?");
            $stmt->bind_param("s", $email);
            $stmt->execute();
            $result = $stmt->get_result();
            
            if ($result->num_rows == 1) {
                $user = $result->fetch_assoc();
                
                if (password_verify($password, $user['password'])) {
                    $_SESSION['user_id'] = $user['id'];
                    $_SESSION['full_name'] = $user['full_name'];
                    $_SESSION['email'] = $user['email'];
                    
                    header("Location: /halla/dashboard.php");
                    exit();
                } else {
                    $error = "Invalid email or password.";
                }
            } else {
                $error = "Invalid email or password.";
            }
            
            $stmt->close();
        } else {
            $error = "Please fill in all fields.";
        }
    }
?>

<!DOCTYPE html>

    <html>

        <head>

            <title>Login - wassup?</title>

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

            </style>

        </head>

        <body>

            <h1 class="appName">wassup</h1>

            <div class="paddingAlign">

                <form class="padding" method="POST" action="login.php">

                    <h2 style="text-align: center;">Log in</h2>
                    
                    <?php if (!empty($error)): ?>
                        <div class="error"><?php echo $error; ?></div>
                    <?php endif; ?>
                    
                    <input type="email" name="email" placeholder="Email:" required> <br>
                    
                    <input type="password" name="password" placeholder="Password:" required> <br>

                    <a href="/halla/signIn.php">Create an account</a> <br>

                    <a href="/halla/reset.php">Forgot password?</a> <br>

                    <button type="submit">Log in</button>

                </form>

            </div>

        </body>

    </html>