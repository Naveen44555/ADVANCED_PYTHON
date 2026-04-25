import re

# #match,search,findall
# ip="hellow world"
# regex=r"hello"
# op=re.match(regex,ip) #it always check starting only
# print(op)   #if it is found that returns none

# op=re.search(regex,ip)
# #returns the matched object if it is found anywhere in the given string 
# #if not found returns none 
# # once it found the match then stops searching.
# op=re.findall(regex,ip)
# print(op)

# #match
# regex1=r"^icici"
# op=re.match(regex1,"icici0276")
# if (op):
#     print("valid for ifsc code")
# else:
#     print("invalid ifsc code")

regex1=r"gmail.com$"
op=re.search(regex1,"naveen gmail.com")  #end  
if(op):
    print("valid")
else:
    print("invalid")


# Pattern	Meaning	Example Match


# .	Any character (except newline)	h.t → hat, hot
# \d	Any digit (0–9)	\d\d → 42
# \D	Any non-digit	\D+ → abc
# \w	Any word character (a–z, A–Z, 0–9, _)	\w+ → hello123
# \W	Any non-word character	\W+ → @#$
# \s	Any whitespace (space, tab, newline)	\s → " "
# \S	Any non-whitespace	\S+ → Hello
# ^ 	Start of string	^Hello matches "Hello world"
# $ 	End of string	world$ matches "Hello world"
# *	 0 or more times	a* → "", a, aaa
# +	 1 or more times	a+ → a, aaa
# ?	 0 or 1 time (optional)	colou?r → color or colour
# {n}	Exactly n times	\d{4} → 2025
# {n,}	n or more times	\d{2,} → 99, 1234
# {n,m}	Between n and m times	\d{2,4} → 99, 1234
# [abc]	One of a, b, or c	[ch]at → cat, hat
# [^abc]	Not a, b, or c	[^0-9] → any non-digit
# ( )	Grouping	(ab)+ → abab


# regex1=r"\d"
# op=re.search(regex1,"hello123")
# if(op):
#     print("valid")
# else:
#     print("invalid")

# regex1=r"\w"        #alphabets numbers characters
# op=re.search(regex1,"hello123")
# if(op):
#     print("valid")
# else:
#     print("invalid")

# regex1=r"\s"        #
# op=re.search(regex1,"hello123")
# if(op):
#     print("valid")
# else:
#     print("invalid")

# regex1=r"[abc]"     #invalid because no abc aatleast one letter
# op=re.search(regex1,"helloworld")
# if(op):
#     print("valid")
# else:
#     print("invalid")

# regex1=r"[aeiou]"    #vowels 
# op=re.search(regex1,"we")
# if(op):
#     print("vowels valid")
# else:
#     print("v invalid")

# regex1=r"[e-i]"    
# op=re.search(regex1,"abcd")
# if(op):
#     print("e valid")
# else:
#     print("v invalid")

# regex1=r"[a-z]"    
# op=re.search(regex1,"abcd")
# if(op):
#     print("a-z valid")
# else:
#     print("a-z invalid")

# regex1=r"[a-z]"    
# op=re.search(regex1,"abcd")
# if(op):
#     print("a-z valid")
# else:
#     print("a-z invalid")

# regex1=r"[^aeiou]"    #this will not allow a string with pure vowels
# op=re.search(regex1,"aei")
# if(op):
#     print("vowels valid")
# else:
#     print("vowels invalid")

# regex1=r"^aeiou"    #this will not allow a string with pure vowels
# op=re.search(regex1,"welcome")
# if(op):
#     print("vowels valid")
# else:
#     print("vowels invalid")

regex1=r"\w{5}"
op=re.search(regex1,"hedssssss")
if(op):
    print("5 valid")
else:
    print("5 invalid")

# regex1=r"^\w{5,10}$"
# op=re.search(regex1,"hellopopo pop")
# if(op):
#     print("5 valid")
# else:
#     print("5 invalid")

# regex1=r"^"

# regex1=r"\w{10}"
# op=re.search(regex1,"hiiihelo")
# try:
#     print("ok nav")
# except:
#     print("not nav")


regex1=r"^[a-zA-Z]+\d+[a-zA-Z]$"
op=re.search(regex1,"SWGASD3444P")
if (op):
    print("valid name")
else:
    print("invalid name")