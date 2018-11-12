# 创建一个名为food的表(其中包含一些合适的字段);读取文件ABBREV.txt并对其进行分析(使用工具函数convert对各行进行分割并对各个字段进行转换);
# 通过调用curs.execute来执行一条SQL INSERT语句，从而将字段中的值插入数据库中。
# 将数据导入数据库
import sqlite3


def convert(value):
    # startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False
    if value.startswith('~'):
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        return value.strip('~')
    if not value:
        value = '0'
    # float() 函数用于将整数和字符串转换成浮点数。
    # 对于其他字段(即数字 字段)，使用float(value)就能获取其内容，但字段为空时不能这样做
    return float(value)


conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food
(id TEXT PRIMAY KEY,
desc TEXT,
water FLOAT,
kcal FLOAT,
protein FLOAT,
fat FLOAT,
ash FLOAT,
carbs FLOAT,
fiber FLOAT,
sugar FLOAT
)
''')
query = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?,)'
field_count = 10
for line in open('ABBREV.txt'):
    # 行分解成字段
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

conn.commit()
conn.close()

# Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，
# 则在指定范围内检查。
# 语法
# startswith()方法语法：
# str.startswith(str, beg=0,end=len(string));
# 参数
# str -- 检测的字符串。
# strbeg -- 可选参数用于设置字符串检测的起始位置。
# strend -- 可选参数用于设置字符串检测的结束位置。
# 返回值
# 如果检测到字符串则返回True，否则返回False。

# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# 注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
# 语法
# strip()方法语法：
# str.strip([chars]);
# 参数
# chars -- 移除字符串头尾指定的字符序列。
# 返回值
# 返回移除字符串头尾指定的字符生成的新字符串。

# float() 函数用于将整数和字符串转换成浮点数。
# 语法
# float()方法语法:
# class float([x])
# 参数
# x -- 整数或字符串
# 返回值
# 返回浮点数。
