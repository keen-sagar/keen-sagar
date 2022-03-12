from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def sum(self,a,b):
        c = a+b
        return c

class B(A):
    def sum(self):
        print(super().sum(4,5))



s=B()
s.sum()