import requests #importing requests

url = "https://catfact.ninja/fact" #our api to get catfacts


#----------------------------------------------------------------------------------------------------------------------
#Explanation of the code
#----------------------------------------------------------------------------------------------------------------------

# lets send a requests to the url and store in variable named 'response'
# server sends raw bytes (status line + headers + body) which is constructed into a response object by requests
# requests parses those bytes and builds a Response object locally, exposing:
#   .status_code, .headers  <- extracted from the status/header lines
#   .text, .content         <- decoded from the body bytes
#   .json()                 <- a method built into requests
# response object is used to extract .status_code and .headers from header line, .content .text is decoded from body bytes, and .json() method is available because of requests
response = requests.get(url) #store server's response object 

# when we print response, it doesn't print data because response is an object
# instead the status code is printed, should be [200]
print(response) #prints the https status becuase its inside the __repr__ method

#printing response.text gives the body part of the response object in string format
print(response.text) # should print out body of response obj

# to print only the data we need to parse the object 
# json method parses the data into a fitting python data structure, in this case thats dictionary
data =  response.json() #data stores the info in the form of dictionary 
print(data) # data should print nearly identical output as response.text but its in dict form 

#since data is a dictionary we can access the cat fact using index
#print (data[0]) #this won't work because the indexes in the output are 'fact' and 'length'

#isolating fact using data[fact]
print (data['fact'])

#if we need it we can isolate length from data dictionary too
print(data['length'])

#----------------------------------------------------------------------------------------------------

#Now that we know what each part is responsible for
#we can write a program that can handle errors too status[200] means everthing is working fine

import requests

url = "https://catfact.ninja/fact"

response = requests.get(url)

if response.status_code == 200: #as response is a object we have to isolate status_code using .status code
    data =  response.json()
    print(data['fact'])
else:
    print("Error: Sever can't be reached rn")

#---------------------------------------------------------------------------------------------------