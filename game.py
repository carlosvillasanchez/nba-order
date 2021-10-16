import json
from random import randrange



with open('30.json') as json_file:
    data = json.load(json_file)
    players = data["players"]
    total_amount = len(data["players"])
    final_list = []

    for i in range(total_amount):
        index = randrange(total_amount-i)
        player = players[index]
        del players[index]
        # print(index, player)
        
        up = len(final_list)
        down = 0
        while (up != down):
            compare_index = randrange(down, up)
            # decision
            decision = 0
            while(decision != 1 and decision != 2):
                print("Who is better?")
                print(player[0] + " (1)  OR  " + final_list[compare_index][0] + " (2)") 
                decision = int(input())
            
            if decision == 1:
                # if better
                down = compare_index + 1        
            else:
                # if worse
                up = compare_index
        final_list.insert(up, player)
    print(final_list)
