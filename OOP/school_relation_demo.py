#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Duo

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def hire(self,tea_obj):
        self.teachers.append(tea_obj)


    def enroll(self,stu_obj):
        self.students.append(stu_obj)

class SchoolMember(object):
    def __init__(self,name,age,sexual):
        self.name = name
        self.age = age
        self.sexual = sexual
    def personal_info(self):
        pass


class Teacher(SchoolMember):
    def __init__(self,name,age,sexual,course,salary):
        super(Teacher, self).__init__(name,age,sexual)
        self.course = course
        self.salary = salary

    def personal_info(self):
        print('''
        ==== info of teacher ====
        name:%s
        age:%s
        sexual:%s
        course:%s
        salary:%s
        '''%(self.name,self.age,self.sexual,self.course,self.salary))

    def teach(self):
        print('%s is teaching %s'%(self.name,self.course))

class Student(SchoolMember):
    def __init__(self, name, age, sexual, stu_id, grade):
        super(Student, self).__init__(name, age, sexual)
        self.stu_id = stu_id
        self.grade = grade

    def personal_info(self):
        print('''
        ==== info of teacher ====
        name:%s
        age:%s
        sexual:%s
        stu_id:%s
        grade:%s
        '''%(self.name,self.age,self.sexual,self.stu_id,self.grade))

    def pay_tuition(self,amount):
        print('%s has paid %s tuition'%(self.name,amount))


sc1 = School("Duo University","1100 W Wells Street")

t1 = Teacher("Duo Zhang",27,"F","Business Intelligence",120000)

s1 = Student("Yang Chen",26,"M","Lover0001","Business Intelligence")


t1.personal_info()

sc1.hire(t1)

print(sc1.teachers[0].name)