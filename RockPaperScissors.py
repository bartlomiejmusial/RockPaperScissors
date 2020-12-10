import random
import os
import time

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
list1 = [rock, paper, scissors]
print("Welcome to the rock, paper and scissors game!")
player = int(input("Choose one option and enter the number\n1 - rock\n2 - paper\n3 - scissors\n"))
computer = random.randint(1,3)

os.system('clear')

print("✊")
time.sleep(0.5)
print("✋")
time.sleep(0.5)
print("✌️")
time.sleep(0.5)

os.system('clear')
if player < 1 or player > 3:
  print("You entered an invalid number!\nYOU LOSE")
elif(player == computer):
  print("\nYou chose:")
  print(list1[player-1])
  print("Computer chose:")
  print(list1[computer-1])
  print("\nTIE!")
elif(player == 1 and computer == 2):
  print("\nYou chose:")
  print(list1[player-1])
  print("Computer chose:")
  print(list1[computer-1])
  print("\nComputer wins!")
elif(player == 1 and computer == 3):
  print("\nPlayer wins!")
  print("\nYou chose:")
  print(list1[player-1])
  print("Computer chose:")
  print(list1[computer-1])
  print("\nPlayer wins!")
elif(player == 2 and computer == 1):
  print("\nYou chose:")
  print(list1[player-1])
  print("Computer chose:")
  print(list1[computer-1])
  print("\nPlayer wins!")
elif(player == 3 and computer == 1):
  print("\nYou chose:")
  print(list1[player-1])
  print("Computer chose:")
  print(list1[computer-1])
  print("\nComputer wins!")
elif(player == 2 and computer == 3):
  print("\nYou chose:")
  print(list1[player-1])
  print("Computer chose:")
  print(list1[computer-1])
  print("\nComputer wins!")
elif(player == 3 and computer == 2):
  print("\nYou chose:")
  print(list1[player-1])
  print("Computer chose:")
  print(list1[computer-1])
  print("\nPlayer wins!")
