class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is {} and I am {} years old.".format(self.name, self.age))


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def say_hello(self):
        super().say_hello()
        print("I am in grade {}.".format(self.grade))

student = Student("Alice", 17, 11)
student.say_hello()
