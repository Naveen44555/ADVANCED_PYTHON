# a=3
# b=4
# a=a+b
# b=a-b
# a=a-b
# print(a,b)



class Base:
    def __init__(self,):
        self.base_val = 100

class Intermediate(Base):
    def __init__(self):
        super(). __init__ ()
        self.inter_val = 200

class Derived(Intermediate):
    def __init__(self):
        super(). __init__()
        self.derived_val = 300

d = Derived()
print(d.base_val)
