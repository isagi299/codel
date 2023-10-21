# Rock Paper Scissors
import random
my_input = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
if my_input>=3 and my_input<0:
    print("you input an invalid number")
print("\n")
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
pic =[rock,paper,scissor]
com_input = random.randint(0,2)
print("Your chose :\n")
print(pic[my_input])
print("\nComputer chose : \n")
print(pic[com_input])


if my_input==0 and com_input==2 or my_input==1 and com_input ==0 or my_input==2 and com_input == 1:
    print("YOU WIN!!!!")
elif com_input==0 and my_input==2 or com_input==1 and my_input ==0 or com_input==2 and my_input == 1:
    print("YOU LOSE??")
else:
    print("DRAW***")