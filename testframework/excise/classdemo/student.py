#! /usr/bin/env python
# coding=utf-8

from persondemo2 import Person

import sys

sys.path.append('/Users/duheng/Documents/project/excise/classdemo/')
print(sys.path)


class Student(Person):

    def __init__(self, name, sex, province):
        Person.__init__(self, name, sex, province)

    def set_grade(self, grade):
        self.grade = grade

    def get_sex(self):
        return '我不告诉你'


if __name__ == '__main__':
    toni_instance = Student('toni2', '男2', '湖南2 ')
    print(toni_instance.get_name())
    print(toni_instance.get_sex())
