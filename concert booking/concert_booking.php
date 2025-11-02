<?php


	// Start the session
	session_start();

	// Initialize ticket counters if they don't exist
	if (!isset($_SESSION['tickets_sold'])) {
		$_SESSION['tickets_sold'] = 0;
	}
	if (!isset($_SESSION['tickets_left'])) {
		$_SESSION['tickets_left'] = 16000; // Total tickets available
	}
	
	
	if (!isset($_SESSION['booked_seats'])) {
    $_SESSION['booked_seats'] = [];
}

	// Function to generate a unique seat number
	function generateUniqueSeatNumber() {
		$min = 1; // Minimum seat number
		$max = 16000; // Maximum seat number

		do {
			$seat_number = rand($min, $max); // Generate a random seat number
		} while (in_array($seat_number, $_SESSION['booked_seats'])); // Ensure it's unique

		return $seat_number;
	}
	

	// Initialize age group counters
	if (!isset($_SESSION['F_age_16_21'])) {
		$_SESSION['F_age_16_21'] = 0;
	}
	if (!isset($_SESSION['F_age_22_35'])) {
		$_SESSION['F_age_22_35'] = 0;
	}
	if (!isset($_SESSION['M_age_16_21'])) {
		$_SESSION['M_age_16_21'] = 0;
	}
	if (!isset($_SESSION['M_age_22_35'])) {
		$_SESSION['M_age_22_35'] = 0;
	}

	// Process form submission
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$gender = $_POST['gender'];
		$age = $_POST['age'];
		$ticket = $_POST['ticket'];

		if ($age >= 16 && $age <= 35) {
			if ($_SESSION['tickets_left'] > 0) {
				// Increment tickets sold and decrement tickets left
				$_SESSION['tickets_sold']++;
				$_SESSION['tickets_left']--;

				// Update age group counters
				if ($gender == "Female") {
					if ($age >= 16 && $age <= 21) {
						$_SESSION['F_age_16_21']++;
					} else if ($age >= 22 && $age <= 35) {
						$_SESSION['F_age_22_35']++;
					}
				} else if ($gender == "Male") {
					if ($age >= 16 && $age <= 21) {
						$_SESSION['M_age_16_21']++;
					} else if ($age >= 22 && $age <= 35) {
						$_SESSION['M_age_22_35']++;
					}
				}
			} else {
				$error_message = '<div style="margin-left: 70px; margin-top: 10px; font-size: 25px; color: red;"> <b style="font-size: 19px; color: red;"> Ticket not available! </b><br> No tickets left. </div>';
			}
		} else {
			$error_message = '<div style="margin-left: 70px; margin-top: 10px; font-size: 25px; color: red;"> <b style="font-size: 19px; color: red;"> Ticket not available! </b><br> You are not eligible to attend the concert. </div>';
		}
	}
	?>


<!DOCTYPE html>

    <html>

        <head>

            <title>
                Booking page Beyonce
            </title>

            <link rel="stylesheet" type="text/css" href="concert.css">

        </head>

        <body>

            <h1 align="center">Beyonce concert booking</h1>

            <h2>Price List</h2>
			
			<ol>
                <li>VVIP: R3000.00</li>
                <li>VIP: R2000.00</li>
                <li>General : R500.00</li>
			</ol>

            <div align="center" class="form">

                <form action="" method="POST">

                    <label for="gender">Gender:</label> 
                        <select style="background-color: rgb(80, 80, 80); color: white;" id="gender" name="gender">
							<option value="Female">Female</option>
							<option value="Male">Male</option>
						</select> <br>

                    <label for="age">Age:</label>
                        <input style="background-color: rgb(80, 80, 80); color: white;" class="age" name="age" id="age" type="number" placeholder="16+" required> <br>

                    <label for="ticket">Ticket:</label>
						<select style="background-color: rgb(80, 80, 80); color: white;" id="ticket" name="ticket">
							<option value="VVIP">VVIP</option>
							<option value="VIP">VIP</option>
							<option value="General Admission">General Admission</option>
						</select> <br>
						
					<input  style="background-color: rgb(80, 80, 80); color: white;" class="subBtn" type="submit" value="Book a seat">

                </form>

            </div>
			
			<div class="table-container">
			
				<table class="table">
				
					<tr>
						<th>Ticket Buyers</th>
						<th>Age group</th>
						<th>Tickets sold</th>
					</tr>
					
					<tr>
						<td>Female</td>
						<td>16-21</td>
						<td>
							<?php
								echo $_SESSION['F_age_16_21'];
							?>
						</td>
					</tr>
					
					<tr>
						<td>Female</td>
						<td>22-35</td>
						<td>
							<?php
								 echo $_SESSION['F_age_22_35'];
							?>
						</td>
					</tr>
					
					<tr>
						<td>Male</td>
						<td>16-21</td>
						<td>
							<?php
								echo $_SESSION['M_age_16_21'];
							?>
						</td>
					</tr>
					
					<tr>
						<td>Male</td>
						<td>22-35</td>
						<td>
							<?php
								echo $_SESSION['M_age_22_35'];
							?>
						</td>
					</tr>
					
					<tr>
						<th>Tickets Available</th>
						<th>Tickets Left</th>
						
					<tr>
					
					<tr>
						<td>16000</td>
						<td> 
							<?php
								echo $_SESSION['tickets_left']; 
							?>
						</td>
						<td colspan="2">HURRY UP!!</td>
					</tr>
				
				</table>
				
				
				<div class="ticket">
				
					<?php
					
						if ($_SERVER["REQUEST_METHOD"] == "POST") {
							$gender = $_POST['gender'];
							$age = $_POST['age'];
							$ticket = $_POST['ticket'];
							
								if ($age >= 18 && $age <= 35) {	
								
									if ($_SESSION['tickets_left'] > 0) {
										$seat_number = generateUniqueSeatNumber();
										$_SESSION['booked_seats'][] = $seat_number;
											
											echo '<div style="margin-left: 20px; color: white;">';
												echo '<div style="font-family: Brush Script MT; font-size: 28px; margin-top: -15px;" align="center"> BEYONCE LIVE CONCERT </div>';
												echo "Seat Booked ______ Seat Number: $seat_number <br>"; 
												echo "Gender: " . htmlspecialchars($gender) . "<br>";
												echo "Age: " . htmlspecialchars($age) . "<br>";
												echo "Ticket type: " . htmlspecialchars($ticket) . "<br>";
												echo '<div style="font-size: 11px; margin-left: 130px; margin-top: 17px;" align="right"> Date: 25th December 2025 ___ Venue: FNB Staduim </div>';
											} else if ($age >= 35) {
												echo '<div style="margin-left: 70px; margin-top: 10px; font-size: 25px; color: red;"> <b style="font-size: 19px; color: red;"> Ticket not available! </b><br> You are old to attend the concert. </div>';

											} else {
												echo '<div style="margin-left: 70px; margin-top: 10px; font-size: 25px; color: red;"> <b style="font-size: 19px; color: red;"> Ticket not available! </b><br> You are young to attend the concert. </div>';
											}
										echo '</div>';
								} else {
									echo "Ticket not booked";
								}
						}
						
					?>
				
				</div>
				
			</div>
			
			<div align="right" >
				<button class="downloadBtn"><b>Download Ticket</b></button>
			</div>
				
        </body>

    </html>
