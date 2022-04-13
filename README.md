# Questions And Answers Contest

This program provides a system to let players answer questions with multiple difficulties. It allows the use of the base questionaire or add your own custom set of questions (up to 25 questions, 5 per rank). Also stores the performance of each player with the prizes won and best streak.

![Game_Model](https://user-images.githubusercontent.com/96447338/163114327-6cab1a21-61e3-4583-a581-7da2c7c56223.png)

#### Features:
* Play the game.
* View player historical stats.
* Try the game multiple times with the same player ID.

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Author](#author)

## Environment
This program was interpreted/tested on Windows 10 using python3 (3.7.3)

## Installation
* Close this repository: "git clone https://github.com/pabloaguilarv/QuestionsAndAnswersContest"
* Make sure the base contest.db is in models. "cd models".
* In the main folder where start.py is located, run "python3 start.py".

## File Descriptions
[start.py](start.py) - Is the main file for the entire program. Once running, in-game options will guide the player.

#### `models/` directory contains classes used for this project as well as the databasases:
[base_model.py](/models/base_model.py) - The base model class from which future classes inherit.
`def __init__(self,name)` - Initializes base model.
* All the other methods execute regular sql-related functions.

Classes inherited from Base Model:
* [players.py](/models/players.py)
* [questions.py](/models/questions.py)
* [options.py](/models/options.py)

[basedbcreation.py](basedbcreation.py) - Is a file that is executed inside the main of the [start.py](start.py) file and takes on the tast of reading the [questions.txt](questions.txt) file to fill the [contest.db](contest.db) database that is used for the game.

[questions.txt](questions.txt) - Contains the questions and options for the game.
The format needed for the questions is to have the statement and the category of that questions separated by a comma.
Statement(be careful to avoid commas in this statement),category(integer from 1 to 5).
#### Example:
"How many hours are in a day",1

Options have the same format and all four of them should be right below the questions they belong to, one under the other.
If the option is not the correct one, should be followed by a zero(0), if it is the correct one, must be followed by a one(1) after the comma.
option(be careful to avoid commas in this text),is_correct.

#### Example:
* 24,1
* 15,0
* 48,0
* 10,0

## Examples of use
```
>python3 start.py
Welcome to the Contest
Select one.

1: Start game.        
2: Check player stats.
3. Exit.
Option: 1
Start game.     

1: New Player.  
2: I have an ID.
3: Exit.        
Option: 1

Enter your name: Paul
Please, save your ID to check your stats later: 2

Hello Paul.

These are the prizes that you can get:

Rank 1: $ 100 USD
Rank 2: $ 200 USD
Rank 3: $ 400 USD
Rank 4: $ 800 USD
Rank 5: $ 1,600 USD

Starting Round 1...

Round 1
For $ 100 USD

According to a popular saying if you feel something deeply you feel it "from the bottom of your" what?
A: Heart
B: Stomach
C: Bottom
D: Shoes

Enter your answer (Enter E to exit with current prize): 
```
## Bugs
There are no know bugs at the moment.

## Author

- [GitHub - Pablo Aguilar](https://github.com/pabloaguilarv)
