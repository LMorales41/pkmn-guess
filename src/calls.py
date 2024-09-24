import requests
import random

class Pokemon:
    def __init__(self, arr):
        self.answer = arr[0]
        self.hintList = arr[1]
        self.gen = arr[2]

    def __str__(self):
        return f"Pokemon Name: {self.answer}\n Hints: {self.hintList}\n Gen: {self.gen}\n"
    
    def show_info(self, guesses):
        print("Currently known: ")
        print("Pokemon is from generation: " + self.gen)
        for i in range(guesses):
            print(self.hintList[i])

    
    def show_all_info():
        print(answer)
        print(hintList)
        print(gen)

    
    


def hello_world():
    print("Hello World")

def get_posts():
    # Define the API endpoint URL
    url = 'https://pokeapi.co/api/v2/pokemon-species/0/'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except Exception as e:
        print('An error occurred:', e)


def get_dex_number():
    return random.randrange(1, 1025)

def get_pokemon_info(number):
    #print (number)
    url = f'https://pokeapi.co/api/v2/pokemon-species/{number}/'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            #hintList = posts[]
            #returnedPokemon = Pokemon(posts["name"],posts[],posts[])
            #print(posts["color"]["name"])
            return posts["name"], posts["color"]["name"], posts["generation"]["name"]
        else:
            print('Error at calling get_pokemon_info:', response.status_code)
            return None
    except Exception as e:
        print('An error occurred at calling get_pokemon_info:', e)

def pokemon_constructor(name, color, gen):
    # print (number)
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            abilityList = []
            typeList = []
            for x in posts["abilities"]:
                abilityList.append(x["ability"]["name"])

            for x in posts["types"]:
                typeList.append(x["type"]["name"])

            hintList = [typeList, abilityList, color, name[0]]
            
            return name, hintList, gen
        else:
            print('Error at calling pokemon_constructor:', response.status_code)
            return None
    except Exception as e:
        print('An error occurred at calling pokemon_constructor:', e)

