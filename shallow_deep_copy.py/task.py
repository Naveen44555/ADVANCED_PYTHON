# # for i in range(0,6):
# #     print(i)
# #     for j in range(1,6):
# #       print(i,j)
    
# v1=5
# v2=10
# lcm_h=v1//1 * v2//v1
# print(lcm_h*3)

# # t1=15,50
# # t2=0
# # while i in t1:

# t1="ABCDEFGHIJKLMNO"
# T2=t1
# for i in t1:
#      for j in i: 
#         print(i)


# for i in range(6):
# for i in range(6,0,-1):
#        print(i*'*')
   

# for i in range(5,0,-1):
#     print(i*'*')

#1.Practise deep copy and shallow copy
#shallow copy
import copy

nn={'sports':{'score':33,'team':11,'out':3}}
naveen=copy.copy(nn)
raj=copy.copy(nn)
vinay=copy.copy(nn)

vinay['sports']['score']=50
raj['sports']['score']=40
naveen['sports']['out']=7
raj['sports']['score']=90
raj['sports']['out']=6

print(naveen)
print(raj)
print(vinay)


#deep copy
nn={'pubg':{'alive':100,'health':90,'kills':2}}
vinay=copy.deepcopy(nn)
lucky=copy.deepcopy(nn)
sheshu=copy.deepcopy(nn)

vinay['pubg']['health']=70
lucky['pubg']['kills']=5

print(vinay)
print(lucky)
print(sheshu)

#2.