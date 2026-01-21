
# class Car:
#     def __init__(self,brand,color,year):
#         self.brand=brand
#         self.color=color
#         self.year=year
#     def display_info(self):
#         print(f"\nBrand:{self.brand}\ncolor:{self.color}\nYear:{self.year}\n")
        
# car1=Car("Toyota","White",2024)
# car1.display_info()
# car2=Car("Honda","Red",2025)
# car2.display_info()


# # print(type(car1)) print type 

# # print a specific attribute
# print(f"Brand:{car1.brand}")


# car1.brand="BMW"
# car1.color="Metallic Blue"
# car1.display_info()



# class Dog:
#     def __init__(self,breed,age):
#         self.breed=breed
#         self.age=age
#     def bark(self):
#         print(f"\nBreed:{self.breed}\nAge:{self.age}\n")
        
# dog1=Dog("Golden Retriever",5)
# dog1.bark()
# dog2=Dog("Rottweiler",10)
# dog2.bark()


# # # print a specific attribute
# print(f"Breeds:{dog1.breed}, {dog2.breed}")

# dog1.age="8"
# dog1.bark()


# class Student:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#     def display_grade(self):

#         if self.mark>=90:
#             return "A Grade"
#         elif self.mark>=80:
#             return "B Grade"
#         elif self.mark>=70:
#             return "C Grade" 
#         elif self.mark>=50:
#             return "D Grade" 
#         else:
#             return "You are Failed.....!"
        
# student1=Student("Hari",78)
# print(f"Name:{student1.name}\n Mark:{student1.mark}\n  Grade:{student1.display_grade()}")

# str method  
# class Book:
#     def _init_(self,bookname,author):
#         self.bookname=bookname
#         self.author=author
#     def _str_(self):
#         return f"{self.bookname} written by {self.author}"
# book1=Book("Macbeth","Shakespear")
# print(book1)



 

# class Employee:
#     company="ABC CORP" #class variable
#     def __init__(self,name,position):
#         self.name=name #instance variable
#         self.position=position
# emp1=Employee("Hari","Manager")
# emp2=Employee("Vyshnav","Developer")

# #Accessing class variable
# print(emp1.company)
# print(emp2.company)

# # Accessing instance variable
# print(emp1.name)

# Innerclass object -  Class within class (tied to outer)

# class Employee:
#     class Company:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location
#     def __init__(self,name,salary,cname,location):
#         self.name=name
#         self.salary=salary
#         self.Company=Employee.Company(cname,location) #innerclass object
    
#     def display_employee(self):
#         print(f"\nName:{self.name}\nSalary:{self.salary}\nCompany:{self.Company.cname}\nLocation:{self.Company.location}\n")
        
# emp=Employee("Hari",50000,"APPLE","California")
# emp.display_employee()

# Composition: One class has another class as an object. 

# Tight Coupling: Object created inside the class.

# class Company:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location
# class Employee:
#     def __init__(self,name,salary,cname,location):
#         self.name=name
#         self.salary=salary
#         self.Company=Company(cname,location) 
        
    
#     def display_employee(self):
#         print(f"\nName:{self.name}\nSalary:{self.salary}\nCompany:{self.Company.cname}\nLocation:{self.Company.location}\n")
        
# emp=Employee("Hari",50000,"APPLE","California")
# emp.display_employee()

# del Employee
# try:
#     print(Employee.Company.cname)
# except Exception as e:
#     print("Error",e)
    

# Loose Coupling: Object created outside and injected.

# class Company:
#         def __init__(self,cname,location):
#             self.cname=cname
#             self.location=location
# class Employee:
#     def __init__(self,name,salary,comp):
#         self.name=name
#         self.salary=salary
#         self.comp=comp
        
#     def display_employee(self):
#         print(f"\nName:{self.name}\nSalary:{self.salary}\nCompany:{self.comp.cname}\nLocation:{self.comp.location}\n")

# c1=Company("Apple","California")
# emp1=Employee("Hari",50000,c1)
# emp1.display_employee()

# del emp1
# try:
#     print(emp1.comp.cname)
# except Exception as e:
#     print("Error",e)


# Encapsulation
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def employee_display(self):
#         print(f"\nName:{self.name}\nSalary:{self.__salary}\n")
#     def update_salary(self,new_salary):
#         self.__salary=new_salary
# emp1=Employee("Hari",50000)
# emp1.employee_display()
# # print(emp1.name)
# # print(emp1.__salary)
# emp1.update_salary(100000)
# emp1.employee_display()


# Inheritance
# single inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"{self.name} makes sound")
# class Dog(Animal):
#     def speak(self):
#         print(F"{self.name} says.woof..!")
# Dog=Dog("Rottweiler")
# Dog.speak()

# multiple inheritance 
# class Engine:
#     def start_engine(self):
#         print(f"{self.name} engine Started")
# class Wheels:
#     def rotate(self):
#         print("Wheels are Rotating")
# class Car(Engine,Wheels):
#     def __init__(self,name):
#         self.name=name 
#     def drive(self):
#         print(f"{self.name} owner is driving the car")
        
# car=Car("BMW")
# car.start_engine()
# car.rotate()
# car.drive()

# class Grandparent: 
#     def sing(self): 
#         print("Grandparent is singing.") 
# class Parent(Grandparent): 
#     def dance(self): 
#         print("Parent is dancing.") 
# class Child(Parent): 
#     def play(self): 
#         print("Child is playing.")
# child = Child()
# child.sing()  
# child.dance()  
# child.play() 

# Hierarchical Inheritance 
# class Animal: 
#     def speak(self):
#         print("Animal speaks.") 
# class Dog(Animal): 
#     def speak(self): 
#         print("Dog barks.") 
# class Cat(Animal): 
#     def speak(self): 
#         print("Cat meows.") 
# dog = Dog() 
# cat = Cat() 
# dog.speak() 
# cat.speak() 

# polymorphism
# method overriding
# class Animal:
#     def speak(self):
#         return "some Sound"
# class Dog(Animal):
#     def speak(self):
#         return "Woof...!"
# class Cat(Animal):
#     def speak(self):
#         return "Meow"
# def animal_sound(animal:Animal):
#     return animal.speak()

# dog=Dog()
# cat=Cat()
# print(animal_sound(dog))
# print(animal_sound(cat))

# # Duck Typing...

# class Dog: 
#     def speak(self): 
#         print("Woof!") 
# class Cat: 
#     def speak(self): 
#         print("Meow!") 
# class Human: 
#     def speak(self): 
#         print("Hello!") 
# def make_it_speak(obj):                         
#     obj.speak()
# # Duck typing in action 
# for creature in [Dog(), Cat(), Human()]:
#     make_it_speak(creature)
    
# Abstraction
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
#     def area(self):
#         return self.width * self.height
# class square(Shape):
#     def __init__(self,a):
#         self.a=a
#     def area(self):
#         return self.a * self.a
      
# rectangle=Rectangle(10,20)
# square=square(10)
# print(f"Area : {rectangle.area()}")
# print(f"Area : {square.area()}")


# Constructor and Destructor 

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print(f"{self.name} has been created")
#     def __del__(self):
#         print(f"{self.name} has destroyed")  
# person=Person("Hari",24)
# del person

# Deccorator Function 
# def decorator(func):
#     def wrap():
#         print("Hiiii.....")
#         func()
#         print("John")
#     return wrap

# @decorator
# def greet():
#     print("Gud Morning")
# greet()

# def aaa(func):
#     def wrap(*args, **kwargs):
#         print("Start")
#         a=func(*args,**kwargs)
#         print (a)
#         print("End")
#     return wrap
# @aaa
# def add(a,b):
#     return a+b
# add(10,30)
# @aaa
# def sub(a,b):
#     return a-b
# sub(20,50)
       
# class methods 
# class Company:
#     company_name="Tech Innovators"
    
#     @classmethod
#     def change_company_name(cls,new_name):
#         cls.company_name=new_name
# print(f"Company name:", Company.company_name)
    
# # change class variable through a class method 
# Company.change_company_name("Softronics")
# print(f"COmpany name after Changing:",Company.company_name)

# Static Method 
class Operation:
    @staticmethod
    def add(a,b):
        return a+b
op=Operation()
print(f"Addition:",op.add(20,30))
            

 


            
    






            