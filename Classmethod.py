class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def fun(self):
        pass

    @classmethod
    def get_person(cls, first_name):
        return cls(first_name, "")

person1=Person.get_person("NAME1")
print(person1.first_name)
person2=Person("NAME2","")
print(person2.first_name)