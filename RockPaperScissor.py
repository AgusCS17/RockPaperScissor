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

#Write your code below this line 👇
player = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors."))
ai = random.randint(0, 2)
choice = [rock, paper, scissors]

print(choice[player])
print("Computer choose: ")
print(choice[ai])

if player == 0 and ai == 2:
    print("You Win!")
elif player == 1 and ai == 0:
    print("You Win!")
elif player == 2 and ai == 1:
    print("You Win!")
elif ai > player or ai < player:
    print("You lose!")
elif player == ai:
    print("Draw!")

