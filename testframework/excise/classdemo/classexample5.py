#! /usr/bin/env python
# coding=utf-8

from classexample4 import Student


class SeniorStudent(Student):
    def __init__(self,name,sex,province,grade):
        Student.__init__(self,name,sex,province,grade)
        self.grade=grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "我不告诉你Girl名字"

    def overtime_studv(self):
        if self.grade==3:
            return u"补课"
        else:
            return u"不补课"

if __name__=='__main__':
    sg=SeniorStudent("huahua","Female","Shanghai",3)
    print(sg.overtime_studv())
