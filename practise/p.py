# list="34,46,76,89"
# list.split

# Telugu vowels: అ to ఔ (U+0C05 to U+0C14)
# Telugu consonants: క to ఱ (U+0C15 to U+0C39)

# print("తెలుగు అక్షరాలు:\n")

# # Vowels
# for code in range(0x0C05, 0x0C14 + 1):
#     print(chr(code), end=" ")

# # Consonants
# for code in range(0x0C15, 0x0C39 + 1):
#     print(chr(code), end=" ")

# for i in range (0x0c15, 0x0c39):
#   print(chr(i))

# print(chr(0x0c15))

# #---------
# s="naveen"
# str=''
# for i in s:
#     str+=i
# a=str.split()
# print(a)

#-------------------
#print(1,12,123)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


n=5
for i in range(1,n+1):
    p=""*(n-i)
    print(p,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()