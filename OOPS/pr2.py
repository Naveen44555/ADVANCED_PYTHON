# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def enginestart(self):
        

# self.brand


# #encapsulation
# class bankaccount:
#     def __init__(self,name,balance):
#         self._name=name
#         self._balance=balance
#     def getbalance(self):
#         print(f'your current balance is :{self._balance}')
#     def deposit(self,amount):
#         if amount>0:
#             self._balance+=amount
#             print(f"{amount} has been credited to your account")
#             print(f'your new balance is :{self._balance}')
#         else:
#             print("invalid amount")
#     def withdraw(self,amount):
#         if 0<amount<self._balance:
#             self._balance-=amount
#             print(f'{amount} has been debited from your account')
#             print(f'your new balance is:{self._balance}')
#         else:
#             print('insufficent balance')

# customer1=bankaccount('shanmukh',50000)
# customer1.getbalance()
# customer1.deposit(150000)
# customer1.withdraw(20000)


# #polymorpism
# #ducktyping
# class dog:
#     def speak(self):
#         print("dog barks")
#     def walk(self):
#         print("dog walks")
# class cat:
#     def speak(self):
#         print('cat meows')
#     def walk(self):
#         print("cat walks")
# class humans:
#     def speak(self):
#         print("man speak")
#     def walks(self):
#         print("man walks")
# def checking(obj):
#     obj.speak()
#     obj.walk()
#     print('it is a man')

# dog1=dog()

# checking(dog1)
# checking(cat)
# checking(humans)

# #method overridng
# class father:
#     def work(self):
#         print("he does work to provide his family")
# class mother:
#     def work(self):
#         print('she cooks food')

# father1=father()
# mother1=mother()
# father1.work()
# mother1.work()

# #method overriding in heritance
# class vehicle:
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#     def start(self):
#         print('car started')
# car1=car()
# car1.start()

# #method overloading
# #simulating 
# class math:
#     def add(self,a=0,b=0,c=0,d=0):
#         return a+b+c+d
# m1=math()
# print(m1.add(3,4))
# print(m1.add(3,4))
# print(m1.add(3,4,7))
# print(m1.add(3,4,7,9))


# #operator overloading
# class book:
#     def __init__(self,pages):
#        self.pages=pages
#     def __add__(self,otherbook):
#         return self.pages+otherbook.pages

# book1=book(250)
# book2=book(300)
# print(book1+book2)

# class class1:
#     def __init__(self,name):
#         self.name=name
#     def __call__(self):
#         print(f'hello {self.name},how are you')
# man1=class1('Naveen')
# man1()
# del man1



