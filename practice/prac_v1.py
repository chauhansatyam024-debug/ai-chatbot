#
# import re
# def tokesnizaton(word):
#     """ to tokenize"""
#     tokens = word.lower()
#     tokens = re.sub(['^\\w\\s']," ",tokens)
#
#     return tokens
#
#
#
# def getResponse(user_input):
#
#
#
#
#
# def main():
#     print("type quit to exit :\n ")
#
#     while True:
#
#         user_input = input("type : ")
#
#         if user_input.lower() == "quit":
#             break
#         else :
#             getResponse(user_input)
#
#
#
#
# """import re
#
# text = "Dr. Smith paid $19.99 for the book. He's happy! #NLP is cool."
#
# # 1. Simple word tokens
# re.findall(r'\w+', text)
# # ['Dr', 'Smith', 'paid', '19', '99', 'for', 'the', 'book', 'He', 's', 'happy', 'NLP', 'is', 'cool']
#
# # 2. Keep contractions together
# re.findall(r"\b[\w']+\b", text)
# # ['Dr.', 'Smith', 'paid', '19.99', "He's", 'happy', 'NLP', 'cool']
#
# # 3. Words + standalone punctuation (common in NLP)
# re.findall(r"\b\w+\b|[.,!?#$]", text)
# # ['Dr', '.', 'Smith', 'paid', '$', '19', '.', '99', ..., '#', 'NLP', ...]
#
# # 4. Split on whitespace AND punctuation
# re.split(r"[\s.,!?]+", text)
# # ['Dr', 'Smith', 'paid', '$', '19', '99', 'for', 'the', 'book', ...]
#
# # 5. Extract specific token types
# re.findall(r'[@#]\w+', text)       # mentions & hashtags → ['@user', '#NLP']
# re.findall(r'https?://\S+', text)  # URLs
# re.findall(r'[\w.]+@[\w.]+\.\w+', text)  # emails
#
# """