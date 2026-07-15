# **Random Ghibli Movie Recommendor**

This program uses the Studio Ghibli API and python's requests and random libraries to suggest a random Ghibli movie.

It's not very different from the [anime recommendation system](../02_anime_recommendation_system/README.md). In fact its almost exactly the same thing with a different API. I wrote this code for the sole reason of exploring data received from responses. It probably took me less than 15 minutes to do probably because I added no new functions here but regardless I had fun. 

## **Table of Contents**
- [API used](#api-used)
- [Dependency](#dependency)
- [Code explanation](#code-explanation)

## **API used**
For this project I used the Studio Ghibli API. 
[https://ghibliapi.vercel.app/films](https://ghibliapi.vercel.app/films)

## **Dependency**
This project uses requests and random. If you want simple examples of them being used, its used in the previous two programs.
[Cat Fact Generator](../01_cat_fact_generator/README.md)
[Random Anime Suggestor](../02_anime_recommendation_system/README.md)

## **Code explanation**

#### **Importing dependencies, defining API url and getting response**
```python
import random
import requests

url = "https://ghibliapi.vercel.app/films"

response = requests.get(url)
print(response) #printing connection status
```

#### **Parsing the data and randomizing a movie**
```python
data = response.json()
random_movie = random.choice(data)
```
Unlike the anime API, this response is a flat list of movie dictionaries, so random.choice() can pick directly from data without digging into a nested 'attributes' key.

#### **Final Recommendation**
```python
print(f"Random Recommendation: {random_movie['title']}")
```

## **Final Program**
Ghibli Movie Recommendation System: [ghibli_recommender.py](./ghibli_recommendor.py)

---

## **Next Project: [Guess the pokemon](../04_guess_the_pokemon/READMEmd)**

[**Back to top**](#random-ghibli-movie-recommendor)