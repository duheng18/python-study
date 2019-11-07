
def exceptionalexample(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print("除数不能为0")
    else:
        print("结果是：",int(result))
    finally:
        print("任何情况下都有我的存在")

# exceptionalexample(10,0)
# exceptionalexample(10,2)


# file_in=open("/Users/duheng/Documents/project/python/190702/Demo1.py1","r")
# print("*"*10)
# content=file_in.read()
# print(content)


def exceptionalexample2(x,y):
    try:
        result=x/y
    except Exception as e:
        print(e)
    else:
        print("结果是：",int(result))
    finally:
        print("任何情况下都有我的存在")

# exceptionalexample2(10,0)
# exceptionalexample2(10,2)


def read_file(in_file):
    try:
        file_in=open(in_file,"r")
    except IOError as e:
        print(e)
read_file("/Users/duheng/Documents/project/python/190702/Demo1.py1")
