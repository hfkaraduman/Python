class kareler():
    def __init__(self,max):
        self.max=max
        self.kuvvet=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.kuvvet <=self.max):
            sonuc=self.kuvvet*self.kuvvet
            self.kuvvet+=1
            return sonuc
        else:
            self.kuvvet=1
            raise StopIteration
kareler=kareler(5)

iterator=iter(kareler)

for i in kareler:
    print(i)
