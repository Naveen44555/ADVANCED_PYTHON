# # static ---------1

class person:
    name="naveen"
    age="23"
    gender="male"
obj1=person()
obj2=person()
print(obj1)
print(obj2)

print(obj1.name)
print(obj2.name)

obj1.name="naveen kumar"
#update value in obj1
print(obj2.name) #does not reflected to object2
print(obj1.name) #reflecting only in obj1
print(person().age) #does not reflect to person clsaa also  

#static ----------2

class fun:
   name="naveen"
   age=23
   gender="male"

obj1=fun()
obj2=fun()
print(obj1)
print(obj1.name)
print(obj1.age)
print(obj2.gender)

#   -----update values
obj1.name="naveen kumar"
print(obj1.name)


#---------------------dynamic objects-------------------

class person:   
   def __init__(self,name,gender,age):
      self.name=name
      self.gender=gender
      self.age=age

obj_rakesh=person("rakesh","male",25)
obj_kiran=person("kiran","male",26)
print(obj_rakesh.name)
print(obj_kiran.name)


class application:
   def __init__(app,name,color,purpose):
      app.name=name
      app.color=color
      app.purpose=purpose

meesho=application("mesho","meroon","shopping")
myntra=application("myntra","white pink","shopping")
print(meesho.name,meesho.color,meesho.purpose)


class application:
   def __init__ (app,name,color,category):
      app.name=name
      app.color=color
      app.category=category
insta=application("instagram","red","socialmedia")
ola=application("ola","yellow","travelling")
swiggy=application("swiggy","orange","food")

print(insta.name,insta.color,insta.category)
   

class application:
   def __init__ (app,name,color,category):
      app.name=name
      app.color=color
      app.category=category
   def purpose(self,name):
      print("social media pusrpose")
insta=application("instagram","red","socialmedia")
insta.purpose

ola=application("ola","yellow","travelling")
swiggy=application("swiggy","orange","food")

print(f"app is {insta.name} color {insta.color} purpose is {insta.category} usage.")


class application:
   def __init__ (app,name,color,category):
      app.name=name
      app.color=color
      app.category=category
   def purpose(self,app_name,purpose):
      print(f"{app_name}is used for{purpose}")

insta=application("instagram","red","socialmedia")
youtube=application("youtube","red","entertainment")
#ola=application("ola","yellow","travelling")
#swiggy=application("swiggy","orange","food")

#print(insta.name,insta.color,insta.category)

insta.purpose("instagram","pink",)
youtube.purpose("youtube","red")




class daily_usage:
   def __init__ (thing,name,shape,purpose):
      thing.name=name
      thing.shape=shape
      thing.purpose=purpose
bottle=daily_usage("bottle","circle","store water")
box=daily_usage("box","square","groceries")
book=daily_usage("book","rectangle","write anything")
mobile=daily_usage("mobile","rectangular","calls")

print(bottle.name,bottle.shape, bottle.purpose)
print(box.name,box.shape, box.purpose)
print(bottle.name,book.shape, book.purpose)
print(mobile.name,mobile.shape, mobile.purpose)   