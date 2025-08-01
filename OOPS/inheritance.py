#aquiring methods and attributes from already defined class into newly created
#called inheritance

#types:
'''1.single inheritance 
2.multiple  inheritance
3.multipath  inheritance
4.hybrid inheritance
5.heirarhical inheritance'''

# 1.single inheritance 
# if we derive one child class from single parent class then it is single inheritance

# class parent:
#     def pmethod(self):
#         print("iam a method from parent")
#     def pmethod2(self):
#         print("iam a second method from parent")
    
# class child (parent):
#     def cmethod(self):
#         print("iam a method from child")

# obj1=child()
# obj1.pmethod()
# obj1.cmethod()
# obj1.pmethod()
# obj1.pmethod2()

# #------------------2

# class parent:
#     def pmethod(self):
#         print("iam a method from parent")
#     def pmethod2(self):
#         print("iam a second method from parent")
    
# class child (parent):
#     def cmethod(self):
#         print("iam a method from child")
#         super().pmethod2()   #calling method from super class using super

# obj1=child()
# obj1.cmethod()
# obj1.pmethod()
# obj1.pmethod2()

# #-------------

class user:
    def __init__ (self,name,email):
        self.name=name
        self.email=email
class student(user):
    def __init__ (self,name,email,enrolledcourses):
        super().__init__(name,email)
        self.enrolledcourses=enrolledcourses
    def getcourses(self):
        print(f"{self.name} is learning {self.enrolledcourses}")
class instructor(user):
    def __init__(self,name,email,courses_training):
        super().__init__(name,email)
        self.courses_training=courses_training
    def getcourses(self):
        print(f"{self.name} is teaching {self.courses_training}")
student_obj=student("naveen","naveen@gmil.com",["html","css","python","js"])
student_obj.getcourses()
trainer_obj=instructor("harish","harish@gmail.com",["html","css",'js'])
trainer_obj.getcourses()


# #--
# class user:
#     def __init__ (self,name,email):
#         self.name=name
#         self.email=email
# class student(user):
#     def __init__ (self,name,email,enrolledcourses):
#         super().__init__(name,email)
#         self.enrolledcourses=enrolledcourses
#     def getcourses(self):
#         print(f"(self.name) is learning {self.enrolledcourses}")
# class instructor(user):
#     def __init__(self,name,email,courses_training):
#         super().__init__(name,email)
#         self.courses_training=courses_training
#     def getcourses(self):
#         print(f"{self.name} is teaching {self.courses_training}")
# student_obj=student("naveen","naveen@gmil.com",["html","css","python","js"])
# student_obj.getcourses()
# trainer_obj=instructor("harish","harish@gmail.com",["html","css",'js'])
# trainer_obj.getcourses()

# #2.multiple  inheritance:
# # if we derive one child class from more than one parent class then it is a multiple inheritance



