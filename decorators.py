# # decorators
# def greet():
#     print('hello')
# greet()

# def check_msg(func):
#     def wrapper():
#         print('before original')
#         func()
#         print('after original')
#     return wrapper

# @check_msg
# def greet():
#     print('hello')
# greet()


# #  *args, **kwargs
# def para(*a):
#     def wrapper (*args):
#         if 0 in args:
#           return "hello"
# print(para(7,34,456,456,7,8,5,99,0,6))


def param(*args):
    return args
    