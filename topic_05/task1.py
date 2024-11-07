import random


objects = {
    "stone": "scissor",
    "scissor" : "paper",
    "paper":"stone"
}


def playersChoice(objects:list)->list:
    bot = random.choice(list(objects.keys()))
    try:
        player = input("select an item [stone, scissor, paper]: ")
        if player not in ["stone", "scissor", "paper"]:
            raise ValueError("Incorrect input")
    
    except Exception as e :
        print(f"Error in entering operation: {e}")
        return playersChoice(objects)
    print(f"\nbot: {bot}\n")
    return bot, player


def game(playersChoice:list, objects: list) -> list:
    if (playersChoice[0] == playersChoice[1]):
        print("Draw🤝")
        return [0, 0]
    elif(objects[playersChoice[0]] != playersChoice[1]):
        print("You win🎊")
        return [0, 1]
    else:
        print("You lose💢")
        return [1, 0]


score = [0, 0]
while True:
    try:  
        print(f"\nScore: bot {score[0]} you {score[1]}\n")
        res = game(playersChoice(objects), objects)
        if(res[0]==0 and res[1]==0):
            continue
        elif(res[0]==1):
            score[0] = score[0] + 1
        else:
            score[1] = score[1] + 1
    except KeyboardInterrupt:
        print(f"\nFinal score: bot {score[0]} vs you {score[1]}")
        break
