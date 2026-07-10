import re
import json
import random as rnd

with open("intents.json" , "r") as file:
    data = json.load(file)


def tokenize(tokens):
    """ to tokenize the pattern """
    tokens = tokens.lower()
    tokens = re.sub(r"[^\w\s]"," " , tokens) # to remove ? , _ ,etc
    tokens = tokens.split() # to get list
    return tokens


def score(tokens,pattern_inputs):
    """to get best score of patterns in intents.json data"""
    return len(set(tokens) & set(pattern_inputs))


def get_response(tokens):
    token = tokenize(tokens)
    best_score = 0
    best_response = None # coz my data already has fallback tag and their response
    for intents in data["intents"]: # to get intents from intents
        for pattern in intents["patterns"]: # to get pattern
            pattern_inputs = tokenize(pattern) # tokenize them
            s = score(token,pattern_inputs) # to get best score ,from each pattern
            if( s > best_score):
                best_score = s
                best_response = intents["responses"] # it give whole line to best_repsonse
                                                    # i mean it give whole lsit of patterns
    if best_response is None:
        for intents in data["intents"]:
            if intents["tag"] == "fallback":
                best_response = intents["responses"]
                break
    return rnd.choice(best_response)

def main():
    """this function is main , we all know what main is"""
    print("type 'quit' to exit")


    while True :
        user_input = input("You: ")


        if user_input.lower() == 'quit':
            print("Chatbot: bye")
            break


        response = get_response(user_input)
        print(f"Chatbot:{response} ")

if __name__ == "__main__": # so it only run it needed
    main()