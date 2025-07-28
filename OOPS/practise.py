# number=int(input("number:"))
# is_perfect=True

# def num():
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print(i)
#             else:
#                 print("it is prime")
#     else:
#         print("invalid")
# num(4)

#----------
# def num():
#     if num>1:
#         for i in range(2,num):
#             if num%i==0:
#                 print(i)
#             else:
#                 print("it is prime")
#     else:
#         print("invalid")
# num(4)

# def  is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n+1):
#         if n%i==0:


# for i in range(1,12):
#     for j in range(i,j+1):
#         if j%i==0:
#             print(j,)
        

# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# n=int(input("number:"))
# print(n)

# # bin
# n1="111"
# n2="100"
# sum1=0
# j=0

# for i in range(len(n1)-1,-1,-1):
#     sum1==int(n1[i]*(2**j))
#     j+=1
# k=0
# for i in range(len(n2)-1,-1,-1):
#     sum1+=int(n2[i]*(2**k))
#     k+=1
# print(str(bin(sum1))[2: ])


#aaa unte one a remove

# s='sraaavan'
# res=s[0]
# c=0
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#         if c<3:
#             res+=s[i]
#     else:
#         c=1
#         res+=s[i]
# print(res)


a=100
t_c=a
w=a
while w>=3 :
    e=w//3
    t_c+=e
    w=e+w%3
print(t_c)

    





