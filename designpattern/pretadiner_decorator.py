from abc import ABC

class Beverage(ABC):
    
    def __init__(self, description, base_cost):
        self.__description = description
        self.__prices = {
            'sugar': 1,
            'milk': 2,
            'coffee': 1,
            'soja': 3
        }
        self.__quantities = {
            'sugar': 0,
            'milk': 0,
            'coffee': 0,
            'soja': 0
        }
        self.__base_cost = base_cost
        
    def add_soja(self, quantity):
        self.__quantities['soja'] += quantity

    def add_milk(self, quantity):
        self.__quantities['milk'] += quantity

    def add_coffee(self, quantity):
        self.__quantities['coffee'] += quantity

    def add_sugar(self, quantity):
        self.__quantities['sugar'] += quantity

        
    def cost(self):
        cost = self.__base_cost
        for ingredient, price in self.__prices.items():
            cost += self.__quantities[ingredient] * price
        return cost
    
    @property
    def description(self):
        return self.__description
    
class Coffee(Beverage):
    
    def __init__(self):
        super().__init__('coffee', 1)
        self.add_coffee(1)
        self.add_sugar(2)
        
class Latte(Beverage):
    
    def __init__(self):
        super().__init__('latte', 2)
        self.add_coffee(2)
        self.add_milk(1)
        self.add_sugar(3)
        
class Chocolate(Beverage):
    
    def __init__(self):
        super().__init__('chocolate', 3)
        self.add_sugar(10)
        
if __name__ == '__main__':
    beverage_1 = Coffee()
    print(f'{beverage_1.description} : {beverage_1.cost()}')
    beverage_2 = Chocolate()
    print(f'{beverage_2.description} : {beverage_2.cost()}')