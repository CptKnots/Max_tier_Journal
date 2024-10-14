import random

# Define available boost categories and options
boosts = {
    "snacks": ["fruit", "chocolate", "nuts", "protein bar"],
    "drinks": ["water", "smoothie", "coffee", "green tea"],
    "sleep": ["nap", "full night's sleep", "restful break"],
    "entertainment": ["watch a movie", "read a book", "play a video game", "go for a walk"]
}

# Function to generate boost based on mood and HP
def generate_boost(mood, hp):
    boost_category = ""
    boost_type = ""
    
    # Logic for boost based on mood and HP
    if mood == "low":
        # When mood is low, higher HP triggers smaller boosts
        if hp < 50:
            boost_category = "sleep"
        elif 50 <= hp < 70:
            boost_category = "entertainment"
        else:
            boost_category = "snacks"
    
    elif mood == "medium":
        if hp < 50:
            boost_category = "sleep"
        elif 50 <= hp < 70:
            boost_category = "drinks"
        else:
            boost_category = "entertainment"
    
    elif mood == "high":
        if hp < 50:
            boost_category = "snacks"
        elif 50 <= hp < 70:
            boost_category = "drinks"
        else:
            boost_category = "entertainment"
    
    # Randomly select a specific boost from the chosen category
    if boost_category:
        boost_type = random.choice(boosts[boost_category])

    return f"Your boost is: {boost_type} from the category: {boost_category}"

# Example use
mood = input("Enter your mood (low, medium, high): ").lower()
hp = int(input("Enter your HP (0-100): "))

boost = generate_boost(mood, hp)
print(boost)
