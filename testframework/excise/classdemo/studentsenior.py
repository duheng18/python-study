#! /usr/bin/env python
#   coding=utf-8

from collegestudent import CollegeStudent


class StudentSenior(CollegeStudent):
    def __init__(self, name, sex, province):
        CollegeStudent.__init__(self, name, sex, province)

    def set_grade(self, grade):
        self.grade=grade

    def get_grade(self):
        return self.grade

    def get_name(self):
        return "jojo "

if __name__ == '__main__':
    toni_instance = StudentSenior('toni', '男', '湖南')
    print(toni_instance.set_grade("dddd"))
    print(toni_instance.get_name())
    print(toni_instance.get_sex())
    print(toni_instance.get_grade())
