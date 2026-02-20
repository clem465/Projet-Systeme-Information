from abc import ABC, abstractmethod

class Duck(ABC):
    
    def __init__(self, fly_behavior,quack_behavior,display_behavior):
        self.__fly_behavior = fly_behavior
        self.__quack_behavior = quack_behavior
        self.__display_behavior = display_behavior
    
    def fly(self):
        self.__fly_behavior.fly()

    def set_fly_behavior(self, fly_behavior):
        self.__fly_behavior = fly_behavior
    
    @abstractmethod
    def quack(self):
        self.__quack_behavior.quack()

    def set_quack_behavior(self, quack_behavior):
        self.__quack_behavior = quack_behavior

    def display(self):
        self.__display_behavior.display()
    
    @abstractmethod
    def display(self):
        pass

class FlyBehavior(ABC):
    
    @abstractmethod
    def fly(self):
        pass

class FlyNone:
    
    def fly(self):
        print('I believe I can fly')

class FlyCloud:
    
    def fly(self):
        print('Fly in the cloud')

class FlyDry:
    
    def fly(self):
        print('Fly dry')


class MallardDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyCloud())
    
    def quack(self):
        print('Quack loud')
        
    def display(self):
        print('I"m MallardDuck')


class RedHeadDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyDry())   
        
    def quack(self):
        print('Quiet loud')
        
    def display(self):
        print('I"m read head')

class RubberDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyNone())
        
    def quack(self):
        print('Pwick')
        
    def display(self):
        print('Yellow')

if __name__ == '__main__':
    donald = MallardDuck()
    picsou = RedHeadDuck()
    rubber = RubberDuck()
    donald.fly()
    picsou.fly()
    rubber.fly()
    picsou.set_fly_behavior(FlyNone())
    picsou.fly() # I believe I can fly expected ???
