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
scine = [rock, paper, scissors]
if your_choice >= 3 or your_choice < 0:
    print("Enter valid input")
else:
    print("Your choice: ")
    print(scine[your_choice])
    print("computer choice: ")
    print(scine[computer_choice])
    if your_choice == 0:
        if computer_choice == 0:
            print("Draw")
        elif computer_choice == 1:
            print("Computer Win")
        elif computer_choice == 2:
            print("You Win")
    elif your_choice == 1:
        if computer_choice == 0:
            print("You Win")
        elif computer_choice == 1:
            print("Draw")
        elif computer_choice == 2:
            print("Computer Win")
    elif your_choice == 2:
        if computer_choice == 0:
            print("Computer Win")
        elif computer_choice == 1:
            print("You Win")
        elif computer_choice == 2:
            print("Draw")

