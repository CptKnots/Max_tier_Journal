from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def get_coordinates(address):
    # 
    # Initialize Nominatim API to convert an address into latitude and longitude
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    # Geocode the input address to get latitude and longitude
    location = geolocator.geocode(address)
    
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Could not geocode the address: {address}")

def calculate_distance(address1, address2):
    # Get the coordinates of the two addresses
    coords_1 = get_coordinates(address1)
    coords_2 = get_coordinates(address2)
    
    # Calculate the distance between the two coordinates in km and miles
    distance_km = geodesic(coords_1, coords_2).kilometers
    distance_miles = geodesic(coords_1, coords_2).miles
    
    return distance_km, distance_miles

if __name__ == "__main__":
    # Take two addresses as input from the user
    address_1 = input("Enter the first address: ")
    address_2 = input("Enter the second address: ")
    
    try:
        # Calculate the distance between the two addresses
        distance_km, distance_miles = calculate_distance(address_1, address_2)
        
        # Display the results
        print(f"Distance between the addresses:")
        print(f"In kilometers: {distance_km:.2f} km")
        print(f"In miles: {distance_miles:.2f} miles")
        
    except ValueError as e:
        print(e)
