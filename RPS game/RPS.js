//remove
// Event listener for the submit button click
document.getElementById('submitBtn').onclick = function() {
    // Get the selected game value
    var rating = document.querySelector('input[name="game"]:checked');
    
    // Get the element to display the result
    var resultDiv = document.getElementById('game-result');
    
    // Check if a weapon is selected
    if (rating) {
    // Get the computer's choice
    var choices = ['Rock', 'Paper', 'Scissor'];
    var compChoice = choices[Math.floor(Math.random() * choices.length)];
    
    // Display the selected weapon and the computer's choice
    resultDiv.innerText = "You chose: " + rating.value + ". Computer chose: " + compChoice + ".";
    
    // Determine the winner
    if (compChoice == "Rock" && rating.value == "Scissor") {
        resultDiv.innerText += " Rock beats Scissors, you lost.";
    } else if (compChoice == "Paper" && rating.value == "Rock") {
        resultDiv.innerText += " Paper beats Rock, you lost.";
    } else if (compChoice == "Scissor" && rating.value == "Paper") {
        resultDiv.innerText += " Scissor beats Paper, you lost.";
    } else if (compChoice == rating.value) {
        resultDiv.innerText += " It's a tie!";
    } else {
        resultDiv.innerText += " You win!";
    }
    } else {
    // Ask the user to select a weapon
    resultDiv.innerText = "Please select a weapon before fighting.";
    }
};
