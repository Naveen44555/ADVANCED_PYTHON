# def factorial (n):
#     fact=1
#     if n==1 or n==0:
#         return fact
#     else :
#         factorial_n=n*factorial(n-1)
#         return factorial_n
# print(factorial(5))


# import copy
# score_b={'score':{'runs':44,'players':10,'overs':5}}
# nithish=copy.copy(score_b)
# sravani=copy.copy(score_b)

# sravani['score']['runs']=2
# print(score_b)
# print(nithish)
# print(sravani)

# import copy

# score_b={'score':{'runs':44,'overs':4.5,'players':12}}
# nithish=copy.copy(score_b)
# sravani=copy.copy(score_b)

# sravani['score']['runs']=33

# print(score_b)
# print(nithish)
# print(sravani)

# import copy
# pubg={'score':{'score':44,'health':100,'kills':0}}

# shanmukh=copy.deepcopy(pubg)
# tharun=copy.deepcopy(pubg)
# naveen=copy.deepcopy(pubg)
# abdul=copy.deepcopy(pubg)

# shanmukh['score']['kills']+=3
# naveen['score']['health']-=25

# print(pubg)
# print(shanmukh)
# print(naveen)
# print(abdul)