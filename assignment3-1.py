#Q4--Tsk4
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.__gender = gender
        self.__age = age   # to restric the direct access to age

    #to set age
    def setAge(self, age):
        self.__age = age

    #to get age
    # to get age
    def getAge(self):
        return self._age

    def sayHello(self):
        print("hello from the person")

    def is_adult(self):
        if self.__age > 18:
            return True
        else:
            return False


p1 = Person("FUCHUN", "MALE2", 30)
#will have error: 'Person' object has no attribute '__age'
#print(p1.__age)
p1.setAge(12)
# if do not have such property, it will create one
# p1.__age=32
print(p1._Person__age)
print(p1._Person__gender)