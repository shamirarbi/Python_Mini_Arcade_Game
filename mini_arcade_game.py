
import random

game_names = ["Guess the Number", "Quiz", "Rock Paper Scissors"]
points_list = [0, 0, 0]
played_list = [0, 0, 0]

GUESS = 0
QUIZ = 1
RPS = 2


def add_score(game_index, points):
    points_list[game_index] += points
    played_list[game_index] += 1
    print(f"\n+{points} point(s) added to {game_names[game_index]}")
    print(f"Total score: {total_score()}")


def total_score():
    return sum(points_list)


def show_scoreboard():
    print("\n" + "=" * 40)
    print("           SCOREBOARD")
    print("=" * 40)
    for i in range(len(game_names)):
        print(f"{game_names[i]:<22} | Played: {played_list[i]:<3} | Points: {points_list[i]}")
    print("-" * 40)
    print(f"{'TOTAL SCORE':<22} | {total_score()}")
    print("=" * 40)


def guess_game():
    comp = random.randint(1, 100)
    guesses = 0
    running = True
    won = False
    max_guesses = 5

    print("\n------GUESS THE NUMBER!!!------")
    print("Select a number between 1 to 100")
    print(f"You have {max_guesses} guesses. Win in 1st guess = 5 points, 2nd = 4, and so on.")

    while running:
        guess = input("Enter your guess: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1

            if guess < 1 or guess > 100:
                print("The number is out of range")
                print("Select a number between 1 to 100")

            elif guess < comp:
                print("Too Low! Try again!")
            elif guess > comp:
                print("Too High! Try again!")
            else:
                print(f"CORRECT! The answer was {comp}")
                print(f"Number of guesses : {guesses}")
                won = True
                running = False

            if running:
                if guesses >= max_guesses:
                    print(f"No guesses left! The answer was {comp}")
                    running = False
                else:
                    print(f"Guesses left: {max_guesses - guesses}")

        else:
            print("Invalid Input!")
            print("Select a number between 1 to 100")

    points = (max_guesses + 1 - guesses) if won else 0
    add_score(GUESS, points)


def quiz_game():
    questions = ("Which planet in our solar system has the most moons as of recent counts?",
                 "What is the most abundant gas in Earth's atmosphere?",
                 "What is the pH of pure water at room temperature?",
                 "Which blood cells are primarily responsible for fighting infection?",
                 "What is the approximate speed of light in a vacuum?")
    options = (("a) Jupiter", "b) Saturn", "c) Uranus", "d) Neptune"),
               ("a) Oxygen", "b) Carbon dioxide", "c) Nitrogen", "d) Argon"),
               ("a) 0", "b) 5", "c) 7", "d) 14"),
               ("a) Red blood cells", "b) White blood cells", "c) Platelets", "d) Plasma cells only"),
               ("a) 300,000 km/s", "b) 30,000 km/s", "c) 3,000,000 km/s", "d) 150,000 km/s"))
    answers = ("b", "c", "c", "b", "a")
    guesses = []
    score = 0
    question_num = 0

    print("\n------QUIZ TIME!------")
    print("1 point for each correct answer (max 5 points)")

    for que in questions:
        print("-"*10)
        print(que)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A,B,C,D): ").lower()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1

    print("*-*-*-*-*-RESULT-*-*-*-*-*")

    print("Answers: ", end="")
    for ans in answers:
        print(ans, end=" ")
    print()
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()
    print()

    points = score  
    score = int(score / len(questions) * 100)
    print(f"Your score is : {score}%")
    add_score(QUIZ, points)


def rps_game():
    options = ("rock", "paper", "scissors")
    total_rounds = 3
    player_wins = 0
    comp_wins = 0

    print("\n------ROCK PAPER SCISSORS------")
    print(f"Best of {total_rounds} rounds. Win the match = 3 points, otherwise you get 1 point per round won.")

    for round_num in range(1, total_rounds + 1):
        print(f"\n--- Round {round_num} of {total_rounds} ---")
        player = None
        comp = random.choice(options)

        while player not in options:
            player = input("Ener a choice (rock, paper, scissors) : ").lower()

        print(f"Player : {player}")
        print(f"Computer: {comp}")

        if player == comp:
            print("It's a Tie!!")
        elif player == "rock" and comp == "scissors":
            print("You Win!!")
            player_wins += 1
        elif player == "paper" and comp == "rock":
            print("You Win!!")
            player_wins += 1
        elif player == "scissors" and comp == "paper":
            print("You Win!!")
            player_wins += 1
        else:
            print("You lose! :'-(")
            comp_wins += 1

        print(f"Score -> You: {player_wins} | Computer: {comp_wins}")

    print("\n*-*-*-*-*-MATCH RESULT-*-*-*-*-*")
    if player_wins > comp_wins:
        print("You won the match!")
        points = 3
    elif player_wins < comp_wins:
        print("Computer won the match!")
        points = player_wins
    else:
        print("The match is a draw!")
        points = player_wins

    add_score(RPS, points)


def main():
    print("=" * 40)
    print("      WELCOME TO THE MINI GAME ARCADE")
    print("=" * 40)

    running = True
    while running:
        print("\n------MAIN MENU------")
        print("1) Guess the Number")
        print("2) Quiz")
        print("3) Rock Paper Scissors")
        print("4) View Scoreboard")
        print("5) Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            guess_game()
        elif choice == "2":
            quiz_game()
        elif choice == "3":
            rps_game()
        elif choice == "4":
            show_scoreboard()
        elif choice == "5":
            running = False
        else:
            print("Invalid choice! Please enter a number from 1 to 5.")

    show_scoreboard()
    print("\nThanks for playing! You did great today.")
    print("Come back soon, the arcade will be waiting for you!")


if __name__ == "__main__":
    main()