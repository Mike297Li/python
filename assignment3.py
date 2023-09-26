# Q1
class vehicle:
    def __init__(self, name_of_vehicle, max_speed, average_of_vehicle):
        self.name_of_vehicle = name_of_vehicle
        self.max_speed = max_speed
        self.average_of_vehicle = average_of_vehicle


# Q2
class car(vehicle):
    def seating_capacity(self, capacity):
        return self.name_of_vehicle, capacity


car = car("name", 120, "average")
print(car.seating_capacity(100))


# Q3
# multiple inheritance: one class inherit from multiple class
class A:
    pass


class B:
    pass


class C(A, B):
    pass


# Q4 Task1-3
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def sayHello(self):
        print("hello from the person")

    def is_adult(self):
        if self.age > 18:
            return True
        else:
            return False


class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)  # use parent constructor
        self.student_id = student_id
        self.course = course

    def sayHello(self):
        print("hello from the Student")


class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, subject):
        super().__init__(name, age, gender)  # use parent constructor
        self.teacher_id = teacher_id
        self.subject = subject

    def sayHello(self):
        print("hello from the Teacher")


P1 = Person("name", 33, "male")
S1 = Student("name", 12, "male", "123", "FSDM")
T1 = Teacher("name", 43, "male", "456", "database")
P1.sayHello()
S1.sayHello()
T1.sayHello()
