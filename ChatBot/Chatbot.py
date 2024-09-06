import re

PatternsResponses = {
    r"hello|hi|hey": "Hello! How can I help you today?",
    r"how are you": "I'm just a chatbot, but I'm doing great! How about you?",
    r"your name|who are you": "I'm a chatbot and my name is Pal! created to assist you with your queries.",
    r"what can you do": "I can answer your questions and provide information. Try asking me something!",
    r"bye|goodbye": "Goodbye! Have a great day!",
    r"weather": "I'm not connected to a weather service, but it's always a good idea to check a weather app!",
    r"time": "I can't tell the exact time, but it's always a good time to ask questions!",
    r"thank you|thanks": "You're welcome! If you have more questions, feel free to ask.",
    r"what's up|sup": "Not much! Just here to help you out. What's up with you?",
    r"help": "Sure, I'm here to help! What do you need assistance with?",
    r"how old are you": "I don't have an age, but I was created to assist you with your queries.",
    r"where are you from": "I exist in the digital world, created to assist you wherever you are.",
    r"who created you": "I was created by a Developer named Poagesh N.",
    r"tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    r"tell me a fun fact": "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
    r"do you like music": "I don't have preferences, but music is fascinating! What kind of music do you like?",
    r"what's your favorite color": "I don't have a favorite color, but I can tell you about colors if you're interested!",
    r"do you have any hobbies": "I don't have hobbies, but I'm here to help you with your queries!",
    r"what's your purpose": "My purpose is to assist you with your questions and provide information.",
    r"do you have friends": "I interact with many users like you, so you could say I have many friends!",
    r"what's the meaning of life": "That's a deep question! Many believe it's to seek happiness and fulfillment.",
    r"do you believe in aliens": "There are many theories about the existence of aliens. What do you think?",
    r"what's your favorite movie": "I don't watch movies, but I can help you find information about any movie!",
    r"can you dance": "I can't dance, but I can help you find some great dance tutorials online!",
    r"what's your favorite book": "I don't read books, but I can help you find information about any book!",
    r"do you sleep": "I don't need sleep. I'm always here to assist you!",
    r"do you eat": "I don't need food, but I can help you find great recipes!",
    r"what's your favorite food": "I don't eat, but I can help you find recipes for any dish you like!",
    r"what's your favorite sport": "I don't play sports, but I can help you find information about any sport!",
    r"do you have a family": "I don't have a family, but I'm here to assist you like a friend.",
    r"what's the best programming language": "The best programming language depends on the task at hand. Python is popular for its simplicity and versatility.",
    r"what's the capital of France": "The capital of France is Paris.",
    r"what's the largest planet": "The largest planet in our solar system is Jupiter.",
    r"what's the speed of light": "The speed of light is approximately 299,792,458 meters per second.",
    r"what's the tallest mountain": "The tallest mountain on Earth is Mount Everest.",
    r"who painted the Mona Lisa": "The Mona Lisa was painted by Leonardo da Vinci.",
    r"what's the square root of 64": "The square root of 64 is 8.",
    r"how many continents are there": "There are seven continents on Earth.",
    r"what's the smallest country": "The smallest country in the world is Vatican City.",
    r"what's the longest river": "The longest river in the world is the Nile River.",
    r"what's the largest ocean": "The largest ocean on Earth is the Pacific Ocean.",
    r"who invented the telephone": "The telephone was invented by Alexander Graham Bell.",
    r"what's the currency of Japan": "The currency of Japan is the Japanese Yen.",
    r"what's the chemical symbol for gold": "The chemical symbol for gold is Au.",
    r"who discovered penicillin": "Penicillin was discovered by Alexander Fleming.",
    r"what's the main ingredient in bread": "The main ingredient in bread is flour.",
    r"how many planets are in the solar system": "There are eight planets in the solar system.",
    r"who wrote 'Hamlet'": "'Hamlet' was written by William Shakespeare.",
    r"what's the largest desert": "The largest desert in the world is the Sahara Desert.",
    r"who developed the theory of relativity": "The theory of relativity was developed by Albert Einstein.",
    r"what's the boiling point of water": "The boiling point of water is 100 degrees Celsius (212 degrees Fahrenheit) at sea level.",
    r"what's the capital of Japan": "The capital of Japan is Tokyo.",
    r"what's the heaviest naturally occurring element": "The heaviest naturally occurring element is uranium.",
    r"what's the freezing point of water": "The freezing point of water is 0 degrees Celsius (32 degrees Fahrenheit).",
    r"what's the most common gas in the Earth's atmosphere": "The most common gas in the Earth's atmosphere is nitrogen.",
    r"what's the most abundant element in the universe": "The most abundant element in the universe is hydrogen.",
    r"who is known as the 'Father of Computers'": "Charles Babbage is known as the 'Father of Computers'.",
    r"what's the largest animal": "The largest animal is the blue whale.",
    r"who discovered gravity": "Sir Isaac Newton is credited with the discovery of gravity.",
    r"what's the largest continent": "The largest continent is Asia.",
    r"what's the most populous country": "The most populous country is China.",
    r"what's the fastest land animal": "The fastest land animal is the cheetah.",
    r"what's the capital of Australia": "The capital of Australia is Canberra.",
    r"what's the hardest natural substance": "The hardest natural substance is diamond.",
    r"who invented the light bulb": "The light bulb was invented by Thomas Edison.",
    r"what's the longest bone in the human body": "The longest bone in the human body is the femur.",
    r"what's the largest organ in the human body": "The largest organ in the human body is the skin.",
    r"what's the tallest building": "As of now, the tallest building in the world is the Burj Khalifa in Dubai.",
    r"who painted 'Starry Night'": "'Starry Night' was painted by Vincent van Gogh.",
    r"what's the capital of Russia": "The capital of Russia is Moscow.",
    r"who invented the airplane": "The airplane was invented by the Wright brothers, Orville and Wilbur Wright.",
    r"what's the chemical symbol for water": "The chemical symbol for water is H2O.",
    r"what's the smallest bone in the human body": "The smallest bone in the human body is the stapes, located in the ear.",
}

def ChatBotResponse(UserInput):
    UserInput = UserInput.lower()
    for pattern, response in PatternsResponses.items():
        if re.search(pattern, UserInput):
            return response
    return "I'm sorry, I don't understand that. Can you please rephrase?"


def Chat():
    print("Welcome to the Chatbot named Pal. say 'Exit' to end the conversation.")
    while True:
        UserInput = input("You:")
        if UserInput.lower() == "exit":
            print("Pal: -----Chat Ended-----")
            break
        else:
            response = ChatBotResponse(UserInput)
            print(f"Pal: {response}")
        

Chat()
