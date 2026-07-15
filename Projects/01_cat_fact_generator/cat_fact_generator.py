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