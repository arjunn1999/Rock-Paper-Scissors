# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from numpy.random import randint
def player(prev_play, opponent_history=[]):
    choices = ["R","P","S"]
    opponent_history.append(prev_play)
    if len(opponent_history)==0:
        guess = choices[randint(3)]
    else:
        opponent_freq={"R":0,"P":0,"S":0}
        for x in opponent_history:
            if x!='':
                opponent_freq[x]+=1
        if opponent_freq["R"]>opponent_freq["S"]:
            if opponent_freq["P"]>opponent_freq["R"]:
                guess = "S"
            else:
                guess = "P"
        else:
            if opponent_freq["S"]>opponent_freq["P"]:
                guess="R"
            else:
                guess = "S"
    return guess
