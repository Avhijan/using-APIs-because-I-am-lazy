import random
import requests
import difflib
import io
from PIL import Image #to display the pokemon's image

#limit=100000 makes sure we get every pokemon in the list, not just the default first 20
url = "https://pokeapi.co/api/v2/pokemon/?limit=100000"

response = requests.get(url)
print(response) #check status code

data = response.json()
results = data['results']

#select random pokemon
random_pokemon = random.choice(results)

#save pokemon name
pokemon = random_pokemon['name']

#save pokemon api
pokemon_api = random_pokemon['url']

#get pokemon details
response = requests.get(pokemon_api)
data = response.json()

pokemon_type = data['types'][0]['type']['name']



#save url to the image of pokenmon
sprite_url = data['sprites']['front_default']


# Hints
#getting extra hint info from the species endpoint
#the main 'pokemon' endpoint doesn't have any interesting hints, moves, exp, stats and other boring things
# we can insted use a different api endpoint pokemon-species
#---------------------------------------------------------------------
species_url = data['species']['url']
species_response = requests.get(species_url)
species_data = species_response.json()

#flavor_text_entries contains same description in a lot of languages, so we need to find english description
flavor_text = None
for entry in species_data['flavor_text_entries']:
    if entry['language']['name'] == 'en':
        #the flavor text from the api often has weird line break
        #replacing the characters like \n and \x0c
        flavor_text = entry['flavor_text'].replace('\n', ' ').replace('\x0c', ' ')
        break 

#habitat can be missing (None) for some pokemon
if species_data['habitat'] is not None:
    habitat = species_data['habitat']['name']
else:
    habitat = None

#color 
color = species_data['color']['name']


#building a list of hints after filtering missing values like missing habitats
hints = []
if flavor_text:
    hints.append(f"Pokedex entry: {flavor_text}")
if habitat:
    hints.append(f"Habitat: {habitat}")
hints.append(f"Color: {color}") #color is reliable because its always presetn

tries = 3

print('You have 3 tries to guess your pokemon correctly')
print(f"Your pokemon's type is {pokemon_type}")

hint_index = 0 #keeps track of which hint to reveal next

while tries > 0:
    print("Your guess:")
    guess = input().strip().lower() # removes extra spaces and ignores case

    #difflib.get_close_matches compares 'guess' with a list containing just the answer
    #cutoff=0.8 means needs to be 80% similar 
    close_match = difflib.get_close_matches(guess, [pokemon], cutoff=0.8)

    if guess == pokemon or close_match: # exact match OR a misspelled

        if guess != pokemon:
            print(f"Close enough! The pokemon was {pokemon}")

        if tries == 3:
            print("Impressive guess and on your first try too, well played")
        else:
            print("Correct Guess!!!")

        print("------------------------------------------------------")
        break #end if win

    else:
        tries -= 1
        print(f'Incorrect!!! you have {tries} tries left.')

        #new hint after each wrong guess
        if hint_index < len(hints) and tries > 0:
            print(hints[hint_index])
            hint_index += 1

        if tries == 0:
            print(f"You have used up all your tries the pokemon was {pokemon}")

        print("------------------------------------------------------")

#final image reveal, this runs whether the player won or lost
#requests.get(sprite_url).content grabs the raw image bytes from the url
#io.BytesIO wraps those bytes so PIL can treat them like a file
#Image.open() reads it into an image object, .show() opens it default image viewer
if sprite_url: #some pokemon may not have a sprite, so we need to check first
    image_bytes = requests.get(sprite_url).content
    image = Image.open(io.BytesIO(image_bytes))

    #zooming because sprites are smoll
    zoom = 4
    new_size = (image.size[0] * zoom, image.size[1] * zoom)

    #resample=Image.NEAREST keeps the pixel edges hard/crisp instead of blurring
    image = image.resize(new_size, resample=Image.NEAREST)

    image.show()