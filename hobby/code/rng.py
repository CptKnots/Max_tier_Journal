import random

def get_fruit_by_color(color):
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    
    # Output the random number for context
    print(f"Random number generated: {random_number}")
    
    # Logic to select fruit based on color and number
    if color == "blue":
        if random_number % 2 == 0:
            return "Grapes"
        else:
            return "Apple"
    elif color == "red":
        if random_number % 2 == 0:
            return "Pear"
        else:
            return "Orange"
    elif color == "yellow":
        if random_number % 2 == 0:
            return "Orange"
        else:
            return "Grapes"
    else:
        return "Invalid color. Please choose blue, red, or yellow."

# Example usage
favorite_color = input("Enter your favorite color (blue, red, or yellow): ").lower()
fruit = get_fruit_by_color(favorite_color)
print(f"You should eat: {fruit}")
