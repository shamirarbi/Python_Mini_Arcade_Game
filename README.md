# Mini Arcade Game

A simple terminal-based arcade written in Python. It has three games in one file, a main menu, and a scoreboard that tracks your points across all games while you play.

Built as a beginner-friendly Python project.

## Games

1. **Guess the Number**
   Guess a number between 1 and 100. You have 5 tries, and the faster you guess it, the more points you get.
2. **Quiz**
   Answer 5 multiple-choice questions about science. Each correct answer gives you 1 point.
3. **Rock Paper Scissors**
   Play 3 rounds against the computer. Whoever wins the most rounds wins the match.

## Scoring System
--------------------------------------------------------------------------------------------------------
| Game                |                              How points work                                   |
|---------------------|--------------------------------------------------------------------------------|
| Guess the Number    | 1st guess = 5 points, 2nd = 4, 3rd = 3, 4th = 2, 5th = 1, no correct guess = 0 |
--------------------------------------------------------------------------------------------------------
| Quiz                | 1 point per correct answer (5 points if all answers are correct)               |
--------------------------------------------------------------------------------------------------------
| Rock Paper Scissors | Win the match = 3 points. Otherwise, 1 point for each round you won            |
--------------------------------------------------------------------------------------------------------

Your points are added up across all games, and you can check them anytime from the menu.

## Features

- Main menu to pick any game
- Score tracking for every game (points and number of times played)
- Total score across all games
- View the scoreboard anytime
- Scoreboard and a goodbye message when you exit
- Score tracking uses Python lists

## Requirements

- Python 3.6 or higher (no extra libraries needed)

## How to Run

```bash
git clone https://github.com/shamirarbi/Python_Mini_Arcade_Game.git
cd Python_Mini_Arcade_Game
python game_arcade.py
```

On some systems you may need to use `python3` instead of `python`.

## Menu Preview

```
========================================
      WELCOME TO THE MINI GAME ARCADE
========================================

------MAIN MENU------
1) Guess the Number
2) Quiz
3) Rock Paper Scissors
4) View Scoreboard
5) Exit
Choose an option (1-5):
```

## Scoreboard Preview

```
========================================
           SCOREBOARD
========================================
Guess the Number       | Played: 1   | Points: 4
Quiz                   | Played: 1   | Points: 5
Rock Paper Scissors    | Played: 1   | Points: 3
----------------------------------------
TOTAL SCORE            | 12
========================================
```

## Notes

- Scores are saved in memory only, so they reset when you close the program.

## Future Improvements

- Save scores to a file so they stay after closing the program
- Add more games
- Add more quiz questions with random order
- Add difficulty levels

## Author

Made by [Shamir Ahamed](https://github.com/shamirarbi)
