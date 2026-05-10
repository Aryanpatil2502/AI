import nltk
from nltk.chat.util import Chat, reflections

nltk.download('punkt')

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! Welcome to our store."]
    ],

    [
        r"what is your name ?",
        ["I am a customer support chatbot."]
    ],

    [
        r"how can i track my order ?",
        ["You can track your order from the 'My Orders' section."]
    ],

    [
        r"what payment methods do you accept ?",
        ["We accept Credit Card, Debit Card, UPI, and Net Banking."]
    ],

    [
        r"how to return a product ?",
        ["Go to 'My Orders' and click on Return Product."]
    ],

    [
        r"bye|exit",
        ["Thank you for visiting. Goodbye!"]
    ]
]

chatbot = Chat(pairs, reflections)

print("Customer Support Chatbot")
print("Type 'bye' to exit\n")

chatbot.converse()
