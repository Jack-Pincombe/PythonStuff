import random
import time

#setting the initial variables
rock = 1
paper = 2
scissors = 3

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, scissors: paper, paper:rock }


#setting the initial scores to 0
player_score = 0
computer_score = 0


#outline of the functions that I will use

def start():

    print "lets play a game of rock, paper , scissors"

    while game():
        pass
    scores()



def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():

    while True:
        print
        player = raw_input("Rock 1\npaper 2\nand scissors /3\nmake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "Please enter 1, 2 or 3"



def result(player, computer):
    print "1...."
    time.sleep(1)
    print"2..."
    time.sleep(1)
    print "3..."
    time.sleep(0.5)
    print "computer threw {0}!".format(names[computer])
    global computer_score, player_score
    if player == computer:
        print "Tie game"
    else:
        if rules[player] == computer:
            print "Congrats you won"
            player_score += 1

        else:
            print "The computer is victorious"
            computer_score += 1

def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ('y', 'Y', 'Yes','yes'):
        return answer
    else:
        print "Thank you for playing"

def scores():
    global player_score, computer_score
    print "High Scores!!!"
    print "Player, " , player_score
    print "Computer ", computer_score

if __name__ == "__main__":
    start()