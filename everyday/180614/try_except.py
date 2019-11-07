try:
    number = eval(input("请输入一个整数:"))
    print(number ** 2)
except NameError:
    print("输入的不是一个整数")
'''try:
        <语句块1>
    except:
        <语句块2>
    else:
        <语句块3>
    finally:
        <语句块4>
如果发生异常执行语句1、2、4
不发生异常执行语句1、3、4
语句块4一定执行


'''