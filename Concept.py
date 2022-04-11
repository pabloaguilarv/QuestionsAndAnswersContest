'''
For this challenge, we want to create a Who Wants to Be a Millionaire-like program.
According to the specifications, there must be:

- 5 ranks each with 5 questions, the higher the rank, the harder the questions. I will take this questions from sources around the internet that have questions from WW2BAM.
- As everyone knows, the questions have 4 options of which only one is correct.
- Game starts from rank 1 for round 1 and it will randomly select 1 question from the base bank.
- Prizes are awarded when questions are answered correctly. A player will get the prize based on the highest rank he managed to achieve.
- Players can end the game voluntarily and its result will be stored on the historical.
- Historical will be updated as well if the player answers incorrectly or finished all the questions.

What we need...:

A main file:
This will contain the backbone of the program.
Will not define any classes, only execute actions.
Consider displaying a timer

FIRST FOCUS ON THE BASE BANK AND THEN WE CAN THINK ABOUT CUSTOMS...

I am thinking if an alternate file should be written to allow the possibility of custom question banks.

Elements of the program:
- Player
- Round
- Rank
- Prize
- Question
- Option

Flow:

Program is initialized
Player is welcomed and prompted to start the game
Player is prompted to enter its name (display a message so the player knows that it will be the name with which results will be stored for future consultation)
Show prize ranks to let player know what they are in to win
Begin round 1
if succesfully answered prompt if player wants to continue
else display the right answer, prize won, rank achieved, display end of game, then exit
Begin round 2 and on and on
'''