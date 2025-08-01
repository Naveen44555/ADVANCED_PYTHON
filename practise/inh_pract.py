# class parent:
#     def pmethod(self):
#         print("iam a parent method 1")
#     def pmethod2(self):
#         print("iam parent method2")
# class child(parent):
#     def cmethod(self):
#         print("iam child method")
#         super().pmethod()
# obj1=child()
# obj1.cmethod()


# #-----------------
# class user:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
#     def student(self,name,email,courses):
#         super().__init__(name,email)
#         self.courses=courses
# class instructor(user):
#     def __init__(self,name,email,course_training):
#         super().__init__(name,email)
#         self.course_training=course_training
#         print(f'name{name} and email {email} courses is trairning {course_training}')
#     def trainer(self,name,email,courses):
#         super().__init__(name,email)
#         self.courses=courses
# obj=instructor()
# obj.trainer("harish","harish@gmail.com",["html","css","js","python"])
# obj.trainer()

# class user:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email
# class student(user):
#     def __init__(self,name,email,course_learning):
#         super().__init__(name,email)
#         self.course_learning=course_learning
#     def getcourses(self):
#         print(f"name is {self.name} email is {self.email} learning courses {self.courses_learning} ")
# class instructor(user):
#     def __init__(self,name,email,course_trianing):
#         super().__init__(name,email)
#         self.course_training=course_trianing
#     def get_courses(self):
#          print(f"name is {self.name} email is {self.email} course trainer for {self.course_training}")

# obj=instructor("harish","harish@gmail.com",["html","css","python"])
# obj.get_courses()


class user:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class student(user):
    def __init__(self,name,email,course_learning):
        super().__init__(name,email)
        self.course_learning=course_learning
    def getcourses(self):
        print(f"{self.name} {self.email} {self.course_learning}")
    def append_course(self,course_name):
        self.course_learning.append(course_name)
        print(f"{self.name} {self.email} {self.course_learning}")
    def remove_course(self,course_name):
        self.course_learning.remove(course_name)
        print(f"{self.name} {self.email} {self.course_learning}")

class instructor(user):
    def __init__(self,name,email,course_training):
        super().__init__(name,email)
        self.course_training=course_training
    def getcoursess(self):
        print(f'{self.name} {self.email} {self.course_training}')

# obj=instructor("harish","harish@gmail.com",["html","sql","django"])
# obj.getcoursess()
obj1=student("naveen","naveen@gmail.com",["html","css","js"])
obj1.getcourses()

obj1.append_course("js")
obj1.remove_course("js")
