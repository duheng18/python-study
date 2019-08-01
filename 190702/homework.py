# 1.利用pip安装第三方模块requests，描述你用什么方法来确认安装是成功的。
# import requests

# 2.把2.918转化成整形
# print(int(2.918))
# print(round(2.918))

# 3.把10进制数18转化成2进制数
# print(bin(18))

# 4.用java替换字符串：“Python is popular” 里面的Python，并把Java变化成JAVA
str = "Python is popular"
str1 = str.replace('Python', 'java')
# print(str1)
firstr = str1[0:4]
str2 = firstr.upper()
str1 = str1.replace(firstr, str2)
# print(str1)

# 5.把列表[1,2,3,4,5,6,7,8]里面的2，4，6，8打印出来
list = [1, 2, 3, 4, 5, 6, 7, 8]
# for index in range(len(list)):
#     if index % 2 == 1:
#         print(list[index])
print(list[1::2])
# 6.创建一个字典，字典的key分别是name,sex,province,修改原始province的值为新值“江苏”
dic = {"name": "dh", "sex": "女", "province": "北京"}
dic["province"] = "江苏"
# print(dic)

Test_str = "Python was  created in 1989,Python is  using in AI, big data, IOT."
# print(Test_str.lower())
list = Test_str.split(" ")
# print(list)
# print(list[int(len(list)/2)])

List_1 = ["python", 5, 6, 8]
List_2 = ["python", "5", 6, 8, 10]
List_1.extend(List_2)
print(List_1)
# list_3=list(set(List_1))
# print(list_3)
