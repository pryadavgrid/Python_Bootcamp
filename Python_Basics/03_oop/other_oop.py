# Creating Class
# Class is like we can create own object/Datastructure and define many method or function
class FirstClass():
    # Class Variable
    greeting = "Hello"
    # Constructor/Default Method Call Automatic during Class object creating
    def __init__(self, name):
        # instance Variable
        self.name = name

    # Class instance Method
    def printDetail(self):
        return f"{self.greeting}, {self.name}"
    
    # Class method they take first parameter "cls" mean class
    @classmethod
    def myClassMethod(cls, newGreetingMsg):
        cls.greeting = newGreetingMsg
        
    @staticmethod
    def myStaticMethod():
        return f"Hi, I am static Method"
    
# create Class Object
class_object = FirstClass("Prateek")

# call class Method
# print(class_object.printDetail())
# class_object.myClassMethod("Hii")
# print(class_object.printDetail())
# print(class_object.myStaticMethod())


# Single Ingheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.eat()
d.bark()


# Multilevel Inheritance
class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def play(self):
        print("Puppy plays")

p = Puppy()
p.eat()
p.bark()
p.play()


# Multiple inheritance
class Father:
    def work(self):
        print("Father works")

class Mother:
    def cook(self):
        print("Mother cooks")

class Child(Father, Mother):
    def study(self):
        print("Child studies")

c = Child()
c.work()
c.cook()
c.study()



# Hierarchical Inheritance

class Animal:
    def eat(self):
        print("Animal eats")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.eat()
d.bark()

c.eat()
c.meow()



# Hybrid Inheritance

class A:
    def show_a(self):
        print("Class A")

class B(A):
    def show_b(self):
        print("Class B")

class C(A):
    def show_c(self):
        print("Class C")

class D(B, C):
    def show_d(self):
        print("Class D")

d = D()
d.show_a()
d.show_b()
d.show_c()
d.show_d()


# Some Important Class Method eg. __str__, __len__, __del__

class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects
        print("Object created")

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.subjects)

    def __del__(self):
        print("Object deleted")

s1 = Student("Rahul", ["Math", "Science"])
print(s1)
print(len(s1))
del s1


# Access Modifier

class Person:
    def __init__(self, name, age, salary):
        self.name = name        # Public
        self._age = age         # Protected
        self.__salary = salary  # Private

    def show_salary(self):
        return self.__salary    # Access private inside class


class Employee(Person):
    def show_details(self):
        print("Name:", self.name)     # ✅ Public
        print("Age:", self._age)      # ✅ Protected

        # print(self.__salary)        ❌ Not allowed (Private)
        print("Salary:", self.show_salary())  # ✅ Correct way


e1 = Employee("Rahul", 25, 50000)
e1.show_details()
