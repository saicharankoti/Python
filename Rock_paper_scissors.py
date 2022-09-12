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
player=int(input("select 0 for rock 1 for paper and 2 for scissors"))
if player>=3 or player<0:
  print("invalid sign you lose")
else:
  list=[rock,paper,scissors]
  length_list=len(list)
  player_choice=list[player]
  print(f"your chose{player_choice}")
  choice=int(random.randint(0,length_list-1))
  comp_choice=list[choice]
  print(f"computer chose {comp_choice}")
  if player==choice:
    print("Draw")
  elif player==0 and choice==2:
    print("You Win")
  elif player==2 and choice==1:
    print("You Win")
  elif player==1 and choice==0:
    print("you win")
  else:
    print("You Lose")
