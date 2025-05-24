print("The Lottery")

import random

ran_num = [0,1,2,3,4,5,6,7,8,9]
winning = random.sample(ran_num, k=7)


strt_game = input("Would you like to generate the winning lottery numbers for today's game? y/n? ").lower()
if strt_game == "y":
    print(winning)

elif strt_game == "n":
    print("Good Bye")



