import json
import requests

def get_restaurants(city_name, api_key):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    query = f"top restaurants in {city_name}"
    params = {
        'query': query,
        'key': api_key,
        'type': 'restaurant',
        'rating': 'rating'
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code} from the API")
        return {}
    print("API Response:", response.json())
    restaurants = response.json().get('results', [])
    if not restaurants:
        print(f"No restaurants found for {city_name}.")
        return {}
    restaurant_data = {}
    for restaurant in restaurants[:10]:  # Get top 10
        name = restaurant['name']
        rating = restaurant.get('rating', 'N/A')
        reviews = restaurant.get('user_ratings_total', 'No reviews')
        restaurant_data[name] = {
            'rating': rating,
            'reviews': reviews
        }

    return restaurant_data

def save_to_json(data, filename='top_restaurants.json'):
    if data:
        print("Saving the following data to JSON:")
        print(data)  # Print data for verification
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

def main():
    #enter a city name
    city_name = input("Enter the name of a city: ")

    # Replace with your Google Places API Key
    api_key = 'AIzaSyBi6V2z6mrwtKZrAaieBI3C2QjuqLTJkKY'

    # Get restaurant data
    restaurant_data = get_restaurants(city_name, api_key)

    # Save the restaurant data to a JSON file
    save_to_json(restaurant_data)

if __name__ == "__main__":
    main()
