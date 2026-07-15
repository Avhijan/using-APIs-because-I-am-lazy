import random
import requests

url = "https://ghibliapi.vercel.app/films"

response = requests.get(url)
print(response) #printing connection status

data=response.json()
random_movie = random.choice(data)
print(f"Random Recommendation: {random_movie['title']}")
