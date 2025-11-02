<!DOCTYPE html>

	<html>
	
		<head>
		
			<title>dis-encrypt</title>
			
			<link rel="stylesheet" type="text/css" href="encrypt.css">
			
		</head>
		
		
		<body>
		
			
		
			<h1>Dis-Un-Encrypt a text</h1>
			
			<div class="startBtns">

				<form method="post" action="encrypt.php">

					<button name="action" value="Encrypt" type="submit" id="En">Encrypt</button>

					<button name="action" value="Unencrypt" type="submit" id="Un">Unencrypt</button>

				</form>

			</div>

			<?php
			
				session_start();
				
				// Initialize session arrays if they don't exist
				if (!isset($_SESSION['inputs'])) {
					$_SESSION['inputs'] = array();
				}
				if (!isset($_SESSION['results'])) {
					$_SESSION['results'] = array();
				}
				
				if ($_SERVER['REQUEST_METHOD'] === 'POST') {
					if (isset($_POST['action'])) {
						$action = $_POST['action'];
						
						if ($action == 'Unencrypt') {
							// Handle number input and processing
							if (isset($_POST['add_number'])) {
								// Add number to session
								if (isset($_POST['number']) && is_numeric($_POST['number'])) {
									$_SESSION['inputs'][] = intval($_POST['number']);
								}
							} elseif (isset($_POST['process_numbers'])) {
								// Process all collected numbers
								$letters = array(
									1=>"A", 2=>"B", 3=>"C", 4=>"D", 5=>"E", 6=>"F", 
									7=>"G", 8=>"H", 9=>"I", 10=>"J", 11=>"K", 12=>"L", 
									13=>"M", 14=>"N", 15=>"O", 16=>"P", 17=>"Q", 18=>"R", 
									19=>"S", 20=>"T", 21=>"U", 22=>"V", 23=>"W", 24=>"X", 
									25=>"Y", 26=>"Z"
								);
								
								foreach ($_SESSION['inputs'] as $num) {
									if (isset($letters[$num])) {
										$_SESSION['results'][] = $letters[$num];
									} else {
										$_SESSION['results'][] = "?";
									}
								}
								
								// Clear inputs after processing
								$_SESSION['inputs'] = array();
							}
							
							// Display unencrypt form
							echo '
							<h1>Unencrypt</h1>
							<form method="post">
								<input type="hidden" name="action" value="Unencrypt">
								
								<label>Enter Number (1-26):</label>
								<input name="number" type="number" min="1" max="26" id="number" required>
								
								<div class="subBtn">    
									<button name="add_number" type="submit">Add Number</button>
									<button name="process_numbers" type="submit">Unencrypt!!</button>
								</div>
							</form>';
							
							// Display collected numbers
							if (!empty($_SESSION['inputs'])) {
								echo '<div class="result"><h3>Numbers to process:</h3><p>' . implode(', ', $_SESSION['inputs']) . '</p></div>';
							}
							
							// Display results if any
							if (!empty($_SESSION['results'])) {
								echo '<div class="result"><h3>Unencrypted Text:</h3><p>' . implode('', $_SESSION['results']) . '</p></div>';
								$_SESSION['results'] = array(); // Clear results after display
							}
							
						} elseif ($action == 'Encrypt') {
							// Handle letter input and processing
							if (isset($_POST['add_letter'])) {
								// Add letter to session
								if (isset($_POST['text']) && !empty($_POST['text'])) {
									$_SESSION['inputs'][] = strtoupper(substr(trim($_POST['text']), 0, 1));
								}
							} elseif (isset($_POST['process_letters'])) {
								// Process all collected letters
								$numbers = array(
									"A"=>1, "B"=>2, "C"=>3, "D"=>4, "E"=>5, "F"=>6, 
									"G"=>7, "H"=>8, "I"=>9, "J"=>10, "K"=>11, "L"=>12, 
									"M"=>13, "N"=>14, "O"=>15, "P"=>16, "Q"=>17, "R"=>18, 
									"S"=>19, "T"=>20, "U"=>21, "V"=>22, "W"=>23, "X"=>24, 
									"Y"=>25, "Z"=>26
								);
								
								foreach ($_SESSION['inputs'] as $letter) {
									if (isset($numbers[$letter])) {
										$_SESSION['results'][] = $numbers[$letter];
									} else {
										$_SESSION['results'][] = 0;
									}
								}
								
								// Clear inputs after processing
								$_SESSION['inputs'] = array();
							}
							
							// Display encrypt form
							echo '
							<h1>Encrypt</h1>
							<form method="post">
								<input type="hidden" name="action" value="Encrypt">
								
								<label>Enter Letter (A-Z):</label>
								<input name="text" type="text" maxlength="1" id="Ltext" required>
								
								<div class="subBtn" align="center">    
									<button name="add_letter" type="submit">Add Letter</button>
									<button name="process_letters" type="submit">Encrypt!!</button>
								</div>
							</form>';
							
							// Display collected letters
							if (!empty($_SESSION['inputs'])) {
								echo '<div class="result"><h3>Letters to process:</h3><p>' . implode(', ', $_SESSION['inputs']) . '</p></div>';
							}
							
							// Display results if any
							if (!empty($_SESSION['results'])) {
								echo '<div class="result"><h3>Encrypted Text:</h3><p>' . implode(' ', $_SESSION['results']) . '</p></div>';
								$_SESSION['results'] = array(); // Clear results after display
							}
						}
					}
				}
				
			?>
			
		</body>
		
	</html>
