# Using APIs Because I Am Lazy, and I know you are too.
<br></br>
**"Progress is made by lazy men looking for easier ways to do things"**

**— Robert Heinlein**

<br></br>

## **My Thoughts:**
Imagine scraping websites, managing a database, or maintaining physical data storage. Couldn't be me. This repository is a testament to humanity's greatest strength: our boredom.

Unfortunately for us, anything and everything we can ever think of has already been thought of. However, in programming, this means complex ideas and difficult logic have already been executed long before us. We don't necessarily have to write complex code, manage massive datasets, or even understand the underlying logic of various applications to use them. We can use **API**s to leverage these systems and build our desired projects.

Take a simple weather app, for example. Considered one of the most basic beginner projects, it's often built by amateurs. Yet, as a concept, isn't it literally divine knowledge to predict the weather of the entire world, let alone having most of those predictions be accurate the majority of the time?

Experienced developers, or any programmers really, overlook these projects because, from a coding standpoint, we don't have to indulge in any complex calculations, ML predictions, or any difficult logic. It's already handled somewhere else, and we get to reap the benefits through a simple **API** call.

I am constantly fascinated by weather apps and similar projects because I believe these so called "simple projects" demonstrate the true power of **API**s. They allow you to freely use the collective knowledge of the entire human race. It's so powerful that it makes the god-gifted ability to accurately predict the weather seem mediocre at best.

---
<br></br>

# **What is an API?**
**API** stands for **Application Programming Interface**. It is a set of rules, tools and protocols that allows applications to communicate and exchange information with one other. It connects two different application systems by establishing a connection which lets them exchange data and information.

#### **Sources:**
* [**GeeksforGeeks**](https://www.geeksforgeeks.org/software-testing/what-is-an-api/)

* [**IBMthink**](https://www.ibm.com/think/topics/api?mhsrc=ibmsearch_a&mhq=API)

## **Characteristics**

* APIs connect two different applications by establishing a secure connection between them.
* APIs enable communication and exhange of information by defining the type of data and how the data is transmitted. 
* APIs validate the concept of DRY(don't repeat yourself) in software development. Instead of writing complex code from scratch we may access already existing systems and reap their results.
* APIs are used in almost everything in the modern world; from developing simple mobile apps to complex cloud computing and banking apps.


### **Don't Repeat Yourself [DRY]**
**DRY** is a fundamental software development concept. It's core principle is to prevent developers from reinventing the wheel by writing redundant code that's already been written and burning time and resources. 

**eg:** An example of this is developers using API of google maps while building an EV charging management system. The developers don't have to waste resources or time building an entire map system, instead they can rely on already existing proven google maps.


## **Working of API** :
API communication comprises of three major parts i.e.
1) **Client**
2) **API** itself
3) **Server**

Generally, Client is simply the device making requests for data while server is the powerful device responsible for fullfilling those requests. In our case we can say that the application requesting the data is the client while the application responsible for providing requested data can be called server. Meanwhile, API acts as the middle man serving as the bridge between the client and server enabling the transfer of data and functionalities.

## **Types of API**
APIs can be classified into four types:

1) REST [**Representational State Transfer**]
2) SOAP [**Simple Object Access Protocol**] 
3) GraphQL
4) gRPC [**Google Remot Procedure Call**]


### **API Types: Methods & Data Formats**

| API Type | Architecture/Protocol | Primary Methods | Data Formats | State  |
| :--- | :--- | :--- | :--- | :--- |
| **REST** <br>*(Representational State Transfer)* | **HTTP / HTTPS** | Standard HTTP methods | Primarily **JSON**, but supports **XML, HTML,** and **plain text**. | **Stateless** |
| **SOAP** <br>*(Simple Object Access Protocol)* | **HTTP, SMTP, TCP,** etc. | XML defined operations |  **XML**  | **Stateful or Stateless.** |
| **GraphQL** | **HTTP** | Single endpoint with POST queries and mutations. | **JSON** | **Stateless.**  |
| **gRPC** <br>*(Google Remote Procedure Call)* | **HTTP/2** | Direct Function/Procedure Calls (RPC). | **Protocol Buffers** / **Binary** | **mostly Stateless** |

</br>

### **Applications:** 
* **REST**: Standard web applications.
* **SOAP**: Strict legacy enterprise or banking systems.
* **GraphQL**: Complex, nested data and optimization of frontend.
* **gRPC**: Connecting backend microservices together.

</br>

## **API Integration**
API integration is merely the process of connecting two application system or more using API.

## [Restrictions while using APIs](https://www.geeksforgeeks.org/software-testing/what-is-an-api/#restrictions-of-using-apis)

There are certain rules we have to follow while using APIs. These are called restritions. They limit how APIs are used for optimization of resources and authentication. Here are few restrictions

1) Rate Limits: Rate limits are maximum number of API calls that can be made within a specific time period.
2) Authentication: Paid APIs and sometimes free APIs require API keys, tokens, or OAuth for access for authenticataion and verification. This prevents spam and DDOS attacks.
3) Access: Limit resources and actions for users or applications.
4) Usage Quotas: Total API usage based on subscription plans, service tiers, or daily/monthly limits.



## **Free APIs / Public APIs**
Free APIs cost you nothing and you can use them to learn how to implement APIs in your program. These are used for research, education or learning developmental skills.

### **Where to find Free APIs?**
The Open-Source community has compiled a massive repository full of free APIs which you can use to make your programs. Its called public-apis and you can find hundreds of free APIs here. The link for the repo is given as follows:

[**public-apis on GitHub**](https://github.com/public-apis/public-apis)

##### **NOTE:** Please note that sometimes even free APIs require API key for authentication to prevent spam

Here are a few examples of APIs which don't require API keys: 

* **Cat Facts API:** Returns random trivia about cats. 
* **JSONPlaceholder:** A fake online REST API for testing and prototyping.


If you are looking for a challenge, here are some examples of APIs with API keys and authentication. You will have to sign up to get API keys. 
* **OpenWeatherMap:** Talked about in myths and legends, it gives you current weather data for any location on Earth.
* **NASA APIs:** Taps into live space data, including the Astronomy Picture of the Day and Mars Rover photos.
* **CoinGecko:** Provides live cryptocurrency market data, prices, and volumes without needing a paid subscription.
---

### **Please don't accidently publish these keys in public repositories**
Github facilitates securing your API keys using a feature called SECRETS which allows you to safely store your keys. This allows you to access your keys while being completly hidden from bad actors.

[**Learn more about Secrets**](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) 

---
For added security, locally you could create a environment file to store your keys and place your .env in .gitignore file to protect your keys. This will prevent it from ever getting pushed.

---
 
### Simple Projects that implement APIs

| # | Project | Description | Link |
| :--- | :--- | :--- | :--- |
| 1 | **Random Cat Fact Generator** | Fetches a random cat fact from the Cat Facts API. | [View Project](./Projects/01_cat_fact_generator/README.md) |
| 2 | **Random Anime Suggestor** | Suggests a random anime using the Kitsu API. | [View Project](./Projects/02_anime_recommendation_system/README.md) |
| 3 | **Random Ghibli Movie Recommendor** | Recommends a random Studio Ghibli film using the Ghibli API. | [View Project](./Projects/03_ghibli_movie_recomendor/README.md) |
| 4 | **Pokemon Guessing Name** | A guessing game where you're given a pokemon's type and hints, then have to guess the pokemon, using the PokeAPI. | [View Project](./Projects/04_guess_the_pokemon/READMEmd) |