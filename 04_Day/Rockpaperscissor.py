import random

your_choice = int(input("What do you choose? type 0 for rock, 1 for paper or 2 for scissors \n"))
computer_choice = random.randint(0, 2)
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


if your_choice == 0:
    print("Your Choice")
    print(rock)
    if computer_choice == 0:
        print("Computer choice")
        print(rock)
        print("Draw")
    elif computer_choice == 1:
        print("Computer choice")
        print(paper)
        print("Computer Win")
    elif computer_choice == 2:
        print("Computer choice")
        print(scissors)
        print("You Win")
elif your_choice == 1:
    print("Your Choice")
    print(paper)
    if computer_choice == 0:
        print("Computer choice")
        print(rock)
        print("You Win")
    elif computer_choice == 1:
        print("Computer choice")
        print(paper)
        print("Draw")
    elif computer_choice == 2:
        print("Computer choice")
        print(scissors)
        print("Computer Win")
elif your_choice == 2:
    print("Your Choice")
    print(scissors)
    if computer_choice == 0:
        print("Computer choice")
        print(rock)
        print("Computer Win")
    elif computer_choice == 1:
        print("Computer choice")
        print(paper)
        print("You Win")
    elif computer_choice == 2:
        print("Computer choice")
        print(scissors)
        print("Draw")
