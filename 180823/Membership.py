# 成员资格
# 为了检查一个值是否在序列中，可以使用int运算符。
# 'w' 'x'是否在字符串permissions中。在Unix中，这两行代码可以作为查看文件可写和可执行权限的脚本。
permissions = 'rw'
print('w' in permissions)
print('x' in permissions)
# 检查所提供的用户名mlh是否在用户列表中。如果程序需要执行某些安全策略，这个检查就派上用场了。
users = ['mlh', 'foo', 'bar']
print(input('Enter your user name:') in users)
# 可以作为垃圾邮件过滤器的一部分，检查字符串subject是否包含字符串'$$$'
subject = '$$$ Get rich now!!!$$$'
print('$$$' in subject)
# in运算符会检查一个对象是否为某个序列（或者是其他的数据集合）的成员（也就是元素）。然而字符串唯一的成员或者元素就是它的字符。
print('P' in 'Python')
# 查看用户输入的密码和PIN密码是否存在于数据库（列表）中的程序。
database = [['albert', '1234'], ['dilbert', '4242'], ['smith', '7524'], ['jones', '9843']]
username = input('User name:')
pin = input('PIN code:')
if [username, pin] in database:
    print('Access granted')
