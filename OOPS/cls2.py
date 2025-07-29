
s="naveen"
str=''
for i in s:
    str+=i
a=str.split()
print(a)

# class bankaccount:
#     def __init__(acnt,name,email,ph,balance):
#         acnt.name=name
#         acnt.email=email
#         acnt.ph=ph
#         acnt.balance=balance
#     def deposit(self,d_amnt):
#         self.balance+=d_amnt
#     def withdrawal(self,w_amnt):
#         self.balance-=w_amnt
#     def checkbalance(self):
#         print(self.balance)
# harish_acnt=bankaccount("harish","harish@gmail.com",9848522114,10000)
# harish_acnt.checkbalance()
# harish_acnt.deposit(1000)
# harish_acnt.checkbalance()
# harish_acnt.withdrawal(500)
# harish_acnt.checkbalance()


class bank:
    def __init__(self,branch,name,ac_no,balance):
        self.branch=branch
        self.name=name
        self.ac_no=ac_no
        self.balance=balance
    def deposit(self,dep):
        self.balance+=dep
    def withdrawal(self,w_drawal):
        self.balance-=w_drawal
    def checkbalance(self):
        print(self.balance)

naveen=bank("nereducherla","naven","3333444444444",20000)
naveen.checkbalance()
naveen.deposit(1500)
naveen.checkbalance()
naveen.withdrawal(10000)
naveen.checkbalance()








# # print("hello".upper())

# a=1
# def un():
#     pass
# print("hello".upper())

# class mobile:
#     a=33
#     def __init__(self,brand,battery,ram,camera,shape):
#         self.brand=brand
#         self.battery=battery
#         self.ram=ram
#         self.camera=camera
#         self.shape=shape
#     def display(self):
#         print("brand:",self.brand)
#         print("battery:",self.battery)
#         print("ram:",self.brand)
#         print("camera:",self.brand)
#         print("shape;",self.shape)
# for i in range(5):
#     obj=mobile("apple","5000mah","8gb","100mp","rectangle")
#     obj.display()
#     print(obj.a)
#     print()

# #------------
# class Main:
#     def name(self):
#         pass
#     print('n')
# obj1=Main()

