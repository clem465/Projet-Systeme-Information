class Spaceship:
    
    __instance = None 
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Spaceship()
        return cls.__instance

if __name__ == '__main__':
    a = Spaceship.get_instance()
    b = Spaceship.get_instance()
    print(f'Type: {type(a)}, Name: {a}')
    print(f'Type: {type(b)}, Name: {b}')
    assert a == b