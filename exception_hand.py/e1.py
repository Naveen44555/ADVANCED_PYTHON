# print("hello")

try:
    # x=int(input("enter x value:"))
    # y=int(input('enter y value:'))
    x=7
    y='nn'

    print(x+y)
except TypeError as error:
    print("you are trying to add integer and string",error)
except KeyError as error:
    print("unknown dict keys you enter")
except ZeroDivisionError as error:
    print("we can't divide any number with zero")
except ValueError as error:
    print('ask the user when user enter string instead of int')
except SyntaxError as error:
    print('your are missing semicolon or something else')
except IndentationError as error:
    print('indentation is not proper')
except FileNotFoundError as error:
    print('file not found error- your file doesnot exist')
except:
    print('something went wrong')
finally:
    print('code executed succefully')

# #code executed succefully
# x=8
# y=9
# print(x+y)

# #1.Nameerrror
# x=8
# y=9
# print(x+y+z)

# #3.Type error
# x=19
# y='nn'
# print(x+y)

# #4.value error
# x=int(input('enter a num'))
# y=int(input('enter'))
# print(x+y)

# #5.indentation error
#  x=8
# y=9
# print(x+y)

# #6.syntax error
# x=8
# if x is 9 
#  print(x)

# #7.zero divison error
# a=7
# b=77
# print(a/0)

# #8.key errror
# dict={'name':'naveen','gender':'male'}
# print(dict['hno'])

# # 9.file not found errror
# open ('./naveen.py')

# #10.ModuleNotFoundError
# try:
#     import some
# except ModuleNotFoundError as error:
#     print('it is module not found error ')

# # import some

