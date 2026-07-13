import re
import json
from random import choice as  ch # if we are only using choice , why not just import choice only

with open("intents.json" ,"r") as file:
    data = json.load(file)

def tokenize(token):
    """ tokenize the words , i mean split them ,so chatbot can use it """
    token = token.lower()
    token = (re.sub(r"[^\w\s]" , " " , token)).split()
    return token


def score(tokens , pattern_inputs):
    """ here we choose respons by giving score to each response ,
        now in version 3 we are using jaccard similiarity method
        by using union and intersectiion and get value in ratio between 0 - 1

        in simple words , scoring is becomeing more strict """


    token_set = set(tokens)
    pattern_set = set(pattern_inputs)
    union_set = token_set | pattern_set
    inter_set = token_set & pattern_set

    if  len(union_set) == 0 : return 0 # avoiding dividing by  0 {extreme case}

    return len(inter_set) / len(union_set) # we will get score in b/w 0 - 1


    


def getToken(token):

    """for output , here we take the best response"""


    token = tokenize(token)
    best_score = 0
    best_response = None
    for intent in data['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = tokenize(pattern)
            s = score(token , pattern_tokens)
            if( s > best_score):
                best_score = s
                best_response = intent["responses"]
    """ here we check if there is no suitabel response , so we go to  fallback , coz the bot fallback"""

    if ( best_response is None): # there can only be one None in whole progrram , so "is" check if this point to that "None"
        for intent in data["intents"]:
                if(intent["tag"] == "fallback"):
                    best_response = intent["responses"]


    return ch(best_response)

def main():
    """this function is main , we all know what main is"""
    print("type 'quit' to exit")


    while True :
        user_input = input("You: ")


        if user_input.lower() == 'quit':
            print("Chatbot: bye")
            break


        response = getToken(user_input)
        print(f"Chatbot:{response} ")

if __name__ == "__main__":
    main()
