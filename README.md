# Python Punchout 🥊

## A command line fighting game

Python Punchout is a fighting game that runs on a command console. Download the files and type .\punchout.py to start the game. A command line window pops up and the game runs in it. Have fun punching!

## Game features and instuctions (also included in the game, accessible via main menu)

- Total of six available characters with weaknesses and strengths
- Three available moves: A punch, kick and a throw
  - Character has 100 points of hp at the start of the battle
  - Each move deals initially 10-40 points of damage damage

**Weakness and strength system:**

- If a move is marked as a character's strength, the move deals initial damage plus 5 damage points
- With weakness move, 5 damage points is reduced from initial damage output

**AI Opponent behaviour:**

- AI chooses its character by random
- It uses its character's strength move 60% of the time, regular move (neither strength or weakness move) 30% and weakness move 10 % of the time

**Main menu commands:**

- H displays this help section
- S Starts the game and propmpts user to choose a fighter
- X Exits the game

**Battle commands:**

- P or p for Punch
- T or t for Throw
- K or k for Kick
- Enter to confirm command

**Game Flow:**

- Each battle contains three rounds
- Round ends when either or both the player and/or AI opponent's HP (hitpoints) reaches zero
- If both the player's and AI Opponent's hp reaches zero at the same time, it is a tie and no winner for the round
- Player with more than zero hp is the winner of the round
- Player who wins more rounds when battle ends is declared the battle winner

## Screenshots

![py-punchout-menu](https://github.com/AnnaJouppi/Python-Punchout/assets/62011685/1c1a76e5-d7bd-4c4b-bf9a-a869e05de3ce)

![fighters-first-round](https://github.com/AnnaJouppi/Python-Punchout/assets/62011685/e4370189-db55-48ce-ae16-674429a6730c)

![punchout-fight](https://github.com/AnnaJouppi/Python-Punchout/assets/62011685/918c043a-5fbd-4afa-a45e-dd0564e13a7b)

