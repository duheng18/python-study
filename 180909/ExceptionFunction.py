# 异常和函数
# 异常和函数能很自然地一起工作。如果异常在函数内引发而不被处理，它就会传播至函数调用的地方。如果在那里也没有处理异常，它就会继续传播，
# 一直到达主程序（全局作用域）。如果那里没有异常处理程序，程序会带着栈跟踪中止。
def faulty():
    raise Exception('Something is wrong')


def ignore_exception():
    faulty()


def handle_exception():
    try:
        faulty()
    except:
        print('Exception handled')
# ignore_exception()
handle_exception()