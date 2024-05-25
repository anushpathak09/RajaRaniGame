#GAME OF OUR CHILDHOOD TIME
#RAJA,RANI,CHOR,POLICE GAME
#Author:Anush Pathak

# importing modules
import os
import random
import time

# creating program
def main():
     user_name = input("Please enter your name: ")
     print("Welcome", user_name, "to our game")
     print("[1] | Start the game")
     print("[0] | Exit")
     opt = input("Choose option: ")
     if opt == "1":
          game()
     else:
          (os.system("exit"))
def game():
     print("Menu:")
     #this all options is only for confusion creation for gamer.
     print("1. Option 1")
     print("2. Option 2")
     print("3. Option 3")
     print("4. Option 4")
     print("5. Exit")
     opt_game = input("Choose option: ")
     if opt_game == "1":
          game_option_()
     elif opt_game == "2":
          game_option_()
     elif opt_game == "3":
          game_option_()
     elif opt_game == "4":
          game_option_()
     elif opt_game == "5":
          os.system("exit")
     else:
          print("Wrong option")


# creating text for random print of text.


def print_random_text():
    robots = ["YOU", "ROBOT-1", "ROBOT-2", "ROBOT-3"]
    total_scores = {robot: 0 for robot in robots}

    for loop in range(1, 6):  # Repeat the process 5 times
        texts = ["Raja=1000", "Rani=800", "Chor=0", "Police=500"]
        print(f"\nGame {loop} scores:")
        for robot in robots:
            if texts:
                random_text = random.choice(texts)
                name, score = random_text.split('=')
                score = int(score)
                total_scores[robot] += score
                texts.remove(random_text)
                print(f"{robot}: {total_scores[robot]}", end=" | ")
                time.sleep(1)  # 3-second delay
        print()  # Move to the next line for the next loop iteration

    # Rank the robots based on their total scores
    ranked_robots = sorted(total_scores.items(), key=lambda x: x[1], reverse=True)
    positions = ["RAJA", "RANI", "POLICE", "CHOR"]
    for i, (robot, _) in enumerate(ranked_robots):
        print(f"\n{positions[i]} position goes to {robot} with total score {total_scores[robot]}")





def game_option_():
     print_random_text()


main()

#further work is going on.
#if you have some ideas please let me know.
