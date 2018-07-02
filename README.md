
+ Test user: **Cat**
+ Test password: **wsd-2017**

# Final Submission

[Deployed APP](https://worldgames-wsd2017.herokuapp.com/)

[Report](https://drive.google.com/open?id=1VUERj33z7eaX_HVXa6Dh7DA7rW1EZiVF)

[Instructions](https://drive.google.com/open?id=1fhTekJNsxGmXevj2QGrPEy8jQ_bWnvMT)


# Project Plan

1.Team

* **599773 Elena Kazakova**. Responsible for: the frontend functionality of the project. Developing skills in: Django and back-end coding in general.

* **604969 Wenbin Luo**. Responsible for: the backend functionality. Developing skills in: Django and JavaScript. 

* **605324 Yiming Yang**. Responsible for: full stack functionality, the model design. Developing skills in: JavaScript and Django

2.Goal

Our goal is to develop an online game store for JavaScript games in short term and deliver it in good quality. The outcome of this project is a online game selling and playing site with many functionalities for gamer and game developers, responsive interactions and reliable security protection.

To accomplish these goals, we would use bootstrap, Django framework and many other developing tools. We hope we would grasp the practical skills for web development through this project.

3.Plans

<table>
  <tr>
    <td>Implemented feature</td>
    <td>Implementation</td>
  </tr>
  <tr>
    <td>Authentication </td>
    <td></td>
  </tr>
  <tr>
    <td>Login, logout and register (both as player or developer) with email validation</td>
    <td>Using the authentication from Django
Implementing extra authentication features using Django Email and Django bcrypt.
</td>
  </tr>
  <tr>
    <td>Basic player functionalities </td>
    <td></td>
  </tr>
  <tr>
    <td>Buying games
Playing games
Finding games
Security restrictions</td>
    <td>Creating the Gamer's model (based on Django user) and database to store the information.
Implementing the game message communication to save the gameplay data of the player.  
Adding basic search function to find games.
For buying games, we will follow the instruction from Simple Payments.</td>
  </tr>
  <tr>
    <td>Basic developer functionalities</td>
    <td></td>
  </tr>
  <tr>
    <td>Adding a game
Setting price for a game
Managing a game
Statistics dashboard for a developer
Security restrictions</td>
    <td>Creating the Gamer’s and Game’s model (based on Django user) and database.
Using Django to modify models of our website. Further works including view design, UI design and model write.
For security issues, we would do research and then implement the methods for payment and authorization securities. </td>
  </tr>
  <tr>
    <td>Game/service interaction</td>
    <td></td>
  </tr>
  <tr>
    <td>Managing player’s scores

 </td>
    <td>Using postMessage to make communication.
Checking methods for sending messages from service to the game.</td>
  </tr>
  <tr>
    <td>Mobile Friendly - Extra feature</td>
    <td></td>
  </tr>
  <tr>
    <td>Responsive web design</td>
    <td>For creating responsive web design, we will use Bootstrap 4, which will be improved by some CSS media queries, as there are several serious bugs in this toolkit that can spoil user experience. 
Using jQuery to create the responsivity of the website. </td>
  </tr>
  <tr>
    <td>Social media sharing - Extra feature</td>
    <td></td>
  </tr>
  <tr>
    <td>Enable sharing games in some social media site (Facebook)</td>
    <td>Implementing the sharing on social media feature after self-learning. Useful link: Sharing on social links</td>
  </tr>
</table>


Table 1

Other features from the "More features" sections will be implemented if we will have enough time.

    1. Diagram and Wireframes

#### **Use case diagram**

Our use case diagram that represents our functional requirements to the service can be found [here](https://drive.google.com/open?id=1Zlm3Sf8P0dzOpfMQL8lAzdKGahok032q). 

#### **Initial Django Models**

Initial Django models are presented in Table 2. Fields that have (*) are unique.

<table>
  <tr>
    <td>Model's field</td>
    <td>Field’s description</td>
  </tr>
  <tr>
    <td>Gamer’s model - customized from Django user model, information about a gamer (user) including personal details, purchasing and game playing history</td>
    <td></td>
  </tr>
  <tr>
    <td>username*</td>
    <td>The username field is a login that is also used as a unique id of a user</td>
  </tr>
  <tr>
    <td>password</td>
    <td>the password for login, processed with bcrypt by Django</td>
  </tr>
  <tr>
    <td>email*</td>
    <td>email of a user that can also be used to login, must have a unique id</td>
  </tr>
  <tr>
    <td>full name</td>
    <td>real name of a user</td>
  </tr>
  <tr>
    <td>purchasing history</td>
    <td>a list of purchased games’ ids linked to the Purchase model</td>
  </tr>
  <tr>
    <td>gameplay history </td>
    <td>a list of gameplays’ ids linked to the Gameplay model</td>
  </tr>
  <tr>
    <td>short description</td>
    <td>additional information about a user</td>
  </tr>
  <tr>
    <td>last login time</td>
    <td>the last time when this user was online</td>
  </tr>
  <tr>
    <td>Developer’s model - this model is customized from Django user model. It has many similar fields with gamer’s model</td>
    <td></td>
  </tr>
  <tr>
    <td>username*</td>
    <td>The username field is a login that is also used as a unique id of a user</td>
  </tr>
  <tr>
    <td>password</td>
    <td>the password for login, processed with bcrypt by Django</td>
  </tr>
  <tr>
    <td>email*</td>
    <td>email of a user that can also be used to login, must have a unique id</td>
  </tr>
  <tr>
    <td>full name</td>
    <td>real name of a user</td>
  </tr>
  <tr>
    <td>rating</td>
    <td>rating given by players to this developer (calculated as the average of all ratings)</td>
  </tr>
  <tr>
    <td>games</td>
    <td>a list of games’ id developed by a developer linked to the Game model</td>
  </tr>
  <tr>
    <td>short description</td>
    <td>additional information about a developer</td>
  </tr>
  <tr>
    <td>last login time</td>
    <td>the last time when this user was online</td>
  </tr>
  <tr>
    <td>Game’s model </td>
    <td></td>
  </tr>
  <tr>
    <td>id*</td>
    <td>a unique id of the game (a number)  </td>
  </tr>
  <tr>
    <td>name</td>
    <td>name of the game</td>
  </tr>
  <tr>
    <td>game’s description</td>
    <td>description given by a developer</td>
  </tr>
  <tr>
    <td>price</td>
    <td>original game’s price, without any discounts</td>
  </tr>
  <tr>
    <td>developer’s username</td>
    <td>the developer’s username of this game linked to Developer’s model. May contain multiple values</td>
  </tr>
  <tr>
    <td>game’s url</td>
    <td>the url to the Javascript file of the game</td>
  </tr>
  <tr>
    <td>purchased by </td>
    <td>the list of gamers’ usernames who purchased this game. Connected to the Purchase model</td>
  </tr>
  <tr>
    <td>highest score</td>
    <td>contains the highest score found among gamers who purchased this game</td>
  </tr>
  <tr>
    <td>rating</td>
    <td>rating given by gamers to this game (calculated as the average of all ratings)</td>
  </tr>
  <tr>
    <td>Purchase model - a record of each purchase, a connection between a gamer and a game</td>
    <td></td>
  </tr>
  <tr>
    <td>id*</td>
    <td>a unique id of this purchase (a number)</td>
  </tr>
  <tr>
    <td>customer</td>
    <td>username of a gamer linked to the Gamer’s model</td>
  </tr>
  <tr>
    <td>game</td>
    <td>purchased game’s id linked to the Game’s model</td>
  </tr>
  <tr>
    <td>price</td>
    <td>the final price after discount, part of this price is given to developer as a profit</td>
  </tr>
  <tr>
    <td>time</td>
    <td>time of purchasing</td>
  </tr>
  <tr>
    <td>Gameplay’s model - a record of a gamer playing a game updated each time when the player saves his/her status in a game</td>
    <td></td>
  </tr>
  <tr>
    <td>id*</td>
    <td>a unique id of this gameplay (a number)</td>
  </tr>
  <tr>
    <td>update time</td>
    <td>the time of the gameplay record’s update </td>
  </tr>
  <tr>
    <td>game</td>
    <td>game’s id linked to the Game’s model</td>
  </tr>
  <tr>
    <td>gamer</td>
    <td>gamer’s username. Connected to the Gamer’s model</td>
  </tr>
  <tr>
    <td>game’s status</td>
    <td>the status of a gameplay that covers everything. It can be saved or loaded by a player when he launches a game. Should be in Json type</td>
  </tr>
  <tr>
    <td>settings</td>
    <td>some options of the game, mainly used to adjust the layout </td>
  </tr>
  <tr>
    <td>current score</td>
    <td>current score of a gamer</td>
  </tr>
</table>


Table 2

    2. Priorities

We will prioritize the following things for the **back-end coding**:

* Functionality with minimum requirement

* Good quality of the code

* Reusability of Django methods and structures

As to the **front-end coding**, we want:

* Create minimalistic, but appealing design for our service

* Achieve a good level of usability and user experience of our service, so our future users can work with it easily

* Create a responsive design for the website, as, currently, responsive design is very important for the web products to be competitive in the market and, likewise, it increases the level of product usability. 

We likewise have one **general priority** for our project:

* Deliver clear documentation for the service

* Write well-commented and readable code. 

4.Process and Time Schedule

We have decided to work collaboratively both online and offline. We think that it is important to meet weekly in person to control the working progress of each member of our group. However, we understand that sometimes we will, probably, have difficulties with it and in this situation, we are going to organize Skype meetings. For staying in touch constantly, we use Telegram messenger. 

For making the process of dividing and assigning tasks more simple, we will use [Trello](https://trello.com/). Trello will allow us to organize the project work better, as it increases the transparency of working process: it will be easy to see what each member of the group is currently doing.

For working together on our documentation, we use Google Drive. After our documentation will be finished, we will convert it to .md format using converters (e.g., [Word to Markdown converter](https://word-to-markdown.herokuapp.com/)). For the diagrams and schemes we will use [draw.io](https://www.draw.io/).  

We are planning to work on the assigned tasks mostly individually. However, as some of our group members does not have enough experience in back-end coding, we will organize some pair coding sessions. 

Our initial **Time Schedule** is presented in the Table 3. 

<table>
  <tr>
    <td>Week</td>
    <td>Activities</td>
  </tr>
  <tr>
    <td>Week 0
11.12 - 17.12</td>
    <td>Discussing the working process
Specifying the project's requirements
Developing initial Django models
Writing the project plan</td>
  </tr>
  <tr>
    <td>Week 1 - Week 2
18.12 - 31.12</td>
    <td>Drawing initial wireframes
Creating the design for our service and developing responsive HTML templates for the website and writing CSS styles</td>
  </tr>
  <tr>
    <td>Week 3
1.01 - 7.01</td>
    <td>First pair coding session
Implementing initial functionality: meet the minimum functional requirements. (register as player or gamer, add game, etc.)
First project deployment</td>
  </tr>
  <tr>
    <td>Week 4
8.01 - 14.01</td>
    <td>Second pair coding session
Implementing other developer’s and gamer’s functionalities based on the design model</td>
  </tr>
  <tr>
    <td>Week 5
15.01 - 21.01</td>
    <td>Third pair coding session
Implementing purchase and gameplay models</td>
  </tr>
  <tr>
    <td>Week 6
22.01 - 28.01</td>
    <td>Fourth pair coding session
Continuing unfinished jobs
Implementing the security functionality (Authentication & payment security)</td>
  </tr>
  <tr>
    <td>Week 7
29.01 - 4.02</td>
    <td>Finishing the security functionality
Starting to add extra features</td>
  </tr>
  <tr>
    <td>Week 8
5.02 - 11.02</td>
    <td>Finishing the mandatory functional requirement part 
Continuing adding extra features
Checking the quality of code</td>
  </tr>
  <tr>
    <td>Week 9
12.01 - 19.02</td>
    <td>Final testing of the service (including usability testing), removing the imperfections and polishing the final version
Finishing the project’s documentation
Writing the final report</td>
  </tr>
</table>


5.Testing

We are planning to test both front-end and back-end functionality of our service. 

The back-end testing will be done with the following activities: 

* The basic code validation will be done using Brackets validator. 

* The security testing will be done mostly manually. We are planning to develop several scenarios based on most common security problems that can be found in the Web (at this step we are definitely going to check [these](https://www.toptal.com/security/10-most-common-web-security-vulnerabilities) problems). However, we are, likewise, interested in trying some testing software, e.g. [SoapUI](https://www.soapui.org/security-testing/getting-started.html) as it is new for us and interesting to learn.  

* For crash and "idiot proof" testing we will write scenarios as well and then perform them to check if everything works correctly. We are planning to implement the principles of defensive design and programming to avoid problems in this area.

The front-end testing will be conducted with the use of the following procedures:

* Static HTML and CSS pages will be tested by the code validator, which is implemented in [Brackets](http://brackets.io/) editor. However, after these pages will be implemented to the project we will test them once again with [the W3C Markup Validation Service](https://validator.w3.org/). 

* Responsive design will be tested for imperfections manually during its implementation.   

Likewise, we find it important to test the service in general. To do this, we will create scenarios based on our current use case diagram and walk through the service to see if our users can meet any difficulties. Another testing that we want to conduct at the later steps is user testing. We want to organize a classic usability testing with some some real possible users of our service. We will ask them to These types of testing will be conducted at the later steps of our project.

6. Risk Analysis

All of our group members do not have much experience in Django and this is the main risk for our project. To reduce this risk, we plan to do the following things:

* We want to focus on the mandatory features firstly and after that implement additional ones 

* We are going to monitor the status of our project on a weekly basis during our group meetings, so we can notice if something will not go as smoothly as we have planned. In the case, if we will not be able to solve the problem by the group effort, we will ask the course personnel for help.

* We want to leave more time for working on the part of the project connected to Django coding, therefore, we will try to finish all stuff connected to front-end coding already before the New Year. 

* Likewise, to avoid difficulties, we plan to do the first project's deployment as soon as possible (already during the first week of January). We will do Heroku deployments every week for avoiding any unpleasant surprises. 

