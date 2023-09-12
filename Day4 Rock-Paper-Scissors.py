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
print("Welcome to the game of Rock - Paper - Scissors")
print("Rock Paper Scissors, goes beyond the simple interactions of scissors cutting paper, paper covering rock, and rock crushing scissors.\nThis globally cherished game levels the playing field for everyone.It is the go-to solution for settling disputes, determining who gets the last pizza slice, or assigning dish duty.")
print("\nLets Play!")
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
if user_choice>2 or user_choice<0:
    print("You typed an invalid number, please try")
else:
    #printing the users choice
    print("You chose:")
    if user_choice==0:
        print(rock)
    elif user_choice==1:
        print(paper)
    elif user_choice==2:
        print(scissors)


    #picking computer's choice randomly
    comp_choice = random.randint(0,2)

    #printing the computer's choice
    print("Computer chose:")
    if comp_choice==0:
        print(rock)
    elif comp_choice==1:
        print(paper)
    elif comp_choice==2:
        print(scissors)


    if (user_choice==2 and comp_choice==1) or (user_choice==1 and comp_choice==0) or (user_choice==0 and comp_choice==2) :
        print("You win")
    elif user_choice == comp_choice:
        print("It's a draw")
    else:
        print("You lose")

