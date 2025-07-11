"""
Rock Paper Scissors Game
------------------------
A fun command-line game with:
- Input validation
- Scoring system
- Play again / quit option
- ASCII art and emoji output
"""

import random
import time

def rps_game():

    """
    Runs an interactive Rock Paper Scissors game:
    - Player vs Computer
    - Tracks user score, computer score, and draws
    - Ends when user chooses to quit or stop playing

    """

    user_score = 0
    comp_score = 0
    draws = 0

    rock_ascii = '''
            _______
        ---'   ____)
             (_____)
             (_____)
              (____)
        ---.__(___)
        '''

    paper_ascii = '''_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

    scissors_ascii = '''
 _______
---'   ____)____
           ______)
       __________)
      (____)
---.__(___)
'''


    while True:
        print('-'*40)
        print("\n🎯 Get ready to play in...")
        for i in range(3 , 0 , -1):
            print(f"{i}...")
            time.sleep(1)

# Data of the user and computer

        valid = {
            "rock": "🪨",
            "paper": "📄",
            "scissors": "✂️",
            "quit" : ""
        }

        comp = ["rock" , "paper" , "scissors"]

# User choice section

        user_choice = input("\nRock/Paper/Scissors/Quit : ").lower()

        if user_choice not in valid:
            print("-" * 40)
            print("Invalid choice, Try again")
            continue

        if user_choice == "quit":
            print("\n" + "-" * 40)
            print("\nThanks for playin!   🎉")
            print(f"🎮 Your score = {user_score}")
            print(f"🤖 Computer score {comp_score}")
            print("\n" + "-" * 40)
            break

        ascii_art = {
            "rock" : rock_ascii,
            "paper" : paper_ascii,
            "scissors" : scissors_ascii
            }
        
        for line in ascii_art[user_choice].splitlines():
            print(line.center(40))

        print("\n🎮 Your Choice:")
        print(f"    {valid[user_choice]}  {user_choice.upper()}")  

# Computer choice section 

        comp_choice = random.choice(comp)

        print("\n🤖 Computer Choice:")
        print(f"    {valid[comp_choice]}  {comp_choice.upper()}")  

        for line in ascii_art[comp_choice].splitlines():
            print(line.center(40))


# Winning Condition Section

        if user_choice == comp_choice:
            print("\nIt's a tie 😐")
            draws += 1
        elif (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            print("\nYou won! 🎉")
            user_score += 1
        else:
            print("\nComputer won! 💻")
            comp_score += 1
        
        print(f"\n🎮 Your score = {user_score}")
        print(f"🤖 Computer score = {comp_score}")
        print(f"🛠️  Draws = {draws}")
        print("\n" + "-"*40 )
    
# Play again section to play infinite times
        while True:
            play_again = input("Wanna play again yes/no : ").lower()


            if play_again in ["yes" , "no" ]:
                break
            print("Invalid Choice , Type yes/no ")
        if play_again == "no":
            print( "-" * 40)
            print("\nThanks for playing")
            print(f"\n🎮 Your score = {user_score}")
            print(f"🤖 Computer score {comp_score}")
            print(f"🛠️  Draws = {draws}")
            print("\n" + "-" * 40)
            return

if __name__ == "__main__":
    rps_game()
