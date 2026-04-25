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



# class Mine:
#     at1=3
#     at2=4
# print(Mine.at1)

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



class BankAccount:
    def __init__(self,accno,accname,branch,money):
        self.ano=accno
        self.aname=accname
        self.branch=branch
        self.money=money
    def deposit(self,amount):
        self.money+=amount
    def withdraw(self, amount):
        self.money-=amount
obj1=BankAccount(11223344,"honey","annaram",1000)
print(obj1.money)
obj1.deposit(2000)
print(obj1.money)
obj1.withdraw(500)
print(obj1.money)






