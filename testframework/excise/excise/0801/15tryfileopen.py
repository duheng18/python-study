try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileExistsError:
    print('The data file is missing.丢了')
except PermissionError:
    print('This is not allowed.')
except FileNotFoundError:
    print('No such file or directory')
except Exception as err:
    print('Some other error occurred:', str(err))
# 异常和错误类型
# AssertionError断言语句（assert）失败
# OverflowError:数值运算超出最大限制
# AttributeError尝试访问未知的对象属性
# RuntimeError:一般的运行时错误
# EOFError用户输入文件末尾标志EOF(ctrl+d)
# StopIteration:迭代器没有更多的值
# ImportError导入模块失败的时候
# SyntaxError:Python的语法错误
# IndexError索引超出序列的范围
# IndentationError:缩进错误
# KeyError字典中查找一个不存在的关键字
# TabError:Tab和空格混合使用
# KeyboardInterrupt用户输入中断键（Ctrl+c）
# SystemError:Python编译器系统错误
# SystemExit:Python编译器进程被关闭
# Memory Error内存溢出（可通过删除对象释放内存）
# TypeError:不同类型间的无效操作
# NameError:尝试访问一个不存在的变量
# UnboundLocalError:访问一个未初始化的本地变量（NameError的子类）
# NotImplementedError:尚未实现的方法
# ValueError:传入无效的参数
# OSError:操作系统产生的异常（例如打开一个不存在的文件）
# ZeroDivisionError:除数为零
