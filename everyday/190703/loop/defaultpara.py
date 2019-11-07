#!/usr/bin/env python
# coding=utf-8

def student(name, sex, province, age=7):
    return name + "," + sex + "," + str(age) + "岁" + province


print(student("大盆", "男性","北京", 10))
print(student(sex="女性", name="小龙女",province="南京"))
