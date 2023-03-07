import random
#1 Welcome User
print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
#2 Ask user how many rounds they want to play
rounds=int(input("How many rounds would you like to play? ==> "))
#3 Make a list of the 5 choices
Choices=["Rock","Paper","Scissors","Lizard","Spock"]
# User defined function
def beats(x,y):
    if x in ["1","Rock"] and y in["Scissors","Lizard"] or x in ["2", "Paper"] and y in ["Rock","Spock"] or x in ["3","Scissors"] and y in ["Paper","Lizard"] or x in ["4", "Lizard"] and y in ["Paper","Spock"] or x in ["5", "Spock"] and y in ["Rock","Scissors"]:
        return True
    else:
        return False
#4 Make accumulator variables for player and bot wins
player_wins=0
bot_wins=0
#5 Make accumulators for player choices
player_rock=0
player_paper=0
player_scissors=0
player_lizard=0
player_spock=0
#6 Make accumulators for bot choices
bot_rock=0
bot_paper=0
bot_scissors=0
bot_lizard=0
bot_spock=0
#5 Make a for loop for amount of rounds
for num in range(rounds):
    #6 Display round
    print("Round", num+1, "of", rounds,":")
    #7 Ask user about their choice
    player_choice=input("What item do you choose?\n 1 - rock\n 2 - paper\n 3 - scissors\n 4 - lizard\n 5 -spock\n your answer ==> ")
    #8 Tally the player choice
    if player_choice=="1":
        player_rock+=1
    elif player_choice=="2":
        player_paper+=1
    elif player_choice=="3":
        player_scissors+=1
    elif player_choice=="4":
        player_lizard+=1
    elif player_choice=="5":
        player_spock+=1
    #8 randomly choose bot choice
    bot_choice=random.choice(Choices)
    #9 Tally the bot choices
    if bot_choice=="1":
        bot_rock+=1
    elif bot_choice=="2":
        bot_paper+=1
    elif bot_choice=="3":
        bot_scissors+=1
    elif bot_choice=="4":
        bot_lizard+=1
    elif bot_choice=="5":
        bot_spock+=1
    print("I chose: ", bot_choice)
    #9 Determine winner using function
    if beats(player_choice,bot_choice):
        print("You win this round!")
        player_wins+=1
    elif beats(bot_choice,player_choice):
        print("I win this round!")
        bot_wins+=1
    else:
        print("This round was a tie!")


