import requests

# Function to fetch a random joke from the API and print it
def get_joke():
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()

    print("\nHere's a joke for you: ")
    print(joke_data["setup"])
    print(joke_data["punchline"])

# Fetch and display the first joke before entering the loop
get_joke()

# Ask the user if they want more jokes
answer = input("Would you like another joke? :)").lower()

# Continue fetching jokes as long as the user responds 'yes'
while answer == "yes":
    get_joke()
    answer = input("Would you like another joke? :)").lower()