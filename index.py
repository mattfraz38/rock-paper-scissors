import stdiomask
# hide user input with asterisks

print("""
**************************************

            ...rock...
            ...paper...
            ...scissors...

*************** SHOOT! ***************

""")

# get secret rock paper scissors choice from user
print("Player 1!")
player_one = stdiomask.getpass("What's your choice? ")
# player_one = input("What's your choice? ")
# player_one = choice_to_num(player_one)

print("Player 2!")
player_two = stdiomask.getpass("What's your choice? ")
# player_two = input("What's your choice? ")
# player_two = choice_to_num(player_two)

print(player_one, player_two)

# convert player inupt to a numerical value
# def choice_to_num(choice):
#   while choice and choice.isalpha():
#     choice = choice.lower()

#     if choice.match("rock"):
#       value = 3
#     elif choice.match("scissors"):
#       value = 2
#     else:
#       value = 1
#   return value


# compare player_one and player_two choice
# determine a winner and print the result
# def rps_game(p1, p2):
#   winner = None

#   if p1 > p2:
#     winner = f"{p1} wins!"
#   elif p2 > p1:
#     winner = f"{p2} wins!"
#   else:
#     winner = "'Draw!"

#     result = """
#     ******************************************

#     \t\tPlayer 1: {p1}
#     \t\tPlayer 2: {p2}

#     \t\t{winner}

#     ******************************************
#     """

#     print(result)
