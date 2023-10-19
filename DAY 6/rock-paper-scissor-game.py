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

#Write your code below this line 👇

import random

user_choice = int(input(print("What do you choose\n1 = rock\n2 = paper\n3 = scissors\n")))

if user_choice == 1:
  print("YOU CHOOSE - ROCK ")
  print(rock)
elif user_choice == 2:
  print("YOU CHOOSE - PAPER ")
  print(paper)
else:
  print("YOU CHOOSE - SCISSORS")
  print(scissors)

  
computer_choice = random.randint(1,3)

if computer_choice == 1:
  print("COMPUTER CHOOSE - ROCK")
  print(rock)
elif computer_choice == 2:
  print("COMPUTER CHOOSE - PAPER")
  print(paper)
else:
  print("COMPUTER CHOOSE - SCISSORS")
  print(scissors)

if user_choice == computer_choice:
  print("GAME TIE")
elif user_choice == 1 and computer_choice == 2:
  print("YOU LOSE")
elif user_choice == 1 and computer_choice == 3:
  print("YOU WIN")
elif user_choice == 2 and computer_choice == 1:
  print("YOU WIN")
elif user_choice == 2 and computer_choice == 3:
  print("YOU LOOSE")
elif user_choice == 3 and computer_choice == 1:
  print("YOU LOOSE")
elif user_choice == 3 and computer_choice == 2:
  print("YOU WIN")
  