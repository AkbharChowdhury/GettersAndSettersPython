class Fruit:
    def __init__(self, name: str):
        self.__name = name

    @property
    def fruit_name(self):
        return self.__name

    @fruit_name.setter
    def fruit_name(self, value):
        self.__name = value

    @fruit_name.deleter
    def fruit_name(self, value):
        print(f'{self.__name} was deleted')
        del self.__name


