from rps_art import rock, paper, scissors
import random

game_is_finished = False
game_images = [rock, paper, scissors]


while not game_is_finished:
    #Coding the user side of the game
    print("\n============================================================================================================")
    choice = int(input("Welcome to the Rock Paper and Scissors Game. Please select '0' for Rock, '1' for Paper, and '2' for Scissors\n"))
    print(game_images[choice])

    #Coding the computer side
    print("\nThe computer chose: \n")
    comp_choice = random.randint(0, 2)
    print(game_images[comp_choice])

    #Coding the comparison and result
    if choice <0 or choice >2:
      print("Please select from the given options!")
    elif comp_choice == 2 and choice == 0:
      print("You won!")
    elif choice == 2 and comp_choice == 0:
      print("You lost..")
    elif comp_choice > choice:
      print("You lost!")
    elif choice > comp_choice:
      print("You won..")
    else:
      print("It is a draw.")
    
    playing = input("\nType 'n' to quit, any other letter to continue..").lower()
    if playing == "n":
        game_is_finished = True
        print("\nThank you for playing!")
    