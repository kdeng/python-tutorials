# -*- coding: utf-8 -*-

class Student(object):
    name = 'Student'

    def __init__(self, name):
        self.name = name;



s = Student('bob')
print("Before delete attribute")
print(s.name)
print(Student.name)

print("After delete attribute")
del s.name
print(s.name)
print(Student.name)
