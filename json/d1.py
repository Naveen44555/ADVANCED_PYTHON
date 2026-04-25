import requests     #module  python data to convert json
import json


# api="https://fakestoreapi.com/docs"
# data=requests.get(api)
# print(data)
# print(type(data))

# json_data=json.dumps(data)
# print(json_data)














data={
    "name":"naveen",
    "age":22,
    "place":"nereducherla"
}
print(type(data))
print(data)

d=json.dumps(data)
print(d)
print(type(d))

f=json.loads(d)
print(f)
print(type(f))


# d["name"]="raja"      #not posible because we can't add
# print(d)

# d=requests.get(data)
# print(d)

# ----------
data={
    "name":"raja",
    "age":33,
    "salary":22000
}
new=requests.post()