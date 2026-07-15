import requests
import random

url = "https://kitsu.io/api/edge/anime"

response = requests.get(url)

print(response) #check status

response_data=response.json()
#print(response_data) #looking at the data structure
# we can see that the name of anime is located in 'cannonicalTitle' index which is insde attributes which is inside a list on 0th index inside 'data' dict
# print('_____________________________________________________________________________________________________________________')
data = response_data['data']
random_anime = random.choice(data)
attributes = random_anime['attributes']
anime_title = attributes['canonicalTitle']

print(f'Anime suggestion: {anime_title}')