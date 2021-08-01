# hide user input with asterisks
import stdiomask
from functions import choice_to_num, calc_rps_winner

print("""
**************************************

            ...rock...
            ...paper...
            ...scissors...

*************** SHOOT! ***************

""")

# get secret rock paper scissors choice from user
print("Player 1!")
p1_choice = stdiomask.getpass("What's your choice? ")
# p1_num_val = choice_to_num(p1_choice)

print("Player 2!")
p2_choice = stdiomask.getpass("What's your choice? ")
# p2_num_val = choice_to_num(p2_choice)

calc_rps_winner(p1_choice, p2_choice)
