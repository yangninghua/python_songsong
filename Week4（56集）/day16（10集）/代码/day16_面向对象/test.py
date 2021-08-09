class ParentClass:
    def __init__(self):
        self.__x = 1
        self.y = 10

    def print(self):
        print(self.__x, self.y)


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.__x = 2
        self.y = 20

c = ChildClass()
c.print()