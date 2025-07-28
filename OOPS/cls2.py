# class bankaccount:
#     def __init__(acnt,name,email,ph,balance):
#         acnt.name=name
#         acnt.email=email
#         acnt.ph=ph
#         acnt.balance=balance
#     def deposit(self,d_amnt):
#         self.balance+=d_amnt
#     def withdrawal(acnt,w_amnt):
#         acnt.balance-=w_amnt
#     def checkbalance(act):
#         print(act.balance)
# harish_acnt=bankaccount("harish","harish@gmail.com",9848522114,10000)
# harish_acnt.checkbalance()
# harish_acnt.deposit(1000)
# harish_acnt.checkbalance()
# harish_acnt.withdrawal(500)
# harish_acnt.checkbalance()

# print("hello".upper())

a=1
def un():
    pass
print("hello".upper())

class mobile:
    a=33
    def __init__(self,brand,battery,ram,camera,shape):
        self.brand=brand
        self.battery=battery
        self.ram=ram
        self.camera=camera
        self.shape=shape
    def display(self):
        print("brand:",self.brand)
        print("battery:",self.battery)
        print("ram:",self.brand)
        print("camera:",self.brand)
        print("shape;",self.shape)
for i in range(5):
    obj=mobile("apple","5000mah","8gb","100mp","rectangle")
    obj.display()
    print(obj.a)
    print()

#------------

