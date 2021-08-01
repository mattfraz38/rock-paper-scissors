# hide user input with asterisks
import stdiomask

def choice_to_num(choice):
  choice.lower()
  while True:
    try:
      # if choice and choice.isalpha():
      choice = choice.lower()

      # if choice == "rock":
      #   return 3
      #   break
      # elif choice == "paper":
      #   return 2
      #   break
      # elif choice == "scissors":
      #   return 1
      #   break

    except ValueError:
      choice = stdiomask.getpass("What's your choice? ")
    else:
      return
      break
      # print("Sorry, one more time...")
    #   continue
    # else:
    #   break

    # else:
    #   if choice == "rock":
    #     return 3
    #     break
    #   elif choice == "paper":
    #     return 2
    #     break
    #   else:
    #     return 1
    #     break

  # if choice == "rock":
  #   return 3
  # elif choice == "paper":
  #   return 2
  # else:
  #   return 1

# convert player inupt to a numerical value


# compare player_one and player_two choice
# determine a winner and print the result
def calc_rps_winner(p1, p2):

  if p1 == "rock" and p2 == "scissors":
    print("Player One Wins!")
  elif p1 == "rock" and p2 == "paper":
    print("Player Two Wins!")
  elif p1 == "paper" and p2 == "rock":
    print("Player One Wins!")
  elif p1 == "paper" and p2 == "scissors":
    print("Player Two Wins!")    
  elif p1 == "scissors" and p2 == "rock":
    print("Player Two Wins!")
  elif p1 == "scissors" and p2 == "paper":
    print("Player One Wins!")    
  else:
    print("Draw!")    

#     result = """
#     ******************************************

#     \t\tPlayer 1: {p1}
#     \t\tPlayer 2: {p2}

#     \t\t{winner}

#     ******************************************
#     """

#     print(result)  