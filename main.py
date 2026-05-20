#3-m
class Phone:
    def __init__(self, model, zaryad):
        self.model = model
        self.__zaryad = zaryad
        
    @property
    def zaryad(self):
        return self.__zaryad
    
    @zaryad.setter
    def zaryad(self, toza):
        self.__zaryad = toza
        
        
c1 = Phone("Iphone 15", 90)
print(c1.model)

res = c1.zaryad
print(res)

c1.zaryad = 100
print(c1.zaryad)
