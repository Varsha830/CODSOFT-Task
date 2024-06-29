print("Welcome to Rock Paper Scissor game !")
import random
choices=["rock","paper","scissor"]
def play_game():
    while True:
        user_choice: str=input("Enter your choice (rock/paper/scissor):")
        while user_choice not in choices:
            print("Invalid choice.Please choose again.")
            user_choice=input("Enter your choice (rock,paper,scissor):" )
        computer_choice=random.choice(choices)
        print("you choose:", user_choice)
        print("computer choose:", computer_choice)
        if user_choice==computer_choice:
            print("Game is tie!")
        elif (user_choice=='rock' and computer_choice=='scissor') or \
        (user_choice=='paper' and computer_choice=='rock') or \
        (user_choice=='scissor' and computer_choice=='paper'):
             print("you win!")
        else:
             print("you lose!")
        play_again=input("\nDo you want to play again?Yes/No")
        if play_again!="Yes":
            print("Thanks for playing")
            break

play_game()

