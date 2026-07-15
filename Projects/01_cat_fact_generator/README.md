# **Random Cat Fact Generator**

This program uses an API and python's requests library to get a random cat fact.

## **Table of Contents**
- [API used](#api-used)
- [Dependency](#dependency)
- [Code explanation](#code-explanation)
- [Final program](#final-program)

## **API used**
You may plug this on your browser to look at the output from the API
[https://catfact.ninja/fact](https://catfact.ninja/fact)

## **Dependency**
Python has an inbuilt library for making HTTP requests called urllib specifically urllib.request, which comes packaged with Python by default and requires no installation. It can be used to make API calls just like requests library but it is more complex than requests.

For this project we will use the requests library instead. It is a third party Python library that's much easier to use than urllib. It allows us handle the responses without having to deal with low level complexities like socket or connection code.

When you call requests.get(url), it sends an HTTP GET request to the server and returns a Response object. Here are the methods and features from requests library:
| Attribute / Method | Description | Feature data type/Method |
| :--- | :--- | :--- |
| `.status_code` | Stores HTTP status code about connection | Integer |
| `.headers` | Stores response headers | Dictionary-like object |
| `.text` | Stores response body decoded as a string data type | String |
| `.content` | Stores response body as raw bytes | Bytes |
| `.json()` | A method that parses a JSON body into a Python data structure | Method (convets to python appropriate data structure) |

**Installation:**
```bash
pip install requests
```

**Learn more:**
- [Requests library GitHub](https://github.com/psf/requests)
- [GeeksforGeeks: Python requests module](https://www.geeksforgeeks.org/python-requests-tutorial/)

## **Code explanation**

#### **Importing dependencies and defining API url**
```python
import requests #importing requests

url = "https://catfact.ninja/fact" #our api that gives catfacts
```

#### **Requesting and receiving response**
```python
response = requests.get(url) #store server's response object
```
This sends a GET request to the URL. The server sends back raw bytes (status line + headers + body), and requests parses those bytes locally to build a Response object. That object has:
- .status_code and .headers are extracted from the status/header lines
- .text and .content is decoded from the body bytes

#### **Printing the response object**
```python
print(response)
```
Printing response doesn't print the actual data, because response is an object, not a string. What gets printed is the HTTP status code. This is becuase response's __repr__ method returns the status code.

**Output for valid connection**
```
<Response [200]>
```

#### **Printing the response body**
```python
print(response.text)
```
response.text gives the body of the response, decoded as a plain string.

**Output:**
```
{"fact":"A cat has 32 muscles in each ear.","length":34}
```

#### **Using .json() method from requests to parse the data**
```python
data = response.json() #data stores the info in the form of dictionary
print(data)
```
To work with the data instead of just viewing it, we parse it with .json(). This method converts the JSON body into a fitting Python data structure, in this case, a dictionary.

**Output:**
```
{'fact': 'A cat has 32 muscles in each ear.', 'length': 34}
```
Note it looks nearly identical to response.text, but it's now an actual Python dict(''), not a string("").

#### **Printing required data**
```python
#print (data[0]) #this won't work because the indexes in the output are 'fact' and 'length'
```
Since data is a dictionary, not a list, it can't be indexed with a number like data[0]. It has to be accessed using its keys, 'fact' and 'length'.

```python
print(data['fact'])
```
This isolates just the cat fact from the dictionary.

**Output:**
```
A cat has 32 muscles in each ear.
```

```python
print(data['length'])
```
This isolates the length of the fact string, if needed.

**Output:**
```
34
```

## **Final program**
[cat_fact_generator](cat_fact_generator.py)

## Next Project [Random Anime Recommendation System](../02_anime_recommendation_system/README.md)

[Back to top](#random-cat-fact-generator)