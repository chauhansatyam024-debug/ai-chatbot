import re
def tokenize(input):
    """ function to remove _ , ? , etc"""
    tokens = input.lower()

    tokens = re.sub(r'[^\w\s]' , " ",tokens)

    return input


def get_response(user_input):
    """ this function is for chatting inputs"""
    user_input = tokenize(user_input)

    user_input = user_input.lower().strip()

    if "hello" in user_input or "hi" in user_input:

        return "Hey there! How's it going?"


    elif "how are you" in user_input:

        return "I'm just code, but I'm doing great!"


    elif "bye" in user_input:

        return "See you later!"


    else:

        return "I don't understand that yet."


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



# we don't to call all code together
if __name__ == "__main__":
    main() # so it we only run when we call it
