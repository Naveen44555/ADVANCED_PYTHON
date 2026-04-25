import re
# regex=r"hello"  #r--create our own regex
# ip="hello world"  #input

# op=re.match(regex,ip)
# print(op)

#2
# regex=r"a.b"
# op=re.match(regex,"a1b")
# print(op)


# regex=r"ubin"
# op=re.match(regex,"ubin1234")
# if (op):  
#    print("valid input")
# else:
#    print("invalid input")


# regex=r"ubin | UBIN"        #or
# op=re.match(regex,"ubin1234")
# if (op):  
#    print("valid input")
# else:
#    print("invalid input")

# #end with $
# regex=r"1234$"      #end 
# op=re.search(regex,"ubin1234")
# if (op):  
#    print("valid input")
# else:
#    print("invalid input")

# regex=r"^hdfc\d+$"
# op=re.search(regex,'hdfc1234')
# if(op):
#     print("valid")
# else:
#     print("invalid")


# regex=r"[a-zA-Z3-7]"
# op=re.search(regex,"2")
# if(op):
#     print("avalid")
# else:
#     print("ainvalid")

# regex=r"[a-f]"      #letter only be a to f
# op=re.search(regex,"a-f")
# if (op):
#     print("valid")
# else:
#     print("invalid")


# regex=r"(a-f)"      #letter only be a or - or f first or middle a-f require in any where
# op=re.search(regex,"a-f")
# if (op):
#     print("valid")
# else:
#     print("invalid")

# regex=r"(dev)"
# op=re.search(regex,"hello developer")
# if (op):
#     print("valid")
# else:
#     print("invalid")

# regex=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}"
# op=re.search(regex,"ABCDE1222D")
# if (op):
#     print("valid pan number")
# else:
#     print("invalid pan number")


# regex=r"[6-9]{1}[0-9]{9}"
# op=re.search(regex,"9381615365")
# if (op):
#     print("valid mobile number")
# else:
#     print("invalid mobile number")

regex=r"^(\+91)\s[6-9]{1}[0-9]{9}$"
op=re.search(regex,"+919381615365")
if (op):
    print("valid india mobile number")
else:
    print("invalid india mobile number")

# regex=r"^[1-9]{6}"
# op=re.search(regex,"222292")
# if(op):
#     print("valid code")
# else:
#     print("invalid code")


# regex=r"^[1-9]{1}[1-9]{5}"
# op=re.search(regex,"222292")
# if(op):
#     print("valid pincode")
# else:
#     print("invalid pincode")

#date 
# regex=r"^[1-9]{1}[0-9]{3}(-)[0-9]{2}(-)[0-9]{2}"
regex=r"^[1-9]{4}(-)(0[1-9]{1}1[0-2]{1})(0[1-9]1)(-)(0[0-2]{1}1[0-9]{1}2{0-9})"
op=re.search(regex,"2222-09-12")
if(op):
    print("valid")
else:
    print("invalid")