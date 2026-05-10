import nltk
from nltk.chat.util import Chat, reflections

# Download tokenizer only once
# nltk.download('punkt')

pairs = [

    # Greetings
    [
        r"(?i).*\b(hi|hello|hey|hola)\b.*",
        [
            "Hello! Welcome to our store.",
            "Hi there! How can I help you today?",
            "Hey! Need any assistance?"
        ]
    ],

    # Name
    [
        r"(?i).*(your name|who are you).*",
        [
            "I am a customer support chatbot.",
            "You can call me StoreBot."
        ]
    ],

    # Order tracking
    [
        r"(?i).*(track|tracking|order status).*",
        [
            "You can track your order from the 'My Orders' section.",
            "Open 'My Orders' to check your delivery status."
        ]
    ],

    # Payment methods
    [
        r"(?i).*(payment|pay|upi|card|net banking).*",
        [
            "We accept Credit Card, Debit Card, UPI, and Net Banking."
        ]
    ],

    # Return product
    [
        r"(?i).*(return|refund|replace).*",
        [
            "Go to 'My Orders' and click on 'Return Product'.",
            "You can request a refund from the orders section."
        ]
    ],

    # Delivery
    [
        r"(?i).*(delivery|shipping|arrive).*",
        [
            "Delivery usually takes 3-5 business days."
        ]
    ],

    # Thanks
    [
        r"(?i).*\b(thanks|thank you)\b.*",
        [
            "You're welcome!",
            "Happy to help!"
        ]
    ],

    # Exit
    [
        r"(?i).*\b(bye|exit|quit)\b.*",
        [
            "Thank you for visiting. Goodbye!",
            "Have a great day!"
        ]
    ],

    # Fallback response
    [
        r"(.*)",
        [
            "Sorry, I didn't understand that.",
            "Could you please rephrase your question?",
            "I am still learning. Try asking something else."
        ]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

print("=" * 50)
print("      CUSTOMER SUPPORT CHATBOT")
print("=" * 50)
print("Type 'bye' to exit.\n")

# Start conversation
chatbot.converse()
