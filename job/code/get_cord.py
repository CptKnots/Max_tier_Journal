import requests
import math

# Function to get coordinates from postal code using Google Geocoding API
def get_coordinates(api_key, postal_code):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": postal_code,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print(f"Error: {data['status']}")
            return None
    else:
        print(f"HTTP Error: {response.status_code}")
        return None

# Function to calculate distance using Haversine formula
def calculate_distance(coord1, coord2):
    # Radius of Earth in kilometers and miles
    R_km = 6371.0  # kilometers
    R_miles = 3958.8  # miles

    lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
    lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance_km = R_km * c
    distance_miles = R_miles * c

    return distance_km, distance_miles

def main():
    # Replace with your Google Maps Geocoding API key
    api_key = 'YOUR_API_KEY_HERE'

    # Input up to two postal codes
    postal_codes = []
    for i in range(2):
        postal_code = input(f"Enter postal code {i + 1} (or press Enter to skip): ")
        if postal_code:
            postal_codes.append(postal_code)
        else:
            break

    if len(postal_codes) < 1:
        print("No postal codes entered. Exiting.")
        return

    # Get and display coordinates for each postal code
    coordinates = []
    for postal_code in postal_codes:
        coord = get_coordinates(api_key, postal_code)
        if coord:
            print(f"Coordinates for {postal_code}: Latitude {coord[0]}, Longitude {coord[1]}")
            coordinates.append(coord)
        else:
            print(f"Could not retrieve coordinates for {postal_code}.")

    # Calculate and display the distance if two postal codes were entered
    if len(coordinates) == 2:
        distance_km, distance_miles = calculate_distance(coordinates[0], coordinates[1])
        print(f"Distance between {postal_codes[0]} and {postal_codes[1]}: {distance_km:.2f} km ({distance_miles:.2f} miles)")

if __name__ == "__main__":
    main()
