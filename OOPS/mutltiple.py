class parent1:
    def p1method(self):
        print("iam a method from parent1")
class parent2:
    def p2method(self):
        print("iam a method from parent2")
class child(parent1,parent2):
    def cmethod(self):
        print("iam a method from child")
        super().p1method()
      
obj1=child()
# obj1.p2method()
obj1.cmethod()