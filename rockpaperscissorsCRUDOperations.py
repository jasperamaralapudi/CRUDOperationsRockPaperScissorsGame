import random

class RockPaperScissors:
    def __init__(self):
        self.rounds = []  # stores game rounds
        self.p_score = 0
        self.c_score = 0

    def add_round(self, player_choice, computer_choice, result):
        self.rounds.append({
            "round": len(self.rounds) + 1,
            "player_choice": player_choice,
            "computer_choice": computer_choice,
            "result": result
        })

    def display_rounds(self):
        if not self.rounds:
            print("No rounds played yet.")
            return
        for round in self.rounds:
            print(f"Round {round['round']}: Player - {round['player_choice']}, "
                  f"Computer - {round['computer_choice']}, Result - {round['result']}")

    def display_scores(self):
        print(f"Player Score: {self.p_score}, Computer Score: {self.c_score}")

    def determine_winner(self, player_choice, computer_choice):
        opts = ['Rock', 'Paper', 'Scissors']
        p_ch = opts.index(player_choice) + 1
        
        if (p_ch == 1 and computer_choice == 'Scissors') or \
           (p_ch == 2 and computer_choice == 'Rock') or \
           (p_ch == 3 and computer_choice == 'Paper'):
            return "Player Wins"
        elif player_choice == computer_choice:
            return "Tie"
        else:
            return "Computer Wins"

    def update_round(self, round_number):
        # First, find the round
        round_to_update = None
        for round in self.rounds:
            if round['round'] == round_number:
                round_to_update = round
                break
        
        if not round_to_update:
            print("Round not found.")
            return

        # Store old result to adjust scores
        old_result = round_to_update['result']

        # Reverse the previous score
        if old_result == "Player Wins":
            self.p_score -= 1
        elif old_result == "Computer Wins":
            self.c_score -= 1

        # Get new choices
        opts = ['Rock', 'Paper', 'Scissors']
        try:
            print("\nUpdating Round", round_number)
            p_ch = int(input('Enter your choice (1. Rock, 2. Paper, 3. Scissors): '))
            if p_ch not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            return

        player_choice = opts[p_ch - 1]
        computer_choice = random.choice(opts)

        print(f"Your choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")

        # Determine new result
        result = self.determine_winner(player_choice, computer_choice)

        # Update scores based on new result
        if result == "Player Wins":
            self.p_score += 1
        elif result == "Computer Wins":
            self.c_score += 1

        # Update the round
        round_to_update['player_choice'] = player_choice
        round_to_update['computer_choice'] = computer_choice
        round_to_update['result'] = result

        print(f"Round {round_number} updated with new result: {result}")
        self.display_scores()

    def delete_round(self, round_number):
        for round in self.rounds:
            if round['round'] == round_number:
                if round['result'] == "Player Wins":
                    self.p_score -= 1
                elif round['result'] == "Computer Wins":
                    self.c_score -= 1
        self.rounds = [round for round in self.rounds if round['round'] != round_number]
        print(f"Round {round_number} deleted.")

    def reset_game(self):
        self.rounds.clear()
        self.p_score = 0
        self.c_score = 0
        print("Game reset.")

    def play_round(self):
        opts = ['Rock', 'Paper', 'Scissors']
        
        try:
            p_ch = int(input('Enter your choice (1. Rock, 2. Paper, 3. Scissors): '))
            if p_ch not in [1, 2, 3]:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            return

        player_choice = opts[p_ch - 1]
        computer_choice = random.choice(opts)

        print(f"Your choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = self.determine_winner(player_choice, computer_choice)

        if result == "Player Wins":
            self.p_score += 1
        elif result == "Computer Wins":
            self.c_score += 1

        print(f"Result: {result}")
        self.add_round(player_choice, computer_choice, result)

game = RockPaperScissors()

while True:
    print("\n1. Play Round\n2. Display Rounds\n3. Display Scores\n4. Update Round\n5. Delete Round\n6. Reset Game\n7. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        game.play_round()
    elif choice == '2':
        game.display_rounds()
    elif choice == '3':
        game.display_scores()
    elif choice == '4':
        try:
            round_number = int(input("Enter the round number to update: "))
            game.update_round(round_number)
        except ValueError:
            print("Invalid round number")
    elif choice == '5':
        try:
            round_number = int(input("Enter the round number to delete: "))
            game.delete_round(round_number)
        except ValueError:
            print("Invalid round number")
    elif choice == '6':
        game.reset_game()
    elif choice == '7':
        print("Exiting the game.")
        break
    else:
        print("Invalid choice. Please try again.")
