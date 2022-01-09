import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
start_playing = True
while start_playing:
    #the user should enter a number 0 or 1 or 2
    prompt = "\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
    user_choice=int(input(prompt))

    #now the computer should choice a number:

    computer_choice = random.randint(0,2)
    print(computer_choice)

    #now display the user and computer choice
    print("\nYou choice:")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

    print("\nComputer choice:")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    else:
        print(scissors)

    #compare and display the winner:
    if (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0):
        print("You Winn")

    elif (user_choice == 2 and computer_choice == 0) or (user_choice == 1 and computer_choice == 2) or (user_choice == 0 and computer_choice == 1):
        print("Computer Winn")
    else:
        print("Tie")

    prompt="\nDo you want to continue playing ? Type 'yes/y' or no/n\n"
    answr=input(prompt).lower()
    if answr == "no" or answr == "n":
        start_playing = False
        print("\nExit")

