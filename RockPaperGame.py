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

import random

images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for rock , 1 for paper or 2 for scissors"))
print(images[choice])

choice1 = random.randint(0, 2)
print("Computer choose:-")
print(images[choice1])

if choice >= 3 or choice < 0:
    print("You typed an invalid number, you lose!")
elif choice == 0 and choice1 == 2:
    print("You win!")
elif choice1 == 0 and choice == 2:
    print("You lose")
elif choice1 > choice:
    print("You lose")
elif choice > choice1:
    print("You win!")
elif choice1 == choice:
    print("It's a draw")
