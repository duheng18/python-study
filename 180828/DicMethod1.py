# 使用get的简单数据库
import people
labels = {
    'phone': 'phone number',
    'addr': 'address'
}
name = input('Name:')
# 查找电话号码还是地址？
request = input('Phone number (p) or address (a)')
# 使用正确的键：
key=request
# 如果请求既不是'p'也不是'a'
if request=='p':
    key='phone'
if request=='a':
    key='addr'

#使用get()提供默认值
person=people.get(name,{})
label=labels.get(key,key)
result=person.get(key,'not available')
print("%s's %s is %s."%(name,label,result))