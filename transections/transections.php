<!DOCTYPE html>

    <html>

        <head>

            <title>ATM</title>

            <link rel="stylesheet" type="text/css" href="transections.css">

        </head>

        <body>

            <div class="screen">
                <h1>ATM</h1>
                <h2>Start with name and amount before you choose payment method</h2>
                
                <form method="POST" action="">
                    <div class="form-container">
                        <div class="button-group">
                            <button type="submit" name="method" value="Credit_card" class="btn btn1">Credit Card</button>
                            <button type="submit" name="method" value="Crypto_currency" class="btn btn2">Crypto Currency</button>
                            <button type="submit" name="method" value="Pay_Pal" class="btn btn3">Pay Pal</button>
                        </div>
                        
                        <div class="input-group">
                            <input type="text" name="name" id="name" placeholder="Name" required>
                            <input type="number" name="amount" id="amount" placeholder="Amount R0.00" required>
                        </div>
                        
                        <div class="button-group">
                            <button type="submit" name="action" value="refund" class="btn btn4">Refund</button>
                            <button type="submit" name="action" value="history" class="btn btn5">History</button>
                        </div>

                    </div>

                </form>
                
                <div class="output">
                    
                    <?php
                    if ($_SERVER["REQUEST_METHOD"] == "POST") {
                        if (isset($_POST['method'])) {
                            $name = htmlspecialchars($_POST['name'] ?? '');
                            $amount = floatval($_POST['amount'] ?? 0);
                            $method = $_POST['method'];
                            $fee = $amount * 0.1; // 10% fee
                            
                            if ($amount >= 100000) {
                                echo '<div class="warning">WARNING!</div>';
                                echo '<p>Hello ' . $name . '</p>';
                                echo '<p>Fraud detected, you can\'t make payments over R100,000.00</p>';
                            } else {
                                echo '<div class="success">SUCCESS!</div>';
                                echo '<p>Hello ' . $name . '</p>';
                                echo '<p>You deposited R' . number_format($amount, 2) . '</p>';
                                echo '<p>Fee deducted R' . number_format($fee, 2) . '</p>';
                                echo '<p>Using ' . htmlspecialchars($method) . '</p>';
                            }
                        } elseif (isset($_POST['action'])) {
                            $action = $_POST['action'];
                            if ($action == 'refund') {
                                echo '<div class="warning">REFUND PROCESS</div>';
                                echo '<p>Please contact customer service for refunds</p>';
                            } elseif ($action == 'history') {
                                echo '<div class="success">TRANSACTION HISTORY</div>';
                                echo '<p>No recent transactions found</p>';
                            }
                        } else {
                            echo '<div class="warning">No payment method selected</div>';
                        }
                    } else {
                        echo '<div class="warning">WARNING!</div>';
                        echo '<p>No transaction data detected</p>';
                        echo '<p>Avoid fraudulent activities</p>';
                    }

                    ?>

                </div>

            </div>

        </body>

    </html>
