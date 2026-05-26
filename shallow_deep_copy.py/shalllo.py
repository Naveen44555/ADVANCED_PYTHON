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

# sravani['score']['runs']=9
# print(score_b)
# print(nithish)
# print(sravani)

# # import copy

# # score_b={'score':{'runs':44,'overs':4.5,'players':12}}
# # nithish=copy.copy(score_b)
# # sravani=copy.copy(score_b)

# # sravani['score']['runs']=33

# # print(score_b)
# # print(nithish)
# # print(sravani)

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



# x=[1,2,3,[1,2,3],4,5,6,[3,4,5,[1,2,3[2,3,4,]]]]
# # x=[1,2,3]
# y=x[3]
# z=0
# for i in y:
#     z=i+z
# print(y)



# # --------new
# # import copy

# ----shallow copy
# a=[1,2,3,[4,5]]
# b=a.copy()
# #         b=copy.copy(a)
# b[0]=100
# print(b)
# print(a)
# b[3][0]=400
# print(b)
# print(a)

# a=[1,2,3,[4,5]]
# import copy
# b=copy.deepcopy(a)
# b[0]=100
# print(b)
# print(a)
# b[3][0]=400
# print(b)
# print(a)


# # ---shallow c
# import copy
# a={"score":{"kills":2,"deaths":2,"health":30}}
# naveen=copy.copy(a)
# honey=copy.copy(a)
# honey["score"]["deaths"]=5
# print(honey)
# print(naveen)

# # deep copy
# import copy
# b={"score":{"kills":2,"deaths":1,"health":70}}
# ani=copy.deepcopy(b)
# kushi=copy.deepcopy(b)
# ani["score"]["kills"]=4
# print(ani)
# print(kushi)