#! /usr/bin/env python
# coding=utf-8

from student import Student


class CollegeStudent(Student):
    def __init__(self, name, sex, province):
        Student.__init__(self, name, sex, province)

    def has_peer(self):
        return self.peer

    def set_peer(self, peer=None):  # 参数加默认值
        if peer:
            self.peer = True
        else:
            self.peer = False


if __name__ == '__main__':
    toni_instance = CollegeStudent('toni', '男', '湖南')
    print(toni_instance.get_name())
    print(toni_instance.get_sex())
