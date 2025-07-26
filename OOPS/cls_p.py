# OOPS --------CLASS

# syntax :

# class name:
#     ------
#     ------
#     ------

#------------------static---------
class person:
    name="Naveen"
    age="22"
    gender="male"

obj1=person()
obj2=person()

print(obj2)  # id
print(obj1)

print(obj1.name)
print(obj2.age)

## ------update the value
obj1.name="naveen kumar"

print(obj1.name)
print(obj2.name)

#------------dynamic-----------

class application:
    def __init__ (app,name,color,purpose):
        app.name=name
        app.color=color
        app.purpose=purpose
instagram=application("instagram","pink","reels")
uber=application("uber","black","travelling")
zomato=application("zomato","red","food")

print(instagram.name,instagram.color,instagram.purpose)

# second
class application:
    def __init__ (web,name,color,category):
        web.name=name
        web.color=color
        web.category=category
    def purpose(self):
        print("social media purpose")
# instagram=application("instagram","red","reels")
# rapido=application("rapido","yellow","travelling")
wynk=application("wynk","red","music")

wynk.purpose()
# print(wynk.name,wynk.color,wynk.category)




