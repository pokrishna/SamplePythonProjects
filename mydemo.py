from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def set_name(self,name):
        pass
    @abstractmethod
    def get_name(self):
        pass


class Sun(Father):
    def set_age(self,age):
        self.age=age
    def get_age(self):
        return self.age
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
