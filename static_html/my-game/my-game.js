function GetButtonValue(clicked_id) {
    var choice_user = document.getElementById(clicked_id).value;

    var choice_computer = Math.random();
    
    if (choice_computer < 0.2) {
	   choice_computer = "Rock";
    } else if (choice_computer >= 0.2 && choice_computer < 0.4) {
	   choice_computer = "Paper";
    } else if (choice_computer >= 0.4 && choice_computer < 0.6) {
	   choice_computer = "Scissors";
    } else if (choice_computer >= 0.6 && choice_computer < 0.8) {
	   choice_computer = "Lizard";
    } else {
	   choice_computer = "Spock";
    } 
    
    document.getElementById("user-choice").innerHTML = '<b>You have chosen: </b>' + choice_user;
    document.getElementById("computer-choice").innerHTML = '<b>Computer has chosen: </b>' + choice_computer;
    
    var compare = function (choice1, choice2) {
	   if (choice1 === choice2) {
           return "The result is a tie!";
       } 
        
       else if (choice1 == "Rock") {
       
        if (choice2 == "Scissors") {
			return "Rock crushes scissors. You won!";
		} else if (choice2 == "paper") {
			return "Paper covers rock. Computer won!";
		} else if (choice2 == "lizard") {
			return "Rock crushes lizard. You won!";
		} else {
			return "Spock vaporizes rock. Computer won!";
		}
        }
        
        else if (choice1 == "Paper") {
            
		if (choice2 == "Rock") {
			return "Paper covers rock. You won!";
		} else if (choice2 == "Scissors") {
			return "Scissors cuts paper. Computer won!";
		} else if (choice2 == "Lizard") {
			return "Lizard eats paper. Computer won!";
		} else {
			return "Paper disproves Spock. You won!";
		}
        } 
       
        else if (choice1 == "Scissors") {
		if (choice2 == "Rock") {
			return "Rock crushes scissors. Computer won!";
		} else if (choice2 == "Paper") {
			return "Scissors cuts paper. You won!";
		} else if (choice2 == "Lizard") {
			return "Scissors decapitates lizard. You won!";
		} else {
			return "Spock smashes scissors. Computer won!";
		}          
	} 
        
        else if (choice1 == "Lizard") {
		if (choice2 == "Rock") {
			return "Rock crushes lizard. Computer won!";
		} else if (choice2 == "Paper") {
			return "Lizard eats paper. You won!";
		} else if (choice2 == "Scissors") {
			return "Scissors decapitates lizard. Computer won!";
		} else {
			return "Lizard poisons Spock. You won!";
		}
	}
        
        else if (choice1 == "Spock") {
		if (choice2 == "Rock") {
			return "Spock vaporizes rock. You won!";
		} else if (choice2 == "Paper") {
			return "Paper disproves Spock. Computer won!";
		} else if (choice2 == "Scissors") {
			return "Spock smashes scissors. You won!";
		} else {
			return "Lizard poisons Spock. Computer won!";
		}
            
		}
}

document.getElementById("game-result").innerHTML = compare (choice_user, choice_computer);  
   
}