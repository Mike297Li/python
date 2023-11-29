class Student:
    # Class attribute
    pi = 3.14159

    @staticmethod
    def add(a, b):
        return a + b + Student.pi

    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age  # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)

    @classmethod
    def addClass(cls):
        return cls.pi


std = Student.getobject()
print(std.addClass())
