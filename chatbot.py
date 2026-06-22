# ========================================
# MOVIE DATA
# ========================================

movies = {
    "action": {
        "description": "Fast-paced movies with fights and adventure.",
        "examples": ["John Wick", "Mad Max: Fury Road", "The Dark Knight"]
    },

    "comedy": {
        "description": "Movies that make you laugh.",
        "examples": ["The Mask", "Home Alone", "Rush Hour"]
    },

    "horror": {
        "description": "Scary movies with suspense and fear.",
        "examples": ["The Conjuring", "Insidious", "IT"]
    },

    "science fiction": {
        "description": "Movies based on future technology and space.",
        "examples": ["Interstellar", "The Matrix", "Avatar"]
    }
}

# ========================================
# GENERAL RESPONSES
# ========================================

responses = {
    "hello": "Hi! Welcome to MovieBot.",
    "hi": "Hello!",
    "how are you": "I am doing great.",
    "help": "Type movie genres like action, comedy, horror, or science fiction.",
    "bye": "Goodbye!"
}

# ========================================
# WELCOME SCREEN
# ========================================

print("=" * 50)
print("🎬 MovieBot - Movie Recommendation Chatbot")
print("=" * 50)
print("Type 'genres' to see available genres")
print("Type 'help' for commands")
print("Type 'exit' to quit")

# ========================================
# MAIN LOOP
# ========================================

while True:

    user_input = input("\nYou: ").lower().strip()

    if user_input == "exit":
        print("MovieBot: Goodbye!")
        break

    if user_input == "genres":
        print("\nAvailable Genres:")
        for genre in movies:
            print("-", genre.title())
        continue

    if user_input in movies:

        movie = movies[user_input]

        print("\n🎥 Genre:", user_input.title())
        print("Description:", movie["description"])

        print("\nRecommended Movies:")
        for m in movie["examples"]:
            print("-", m)

        continue

    print("MovieBot:",
          responses.get(
              user_input,
              "Sorry, I don't understand. Type 'genres' to see options."
          ))
