var TotalPlayTime = 0
var TotalWinTime = 0

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

  var compare = function(choice1, choice2) {
    TotalPlayTime++;

    if (choice1 === choice2) {
      return "The result is a tie!";
    } else if (choice1 == "Rock") {

      if (choice2 == "Scissors") {
        ++TotalWinTime;
        return "Rock crushes scissors. You won!";
      } else if (choice2 == "paper") {
        return "Paper covers rock. Computer won!";
      } else if (choice2 == "lizard") {
        ++TotalWinTime;
        return "Rock crushes lizard. You won!";
      } else {
        return "Spock vaporizes rock. Computer won!";
      }

    } else if (choice1 == "Paper") {

      if (choice2 == "Rock") {
        ++TotalWinTime;
        return "Paper covers rock. You won!";
      } else if (choice2 == "Scissors") {
        return "Scissors cuts paper. Computer won!";
      } else if (choice2 == "Lizard") {
        return "Lizard eats paper. Computer won!";
      } else {
        ++TotalWinTime;
        return "Paper disproves Spock. You won!";
      }
    } else if (choice1 == "Scissors") {
      if (choice2 == "Rock") {
        return "Rock crushes scissors. Computer won!";
      } else if (choice2 == "Paper") {
        ++TotalWinTime;
        return "Scissors cuts paper. You won!";
      } else if (choice2 == "Lizard") {
        ++TotalWinTime;
        return "Scissors decapitates lizard. You won!";
      } else {
        return "Spock smashes scissors. Computer won!";
      }
    } else if (choice1 == "Lizard") {
      if (choice2 == "Rock") {
        return "Rock crushes lizard. Computer won!";
      } else if (choice2 == "Paper") {
        ++TotalWinTime;
        return "Lizard eats paper. You won!";
      } else if (choice2 == "Scissors") {
        return "Scissors decapitates lizard. Computer won!";
      } else {
        ++TotalWinTime;
        return "Lizard poisons Spock. You won!";
      }
    } else if (choice1 == "Spock") {
      if (choice2 == "Rock") {
        ++TotalWinTime;
        return "Spock vaporizes rock. You won!";
      } else if (choice2 == "Paper") {
        return "Paper disproves Spock. Computer won!";
      } else if (choice2 == "Scissors") {
        ++TotalWinTime;
        return "Spock smashes scissors. You won!";
      } else {
        return "Lizard poisons Spock. Computer won!";
      }

    }

  }

  document.getElementById("game-result").innerHTML = compare(choice_user, choice_computer);
  document.getElementById("playtime").innerHTML = TotalPlayTime;
  document.getElementById("wintime").innerHTML = TotalWinTime;
}

$(document).ready( function() {
"use strict";

$("#submit_score").click(function() {
  var msg = {
    "messageType": "SCORE",
    "score": parseInt($("#wintime").text())
  };
  window.parent.postMessage(msg, "*");
});


$("#save").click(function() {
  var msg = {
    "messageType": "SAVE",
    "gameState": {
      "playtime": parseInt($("#playtime").text()),
      "wintime": parseInt($("#wintime").text())
    }
  };
  window.parent.postMessage(msg, "*");
});

// Sends a request to the service for a
// state to be sent, if there is one.
$("#load").click(function() {
  var msg = {
    "messageType": "LOAD_REQUEST",
  };
  window.parent.postMessage(msg, "*");
});

// Listen incoming messages, if the messageType
// is LOAD then the game state will be loaded.
// Note that no checking is done, whether the
// gameState in the incoming message contains
// correct information.
//
// Also handles any errors that the service
// wants to send (displays them as an alert).
var playtime=0;
var wintime=0;
window.addEventListener("message", function(evt) {
  if (evt.data.messageType === "LOAD") {
    playtime = evt.data.gameState.playtime;
    wintime = evt.data.gameState.wintime;
    $("#wintime").text(wintime);
    $("#playtime").text(playtime);
  } else if (evt.data.messageType === "ERROR") {
    alert(evt.data.info);
  }
});

var message = {
  messageType: "SETTING",
  options: {
    "width": 700, //Integer
    "height": 400 //Integer
  }
}
window.parent.postMessage(message, "*");
}
);
