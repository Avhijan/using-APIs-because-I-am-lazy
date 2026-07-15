# **Pokemon Type Guesser**

This program uses the PokeAPI and python's requests, random, difflib and PIL libraries to run a guessing game where you're given a random pokemon's type and hints, and have to guess the pokemon.

This project explores the actual use of API endpoints where we don't just display a random cat fact or an anime name as a reult but rather add functionalites to the endpoints. In this case I have made a game where we can guess a pokemon while hints are being delivered. Calling this a proper usecase for APIs would be a stretch.

## **Table of Contents**
- [API used](#api-used)
- [Dependency](#dependency)
- [Code explanation](#code-explanation)

## **API used**
For this project I used two pokemon APIs to get details about the pokemon, its image and hints for guess.
[https://pokeapi.co/api/v2/pokemon/](https://pokeapi.co/api/v2/pokemon/)
[https://pokeapi.co/api/v2/pokemon-species/](https://pokeapi.co/api/v2/pokemon-species/)

The main pokemon endpoint has stuff like type, height, weight and sprites, but doesn't have flavor text, habitat or colour. However except for colour there is nothing good to use as hints. Instead I used the endpoint called pokemon-species, which every pokemon links to.

## **Dependency**
This project uses requests and random, both covered already. If you are interested:
[Cat Fact Generator](../01_cat_fact_generator/README.md)
[Random Anime Suggestor](../02_anime_suggestor/README.md)

**difflib**

We can't expect everyone to know the spelling of all the pokemons. At best, most people would recognize pickachu and proceed to spell it "pikacho". In fact I had to google it myself just now to make sure so we need a way to ignore spelling erros or typos.

difflib is an inbuilt python library used for comparing sequences, most commonly strings. Here we used it for fuzzy/typo tolerant matching through get_close_matches(). This checks how similar a guess is to the true answer instead of requiring an exact match. 

**io**
After seeing that there was an image url within the response data I wanted to show the pokemon at the end of the guess. So we need a way to get the image and display it.

io is an inbuilt python library used for handling various input/output streams. Here it's used through io.BytesIO(), which takes raw bytes (in our case an image) and wraps them so they can be read as if they were a file. We don't have to download ti or save the file on the disk to use it.

**PIL (Pillow)**
We still need to show the image and since the sprites are small we will need to zoom in a little to make it better.
Pillow (PIL), is a third party python library used for opening, editing and displaying images. This is not inbuilt so we need to install it.

```bash
pip install Pillow
```
Here it's used to open the pokemon's sprite image, resize it, and display it in the system's default image viewer.

**Learn more:**
- [Pillow documentation](https://pillow.readthedocs.io/en/stable/)
- [Python difflib documentation](https://docs.python.org/3/library/difflib.html)

## **Code explanation**

#### **Importing dependencies and defining API url**
```python
import random
import requests
import difflib
import io
from PIL import Image

url = "https://pokeapi.co/api/v2/pokemon/?limit=100000"
```
limit=100000 makes sure we get every pokemon in the list. Not having this gets only 20 pokemons and names keep repeating.

#### **Getting response and picking a random pokemon**
```python
response = requests.get(url)
data = response.json()
results = data['results']

random_pokemon = random.choice(results)

pokemon = random_pokemon['name']
pokemon_api = random_pokemon['url']
```

#### **Getting pokemon details and type**
```python
response = requests.get(pokemon_api)
data = response.json()

pokemon_type = data['types'][0]['type']['name']
```

#### **Saving the sprite url for later**
```python
sprite_url = data['sprites']['front_default']
```
The sprite url will be used later to display the image.

#### **Getting extra hints from the species endpoint**
```python
species_url = data['species']['url']
species_response = requests.get(species_url)
species_data = species_response.json()
```

```python
flavor_text = None
for entry in species_data['flavor_text_entries']:
    if entry['language']['name'] == 'en':
        flavor_text = entry['flavor_text'].replace('\n', ' ').replace('\x0c', ' ')
        break
```
flavor_text_entries holds Pokedex descriptions in many languages. We use a loop until we find the English one. we alos have to replace the random charcter for forms like \n or \x0c

```python
if species_data['habitat'] is not None:
    habitat = species_data['habitat']['name']
else:
    habitat = None

color = species_data['color']['name']
```
Habitat can be missing for some pokemon. Color is generally present so we can grab it directly.

#### **Building the hint list**
```python
hints = []
if flavor_text:
    hints.append(f"Pokedex entry: {flavor_text}")
if habitat:
    hints.append(f"Habitat: {habitat}")
hints.append(f"Color: {color}")
```
we can't print a hint saying "None" so we have to remove empty hints

#### **The guessing loop**
```python
close_match = difflib.get_close_matches(guess, [pokemon], cutoff=0.8)

if guess == pokemon or close_match:
```
get_close_matches() compares the guess against a list containing just the correct answer. cutoff=0.8 means the guess has to be about 80% similar. Handles typos or spelling erros.

```python
if hint_index < len(hints) and tries > 0:
    print(hints[hint_index])
    hint_index += 1
```
After each wrong guess, one new hint is revealed. We use indexing to make sure the same hint doesn't repeat.

#### **Final image reveal**
```python
if sprite_url:
    image_bytes = requests.get(sprite_url).content
    image = Image.open(io.BytesIO(image_bytes))

    zoom = 4
    new_size = (image.size[0] * zoom, image.size[1] * zoom)
    image = image.resize(new_size, resample=Image.NEAREST)

    image.show()
```
requests.get(sprite_url).content grabs the raw image bytes, io.BytesIO() wraps them so PIL can read them like a file, and Image.open() turns them into an image object. Sprites are generally small (about 96x96) so we need to scale them up. For pixel type sprites, resample=Image.NEAREST is used so image looks crisp and not blurry.

## **Final Program**
Pokemon Type Guesser: [pokemon_guesser.py](./poke_guessing_game.py)

---

[Back to top](#pokemon-type-guesser)