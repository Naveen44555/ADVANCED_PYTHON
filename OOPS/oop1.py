# # print("hii")
# class person():
#     name="naveen"
#     age=22
#     city="hyd"
# p=person()
# p1=person()
# p.name="hh"
# # p1.name="hh"
# print(p.name)
# print(p1.name)
# print(p.age)
# print(p.city)
  
# class sample_class:
#     def sample_method():
#         print("hii")
# obj1=sample_class()
# obj1.sample_method()



# class Mine:
#     at1=3
#     at2=4
# print(Mine.at1)

# class BankAccount:
#     def __init__(self,accountno,accname,ifsecode,balance):
#         self.accountno=accountno
#         self.accname=accname
#         self.ifsecode=ifsecode
#         self.balance=balance
#     def display(self):
#         print( self.accountno,self.accname,self.ifsecode, self.balance)
# obj=BankAccount(2233,"naveen",1234,4000)
# obj.display()

class BankAccount:
    def __init__(self,accountno,accname,ifsecode,balance):
        self.accountno=accountno
        self.accname=accname
        self.ifsecode=ifsecode
        self.balance=balance
    def withdraw(self,amount):
        self.balance-=amount
    def deposit(self,amount):
        self.balance+=amount
    def checkBalance(self):
        print(self.balance)
obj = BankAccount(1234,"naveen",2233,5000)
obj.checkBalance()
obj.deposit(1000)
obj.checkBalance()
obj.withdraw(3000)
obj.checkBalance()



# class BankAccount:
#     def __init__(self,accno,accountname,money):
#         self.accno=accno
#         self.no=accountname
#         self.money=money
        
#     def deposit(self,amount):
#         self.money+=amount
#     def withdraw(self,amount):
#         self.money-=amount
# obj1=BankAccount(123456,'naveen',3000)
# # obj1.Account(123456,'naveen',3000)
# obj1.deposit(2000)
# print(obj1.money)
# obj1.withdraw(1000)
# print(obj1.money)



# class BankAccount:
#     def __init__(self,accno,accname,branch,money):
#         self.ano=accno
#         self.aname=accname
#         self.branch=branch
#         self.money=money
#     def deposit(self,amount):
#         self.money+=amount
#     def withdraw(self, amount):
#         self.money-=amount
# obj1=BankAccount(11223344,"honey","annaram",1000)
# print(obj1.money)
# obj1.deposit(2000)
# print(obj1.money)
# obj1.withdraw(500)
# print(obj1.money)


# # without __init__
# class per:
#     pass
# p1=per()
# p1.name="naveen"
# p1.age=233
# print(p1.age)

# a=10
# print(a)
# del a
# print(a)


# inheritance
# # single
# class Parent:
#     def m1(self):
#         print("iam parent")
# class Child(Parent):
#     def m2(self):
#         print("iam child")
# obj=Child()
# obj.m1()
# obj.m2()

# # multiple
# class father:
#     def m1(self):
#         print("iam father")
# class mother:
#     def m2(self):
#         print("iam mother")
# class child(father,mother):
#     def m3(self):
#         print("iam child")
# p1=child()
# p1.m2()
# p1.m3()
# p1.m1()


