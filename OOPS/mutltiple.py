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


class parentactor:
    def __init__(self,name,pworth):
        self.pname=name
        self.pworth=pworth
        print(f"{self.pname} is the parent")
    def passets(self):
        print(f"{self.pname} assets are {self.pworth}")
class childactor(parentactor):
    def __init__(self,pname,cname,pworth):
        super().__init__(pname,pworth)
        self.cname=cname
        print(f"{self.cname} is came by the reference of {self.pname}")
    def cassets(self,worth):
        self.cworth=worth
        print(f"{self.cname} is having worth of {self.cworth}cr")
    def totalassets(self):
        print(f"total  assets of {self.cname} is {self.pworth+self.cworth}")
    
ramcharan=childactor("chiranjeevi","ramcharan",100)
ramcharan.cassets(75)
ramcharan.totalassets()
ramcharan.passets()
