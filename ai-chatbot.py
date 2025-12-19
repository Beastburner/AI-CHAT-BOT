# import useful libraries
import random
import datetime
import re

# chatbot name
BOT_NAME = "Lazycook"

# memory
user_name = None
last_weather_response = None


# responses
user_preferences = {
    "likes_jokes": True,
    "likes_motivation": True
    
}

joke_reaction_count = 0

positive_joke_reactions = [
    "wow",
    "nice",
    "nice joke",
    "haha",
    "lol",
    "funny",
    "another",
    "another one",
    "more",
    "good one"
]

motivation_reaction_count = 0

positive_motivation_reactions = [
    "that helped",
    "thanks",
    "thank you",
    "feeling better",
    "this helped",
    "motivated",
    "motivation",
    "encouraging",
    "needed this"
]

greetings = [
    "Hello, how can I help you today?",
    "Hey there! What’s up?",
    "Hi! Need any assistance?"
]

help_responses = [
    "I can help you with general questions.",
    "I can tell you jokes, the time, and talk about the weather!",
    "Ask me anything—I'm here 😄"
]

bored_responses = [
    "Feeling bored? Want a joke or a random fact?",
    "You could try learning something new or coding something fun 💻",
    "Boredom is creativity waiting to happen ✨"
]

mood_responses = {
    "happy": [
        "That's awesome! Keep smiling 😊",
        "Love that energy 😄"
    ],
    "sad": [
        "I'm sorry you're feeling sad 😞 Want to talk about it?",
        "It's okay to feel down sometimes 💙"
    ],
    "angry": [
        "Take a deep breath 😤 I'm here to help.",
        "Want to vent? I’m listening."
    ],
    "tired": [
        "Sounds like you need some rest 😴",
        "Maybe take a short break or grab some water 💧"
    ]
}

random_responses = [
    "Fun fact: Honey never spoils 🍯",
    "Random thought: Code is poetry.",
    "Did you know octopuses have three hearts? 🐙"
]

weather_keywords = [
    "weather", "temperature", "rain", "sunny",
    "hot", "cold", "forecast"
]

jokes = [
    "Why don’t programmers like nature? Too many bugs.",
    "Why did the computer go to the doctor? Because it caught a virus.",
    "Why do Python programmers prefer dark mode? Because light attracts bugs."
]


# response function
def chatty_response(user_input):
    global user_name, last_weather_response
    user_input = user_input.lower()
    global joke_reaction_count
    global motivation_reaction_count


    # ---- NAME MEMORY ----
    name_match = re.search(r"(my name is|i am|call me)\s+(\w+)", user_input)
    if name_match:
        user_name = name_match.group(2).capitalize()
        return f"Nice to meet you, {user_name}! 😊"

    if "my name" in user_input and user_name:
        return f"Your name is {user_name}!"

    # ---- GREETINGS ----
    if any(word in user_input for word in ["hi", "hello", "hey", "wassup"]):
        if user_name:
            return f"Hey {user_name}! {random.choice(greetings)}"
        return random.choice(greetings)

    # ---- BOT NAME ----
    if "your name" in user_input:
        return f"My name is {BOT_NAME} 🤖"

    # ---- MOOD DETECTION ----
    for mood in mood_responses:
        if mood in user_input:
            return random.choice(mood_responses[mood])

    # ---- BORED ----
    if any(word in user_input for word in ["bored", "boring"]):
        return random.choice(bored_responses)
    if user_preferences["likes_motivation"] and "sad" in user_input:
     return "I know things are tough right now, but you’re stronger than you think 💪"
    if user_preferences["likes_motivation"] and "bored" in user_input:
     return "How about setting a small goal right now? Tiny wins matter 🚀"



    # ---- HELP ----
    if any(word in user_input for word in ["help", "assist", "support"]):
        return random.choice(help_responses)

    # ---- JOKES ----
    if any(word in user_input for word in ["joke", "jokes", "funny"]):
        return random.choice(jokes)
    if user_preferences["likes_jokes"] and "bored" in user_input:
      return random.choice(jokes)

    # --- Detect positive reaction to motivation ---
    if any(word in user_input for word in positive_motivation_reactions):
        motivation_reaction_count += 1

        if motivation_reaction_count >= 2:
            user_preferences["likes_motivation"] = True
            return "I’m glad it helped 💙 I’ll motivate you more when needed."

        return "Happy to help 💪 You’ve got this!" 
    # ---- WEATHER (non-repeating) ----
    if any(word in user_input for word in weather_keywords):
        weather_responses = [
            "I can't check live weather, but be prepared ☔",
            "Hope the weather is nice where you are 🌤️",
            "Hot or cold—stay comfortable 🧥💧"
        ]

        response = random.choice(weather_responses)
        while response == last_weather_response:
            response = random.choice(weather_responses)

        last_weather_response = response
        return response

    # ---- TIME ----
    if "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time} ⏰"
     # --- Detect positive reaction to jokes ---
    if any(word in user_input for word in positive_joke_reactions):
       joke_reaction_count += 1

       if joke_reaction_count >= 2:
          user_preferences["likes_jokes"] = True
          return "Seems like you enjoy jokes 😄 I’ll remember that!"

       return "Glad you liked it 😄 Want another one?"


    # ---- RANDOM ----
    if "random" in user_input:
        return random.choice(random_responses)

    return "I'm not sure about that 🤔 Try asking something else!"


# main chatbot loop
def chatbot():
    print(f"Hello! I am {BOT_NAME}. How can I help you today?")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print(f"{BOT_NAME}: Goodbye! Have a great day 👋")
            break

        print(f"{BOT_NAME}:", chatty_response(user_input))


# run chatbot
if __name__ == "__main__":
    chatbot()
