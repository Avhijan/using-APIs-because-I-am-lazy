# **Random Anime Suggestor**

This program uses the Kitsu API and python's requests and random libraries to suggest a random anime.

## **Table of Contents**
- [API used](#api-used)
- [Dependency](#dependency)
- [Code explanation](#code-explanation)

## **API used**
For this project I used API from Kitsu.io. You can plug this into your browser to see what output from the API looks like.
[https://kitsu.io/api/edge/anime](https://kitsu.io/api/edge/anime)

## **Dependency**
This project uses requests like in cat fact generator. If you are intereste:
[Cat Fact Generator](../01_cat_fact_generator/README.md)

**Random**

Random is a inbuild python library which generates random numbers. We can use it to select an option randomly. For this project I used random.choice() to pick a anime randomly from the API's response.

## **Code explanation**

#### **Importing dependencies and defining API url**
```python
import requests
import random

url = "https://kitsu.io/api/edge/anime"
```

#### **Getting Respose from the API**

```python
response = requests.get(url)

print(response) #check status
```
Sends the GET request and checks the status code.

#### **Parsing the data using json() method**

```python
response_data = response.json()
```
Parses the response body into a Python data structure, same as before.

Unlike the cat fact API, this response isn't a flat dictionary. The anime title is nested a few levels deep: response_data is a dict containing a 'data' key, which holds a list of anime, and each anime in that list is a dict with an 'attributes' key, which itself is a dict containing 'canonicalTitle'.

#### **FInding required data and randomizing an anime**
```python
data = response_data['data']
```
Isolates the list of anime from the response.

```python
random_anime = random.choice(data)
```
random.choice() picks one random item out of the data list, this is what makes the suggestion different each time the program runs.

#### **Getting the title of the anime from randomly selected anime**
```python
attributes = random_anime['attributes']
anime_title = attributes['canonicalTitle']
```
Digs into the randomly picked anime's dictionary to pull out its attributes, then grabs the title from within that.

#### **Final Anime Recommendation**
```python
print(f'Anime suggestion: {anime_title}')
```
## **Final Program**
Anime Recommendation System: [anime_recommender.py](./anime_recommender.py)

---

## **Next Project [Ghibli Movie Recommendor](../03_ghibli_movie_recomendor/)**

[**Back to top**](#random-anime-suggestor)