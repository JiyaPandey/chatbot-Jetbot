import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    ['(hi|hello|hey)', ['Hello! How can I assist you today?']],
    ['(what is your name?)', ['I am a simple Python chatbot.']],
    ['(how are you?)', ['I am just a bunch of code, but thanks for asking!']],
    ['(.*) help (.*)', ['Sure! How can I help you with %2?']],
    ['(bye|exit)', ['Goodbye! Have a great day!']]
]
print("hello , welcome to JetBot , lets start !!!")
chatbot = Chat(pairs, reflections)
print("Chat with the bot (type 'bye' to exit)")
chatbot.converse()