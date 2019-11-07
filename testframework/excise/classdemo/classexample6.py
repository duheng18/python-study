#! /usr/bin/env python
# coding=utf-8

class Person:
    total_person = 0  # 类变量

    def __init__(self, name, sex, province):
        print("Init the class")
        self.name = name
        self.sex = sex  # 实例变量
        self.province = province
        Person.total_person += 1

    @staticmethod  # 静态方法 不用初始化就能访问
    def set_new_name(new_name):
        return "new name is:" + new_name

    @property
    def get_sex(self):
        return self.sex

    def get_name(self):
        return self.name

    @classmethod  # 类方法
    def set_new_province(cls, new_province):
        return "Your province is:" + new_province


if __name__ == '__main__':
  # print(Person.set_new_name("hanmeimei"))
  # print(Person.get_name)
  # print(Person.set_new_name("Jiangsu"))
  # print("*" * 50)

    pp = Person("huahua", 'Female', 'Shanghai')
    # print(pp.get_name())
    # print(pp.set_new_province("广东"))
    # print(Person.set_new_name('toni'))  # 静态方法可以用类调用
    print(pp.get_sex)
    print(pp.get_name())
