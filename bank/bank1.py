# import random
class bank:
   def create_new_account(self):
     h_details ={}

     data=random.randint(1000444444,88880999999)
     h_details['h_name']=input('enter holder name:')
     h_details['mobile']=input('enter mobile number')
     h_details['aadhar']=input('enter adar number')
     h_details['account_number']=data
     h_details['ifsc']='IFSC25554'

     n1=input('select type')
    