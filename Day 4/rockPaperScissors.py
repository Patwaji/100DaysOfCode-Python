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

rock_paper_scissor = [rock, paper, scissors]
computer_choice = random.randint(0,2)

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(rock_paper_scissor[human_choice])

print("Computer chose : " + rock_paper_scissor[computer_choice])

if human_choice == 0 and computer_choice == 2 :
    print("You win.")
elif human_choice == 0 and computer_choice == 1 :
    print("You lose")
elif human_choice == 1 and computer_choice == 2 :
    print("You lose")
elif human_choice == 1 and computer_choice == 0 :
    print("You win")
elif human_choice == 2 and computer_choice == 0 :
    print("You lose")
elif human_choice == 2 and computer_choice == 1 :
    print("You win")
else :
    print("It's a draw")
