#!/usr/bin/python3
"""
Person:
- Name
- Email
- Passowrd

Student:
- Name
- Email
- Passowrd

Teacher:

"""

class Person:
	def __init__(self, name, email, age=-1):
		self.name = name
		self.email = email
		self.age = age
	
	def get_details(self):
		detail = f"My name is {self.name} and my email is {self.email}"
		print (detail)

	def get_email(self):
		return self.email

class Student(Person):
	def __init__(self, name, email, age, classRoom):
		self.classRoom = classRoom
		super().__init__(name, email, age)

	def is_above_18(self):
		if self.age == -1:
			raise ValueError("The Age is not given")
		return self.age > 18
	
	def get_details(self):
		detail = f"My name is {self.name} and my email is {self.email} \
		. I am also a student in {self.classRoom}."
		print(detail)
		return detail
	
	def get_email(self):
		if self.age > 18:
			return super().get_email()
		return -1


person1 = Person("Eva", "eva@gmail.com")
person2 = Person("Ella", "ella@gmail.com")
person1.get_details()
person2.get_details()

stud1 = Student("Solo", "solo@gmail.com", 25, "B-class")
stud1.get_details()
print(stud1.is_above_18())