# 别名方式将turtle库别名为t
import turtle as t

# 设置绘制窗口的标题栏信息
t.title("自动轨迹绘制")
# 设置绘制窗口的大小
t.setup(800, 600, 0, 0)
# 设置初始绘制的画笔颜色
t.pencolor("red")
# 绘制画笔的粗细
t.pensize(5)
# 数据读取,定义一个空列表
datals = []
# 打开data.txt文件，解析数据文件中每一行信息，并且对这一行的信息进行处理。
f = open("data.txt", "rt")
# 从文件中读取遍历每一行
for line in f:
    # 将文件最后的\n换行符转换成空字符串，去掉换行的信息
    # line信息存储的是我们定义的每一行数据接口的值
    line = line.replace("\n", "")
    print(line)
    # 将数据接口的值进行分隔处理，并且提取其中的信息
    # 拿到的每一行都有6个参数，中间用，进行分隔。当我们用for line in f获取一行信息时，我们拿到的是字符串。
    # 希望解析的元素都是真实的数据。用ine.split(",")将字符串分割成若干个字符串，分隔依据",".
    # map函数 python提供的内嵌函数，无需import可以直接使用的函数。map函数作用：将第一个参数的功能作用于第二个参数的每一个元素。
    # map(eval, line.split(","))作用，将列表中的每一个元素两侧的引号都去掉。这些运算产生的结果就是列表，列表中每一个元素都去掉了字符串中的引号
    # 而变成了数字。之后我们使用append将字符串放到我们预先定义的datals列表中。
    datals.append(list(map(eval, line.split(","))))
f.close()
# 逐一的获取其中的遍历整数。
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
