import nltk
from nltk.chat.util import Chat, reflections

set_pairs = [

    [

        r"my name is (.*)",

        ["Hello %1, How are you doing today ?",]

    ],

    [

        r"hi|hey|hello",

        ["Hello", "Hey there",]

    ], 

    [

        r"what is your name?",

        ["You can call me lipton ",]

    ],

    [

        r"how are you ?",

        ["I am fine, thank you! How can i help you?",]

    ],
    [
        r"how old are you ?",

        ["Sorry I cannot tell you my age"]
    ],
    [
        r"how're you doing ? ",

        ["I am doing great and you ?"]
    ],

    [

        r"I am fine, thank you",

        ["great to hear that, how can i help you?",]

    ],

    [

        r"how can i help you? ",

        ["i am looking for online guides and courses to learn data science, can you suggest?", "i am looking for data science training platforms",]

    ],

    [

        r"i'm (.*) doing good",

        ["That's great to hear","How can i help you?:)",]

    ],

    [

        r"i am looking for online guides and courses to learn data science, can you suggest?",

        ["Pluralsight is a great option to learn data science. You can check their website",]

    ],

    [

        r"thanks for the suggestion. do they have great authors and instructors?",

        ["Yes, they have the world class best authors, that is their strength;)",]

    ],

    [

        r"(.*) thank you so much, that was helpful",

        ["Iam happy to help", "No problem, you're welcome",]

    ],

    [
        r"Why ?",

        [ "It is confidential "]
    ]

    [

        r"quit",

    ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]

],

]

def chatbot():
    print('Hi,My name is lipton')

chatbot()

chat = Chat(set_pairs,reflections)


chat.converse()
if __name__ == "__main__":
    chatbot()