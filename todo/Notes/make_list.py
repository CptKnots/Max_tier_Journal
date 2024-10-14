
kingdom = ["1", "two"]
    
def update_kingdom(new_sector):
    global kingdom
    kingdom.extend(new_sector)
    return kingdom







# make_list.py

# Dictionary to store species and their kingdoms
kingdom_dict = {}

# Function to update the kingdom
def update_kingdom(species):
    # Check if the species is already in the dictionary
    if species in kingdom_dict:
        updated_kingdom = kingdom_dict[species]
    else:
        # If species is not in the dictionary, prompt for a new kingdom
        new_kingdom = input(f"Enter kingdom for {species}: ")
        kingdom_dict[species] = new_kingdom
        updated_kingdom = new_kingdom
    return updated_kingdom




