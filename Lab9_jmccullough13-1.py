#Match Coins
#Jeffrey McCullough
#This game has two players flip coins and gain or lose points based on the outcome.
#February 28, 2023

from coin import Coin
def main():
    player_1 = Coin(20, "Heads")
    player_2 = Coin(20, "Heads")
    again = input("Do you want to play? Y for yes: ")
    while again.upper() == "Y":
        player_1.toss()
        player_2.toss()
        if player_1.toss() == player_2.toss():
            player_1.set_amount(1)
            player_2.set_amount(-1)
        else:
            player_1.set_amount(-1)
            player_2.set_amount(1)

        print(f"Player 1 got a {player_1.get_sideup()} and player 2 got a {player_2.get_sideup()}")
 
        if player_1.get_amount() == 0 or player_2.get_amount() == 0:
            print("Game over")
            break

        again = input("Do you want to play again? Y for yes: ")
    
    print(f"Player 1 has {player_1.get_amount()} coins and Player 2 has {player_2.get_amount()} coins")
    if player_1.get_amount() > player_2.get_amount():
        print("Player 1 wins!")
    elif player_1.get_amount() < player_2.get_amount():
        print("Player 2 wins!")
    else:
      print("Tie!")
    print("Thank you for playing!")

main()
