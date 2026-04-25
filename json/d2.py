import requests
import json

# The FakeStore API is a demo API — it doesn’t actually store or use your data.
# Instead, when you send a POST request, 
# it just pretends to create a user and gives you a fake response with only an id number.

# ----crud-operation
# create,read,update,delete

# methods
# get
# post
# put / patch
# delete 

# 1---get
url="https://fakestoreapi.com/users"
res=requests.get(url)
print(res)

# 2----post
# ----------In Python — two ways to send JSON data
# ✅ Method 1: Use the json parameter (Recommended)
# This is the easiest and safest method when using the requests library.

url="https://fakestoreapi.com/users"
data={
    "name":"raja",
    "age":33,
    "salary":22000
}
response=requests.post(url,json=data)
print(response.status_code)     #Prints the HTTP status (like 200, 201, or 400)
print(response.json())
print(response.text)


# # ✅ Method 2: Convert manually with json.dumps()

url="https://fakestoreapi.com/users"
data={
    "email":"raja@gmail.com",
    "username":"john",
    "password":22000,
}
res=json.dumps(data)
# print(res)
# print(type(res))
headers={
    "employee":"details"
}
response=requests.post(url,res,headers=headers)
print(response.json())
print(response.status_code)

# ----------------------
url="https://fakestoreapi.com/users"
data={
    "name":"nnn",
    "place":"nlg",
    "pin":333
}
res=requests.post(url,json=data)
print(res)
print(type(res))
print(res.status_code)
print(res.json())

# ------manually post
url="https://fakestoreapi.com/users"
data={
    "name":"nnn",
    "place":"nlg",
    "pin":333
}
res=json.dumps(data)
print(res)
headers={
    "emp":"det"
}
response=requests.post(url,res,headers=headers)
print(response.json())

# Convert JSON → Python
data={
     "name":"nnn",
    "place":"nlg",
    "pin":'333'
}
res=json.dumps(data)
nav=json.loads(res)
print(res)
print(nav)
print(type(res))        #<class 'str'>
print(type(nav))        #<class 'dict'>

# 3-----put
# now you’re entering API request methods — 
# PUT and PATCH are very important when updating data on a server.
# Both are used to update existing data in an API,
# but they work a bit differently.

# PUT--Replace completely
# PATCH--Modify partially

# https://fakestoreapi.com/users → All users (list)
# https://fakestoreapi.com/users/1 → Only one user (ID 1)
# https://fakestoreapi.com/users/2 → User with ID 2, and so on

# put
url="https://fakestoreapi.com/users/1"
data={
    "name":"nnn",
    "place":"nlg",
    "pin":45444
}
res=requests.put(url,json=data)
print(res)


# #------patch
url="https://fakestoreapi.com/users/2"
data={
    "name":"nnn",
    "place":"nlg",
    "pin":45444
}
res=requests.patch(url,json=data)
print(res)
print(res.status_code)
print(res.json()) 

# DELETE is an HTTP method used to remove data from the server.
url="https://fakestoreapi.com/users/2"
res=requests.delete(url)
print(res)
print(res.status_code)