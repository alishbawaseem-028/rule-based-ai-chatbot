# ================================================
# PROJECT 1: RULE-BASED AI CHATBOT
# DecodeLabs Industrial Training Kit - Batch 2026
# ================================================

# Knowledge Base using Dictionary (Hash Map)
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What's going on?",
    "how are you": "I'm functioning perfectly. How about you?",
    "what is your name": "I'm DecodeBot, your rule-based AI assistant from DecodeLabs.",
    "who are you": "I'm a Rule-Based Chatbot developed for DecodeLabs AI Training Program.",
    "thank you": "You're very welcome.",
    "thanks": "My pleasure.",
    "good morning": "Good morning! Wishing you a great day ahead.",
    "good evening": "Good evening! Hope you're having a wonderful day.",
    "good night": "Good night! Sweet dreams.",
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs.",
    "weather": "I can't check real weather yet, but in the world of code it's always sunny with a chance of bugs.",
    "bye": "Goodbye! Have a fantastic day.",
    "goodbye": "Goodbye! It was nice chatting with you.",
    "exit": "Goodbye! See you next time.",
    "quit": "Goodbye! See you next time."
}

print("DecodeBot: Hello! I am DecodeBot - a Rule-Based AI Chatbot.")
print("Type 'exit', 'quit', 'bye' or 'goodbye' to end the conversation.\n")

# Algorithmic Efficiency Demonstration
print("=" * 60)
print("ALGORITHMIC EFFICIENCY (Dictionary vs If-Elif Ladder)")
print("=" * 60)
print("Dictionary (Hash Map)  : Constant time lookup - O(1)")
print("If-Elif Ladder         : Linear time lookup - O(n)")
print("→ Dictionary is used for better performance and scalability.")
print("=" * 60 + "\n")

while True:
    # Input & Sanitization
    user_input = input("You: ").strip()
    clean_input = user_input.lower()
    
    # Exit Strategy
    if clean_input in ["exit", "quit", "bye", "goodbye"]:
        print("DecodeBot: Goodbye! Keep mastering AI.")
        break
    
    # Hybrid Architecture Logic
    reply = responses.get(clean_input)
    
    if reply:
        # Rule Match - Instant Response
        print(f"DecodeBot: {reply}")
    else:
        # No Rule Match - Simulate passing to LLM
        print("DecodeBot: I don't have a predefined rule for that.")
        print("   → Would pass to LLM for generative response (Hybrid Architecture)")
        
        # Additional Smart Logic (Nested Conditions)
        if "how" in clean_input:
            print("DecodeBot: I'm great at following rules. What would you like to know?")
        elif any(word in clean_input for word in ["age", "old", "born", "created"]):
            print("DecodeBot: I was created as part of this training project.")
        else:
            print("DecodeBot: Try asking me my name, a joke, or say hello.")

print("\n" + "=" * 60)
print("Project 1 Completed Successfully!")
print("Features Implemented:")
print("- Continuous Input Loop")
print("- Input Sanitization")
print("- Dictionary-based Knowledge Base")
print("- Hybrid Architecture Concept")
print("- Clean Exit Strategy")
print("=" * 60)