import sys, shelve


def store_pernson(db):
    """
    Query user for data and store it in the shelf object
    :param db:
    :return:
    """
    pid = input('Enter unique ID number：')
    person = {}
    person['name'] = input('Enter name:')
    person['age'] = input('Enter age:')
    person['phone'] = input('Enter phone number:')

    db[pid] = person


def lookup_person(db):
    """
    Query user for ID and desired field,and fetch the corresponding data from the shelf object
    :param db:
    :return:
    """
    pid = input('Enter ID number:')
    field = input('What would you like to know?(name,age,phone)')
    # 对用户的输入使用strip和lower函数，可以让用户随意输入大小写字母和添加空格。
    # strip去除首尾的空格 lower字符串中所有大写字符转换程小写
    field = field.strip().lower()

    # Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。
    print(field.capitalize() + ':', db[pid][field])


def print_help():
    print('The available commands are:')
    print('store : Store information about a person')
    print('lookup: Looks up a person from ID number')
    print('quit: Save changes and exit')
    print('? : Prints this message')


def enter_command():
    cmd = input('Enter command(? for help):')
    cmd = cmd.strip().lower()
    return cmd


def main():
    # 在main函数中用shelve打开数据库（database）,然后将其作为参数传给另外需要它的函数。
    database = shelve.open('/Users/baidu/Downloads/dh/180915/database')  # You may want to change this name
    # 使用try/finally确保数据库能够正确关闭。
    try:
        while True:
            cmd = enter_command()
            if cmd == 'store':
                store_pernson(database)
            elif cmd == 'lookup':
                lookup_person(database)
            elif cmd == '?':
                print(print_help())
            elif cmd == 'quit':
                return
    finally:
        database.close()


# 主程序放在main函数中，只有在条件成立的时候才被调用。这意味着可以在其他程序中将这个程序作为模块导入，然后调用main函数。
if __name__ == '__main__': main()
