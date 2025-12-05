import json

filename = "students.json"   

with open(filename, "r") as st_json:
    st = json.load(st_json)

print(st)


import requests
from datetime import datetime

API_KEY = "1bcbc860f13f3eac55eab1924cfa2139"

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.json().get('message', 'Unable to fetch data')}")
        return

    data = response.json()
    
    # Extract main data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    
    # Weather description
    weather_description = data["weather"][0]["description"].title()
    
    # Wind info
    wind_speed = data["wind"]["speed"]
    
    # Sunrise and Sunset times
    sunrise = datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"]).strftime('%H:%M:%S')
    sunset = datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"]).strftime('%H:%M:%S')
    
    # Print nicely
    print(f"\n🌤 Weather in {city.title()}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Weather: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Sunrise: {sunrise}")
    print(f"Sunset: {sunset}\n")

def main():
    while True:
        city = input("Enter a city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        elif city == "":
            print("Please enter a valid city name.")
        else:
            get_weather(city)

if __name__ == "__main__":
    main()



import json
import os

FILE = "books.json"

def load_data():
    if not os.path.exists(FILE):
        return {"books": []}  
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_book():
    data = load_data()
    
    new_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    data["books"].append({
        "id": new_id,
        "title": title,
        "author": author
    })

    save_data(data)
    print("Book added successfully!")

def update_book():
    data = load_data()
    book_id = int(input("Enter the ID of the book to update: "))

    for book in data["books"]:
        if book["id"] == book_id:
            print("Leave empty if you don't want to change it.")
            new_title = input("New title: ")
            new_author = input("New author: ")

            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author

            save_data(data)
            print("Book updated!")
            return
    
    print("Book with that ID was not found.")

def delete_book():
    data = load_data()
    book_id = int(input("Enter the ID of the book to delete: "))

    original_length = len(data["books"])
    data["books"] = [book for book in data["books"] if book["id"] != book_id]

    if len(data["books"]) < original_length:
        save_data(data)
        print("Book deleted!")
    else:
        print("No book with that ID found.")

def menu():
    while True:
        print("\n--- Book Manager ---")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

menu()


import requests
import random

API_KEY = "e67bbb79"

def get_movies_by_genre(genre):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&type=movie&s={genre}"

    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error: Unable to fetch data.")
        return None
    
    data = response.json()

    if "Search" not in data:
        return None
    
    return data["Search"]

def get_movie_details(imdb_id):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&i={imdb_id}&plot=full"
    response = requests.get(url)
    return response.json()

def recommend_movie():
    while True:
        genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ").strip()

        if not genre:
            print("Please enter a genre.")
            continue

        movies = get_movies_by_genre(genre)

        if not movies:
            print(f"No movies found for genre '{genre}'. Please try again.\n")
            continue

        movie = random.choice(movies)
        details = get_movie_details(movie["imdbID"])

        print("\n🎬 Recommended Movie:")
        print(f"Title: {details.get('Title')}")
        print(f"Year: {details.get('Year')}")
        print(f"Genre: {details.get('Genre')}")
        print(f"IMDB Rating: {details.get('imdbRating')}")
        print(f"Plot: {details.get('Plot')}\n")
        break  # exit the loop after showing a recommendation

recommend_movie()
