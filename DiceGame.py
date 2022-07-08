import random

def rolldice():
   while True:
      player_input = input("Do you want to roll the dice?(y/n): ")
      player_input.lower()
      if(player_input!="n" and player_input!="y"):
         print("Input correct value")
      elif(player_input=="y"):
         generatenumber()
      else:
         print("Goodbye :)")
         break


def generatenumber():
      print("You rolled "+str(random.randint(1,6)))