# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import numpy as np
def player(prev_play, opponent_history=[], my_history=[], detected=[],cnt=[0],play_order=[{  "RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0,}]):
    guess="R"
    cnt[0]+=1
    if not prev_play:
        prev_opponent_play = 'R'
        detected.append(False)
    opponent_history.append(prev_play)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if cnt[0]<1000: #quincy
        guess = beat_quincy(opponent_history[-2] if len(opponent_history) > 1 else "R", opponent_history[-1])
    elif cnt[0]<2000 : #abbey
        guess = defeat_abbey(my_history[-1], my_history[-2:], play_order)
    elif cnt[0]<3000: #kris 
        guess = ideal_response[ ideal_response[my_history[-1]] ] 
    elif cnt[0]<4000:  # mrugesh
        guess = ideal_response[ marguesh_idea(my_history[-10:])]
    else: 
        guess=random_guess()
       
    my_history.append(guess)
    return guess

def random_guess():
    #radom solution
    guess= "R"
    x= np.random.uniform(0,3)
    if (x>2):
        guess = "R"
    elif (x>1):
        guess = "P"
    else:
        guess ="S"
    return guess

def beat_quincy(A,B):
    if B=="S": # his next is R
        return "P"
    elif B=="R" and A=="S": # his next is R
        return "P"
    elif B=="R" and A=="R":# his next is P
        return "S"
    elif B=="P" and A=="P": # his next is S
        return "R"
    else: # "RP" his next is P
        return "S"

def marguesh_idea(last_ten):
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    most_frequent = max(set(last_ten), key=last_ten.count)
    if most_frequent == '':
        most_frequent = "S"
    return ideal_response[most_frequent]

def defeat_abbey(prev_opponent_play, opponent_history, play_order):
    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[ideal_response[prediction]]