# 方法是一个与某些对象有紧密联系的函数，对象可能是列表、数字，也可能是字符串或者其他类型的对象。
# 方法调用：对象.方法（参数）
# 1.append
# append方法用于在列表末尾追加新的对象：
# 在恰当的位置修改原来的列表。这就意味着它不是简单地返回一个修改过的新列表，而是直接修改原来的列表。
lst = [1, 2, 3]
lst.append(4)
print(lst)
# 2.count
# count统计某个元素在列表中出现的次数
n = ['to', 'be', 'or', 'not', 'to', 'be'].count('to')
print(n)
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))
print(x.count([1, 2]))
# 3.extend
# 可以在列表的末尾一次性追加另一个序列中的多个值。
# 用新列表扩展原有的列表。
# extend方法修改了被扩展的序列。
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
# 不是一个原位置操作，并不会修改原来的列表。
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a)
# 分片赋值来实现相同的效果
a = [1, 2, 3]
b = [4, 5, 6]
a[len(a):] = b
print(a)
# 4.index
# index方法用于从列表中找出某个值第一个匹配项的索引位置：
knights = ['We', 'are', 'the', 'Kinights', 'who', 'say', 'ni']
print(knights.index('who'))
# 5.insert
# insert方法用于将对象插入到列表中。
# 与extend方法一样，insert方法的操作也可以用分片赋值来实现。
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
# numbers[3:3]=['four']
print(numbers)
# 6.pop
# pop方法会移除列表中的一个元素（默认是最后一个），并且返回该元素的值：
x = [1, 2, 3]
x.pop()
print(x)
x.pop(0)
print(x)
# pop方法是唯一个既能修改列表又返回元素值（除了None）的列表方法。
# 使用pop方法可以实现一种常见的数据结构--栈。栈的原理就像堆放盘子那样。顶部放盘子顶部拿走。
# LIFO后进先出
# 入栈(push)、出栈（pop）append入栈
# pop方法和append方法的操作结果恰好相反，如果入栈（或者追加）刚刚出栈的值，最后得到的结果还是原来的栈。
x = [1, 2, 3]
x.append(x.pop())
print(x)
# 如果需要一个先进先出（FIFO）的队列，那么可以使用insert（0,...）来代替append方法。或者，也可以继续使用append方法，
# 但必须用pop(0)来代替pop().更好的解决方案是使用collection模块中的deque对象。
# 7.remove
# remove方法用于移除列表中某个值的第一个匹配项。
# 只有第一次出现的值被移除来，而不存在于列表中的值是不会被移除的。
# remove是一个没有返回值的原位置改变方法。它修改来列表却没有返回值，这与pop方法相反。
x = ['to', 'be', 'or', 'not', 'to', 'be', 'bee']
x.remove('be')
print(x)
x.remove('bee')
print(x)
# 8.reverse
# reverse方法将列表中的元素反向存放。(该方法也改变来列表但不返回值)
# 需要对一个序列进行反向迭代，那么可以使用reverse函数。这个函数并不返回一个列表，而是返回一个迭代器对象。
x = [1, 2, 3]
x.reverse()
print(x)
# 使用list函数把返回对对象转换成列表也是可行的：
x = [1, 2, 3]
m = list(reversed(x))
print(m)
# 9.sort
# sort方法用于在原位置对列表进行排序。在"原位置排序"意味着改变原来的列表，从而让其中的元素能按一定的顺序排列，
# 而不是简单地返回一个已排序的列表副本。
x = [4, 6, 2, 1, 7, 9]
x.sort()
print(x)
# sort方法修改了x的却返回了空值，那么最后得到的是已排序的x以及值为None的y.
x = [4, 6, 2, 1, 7, 9]
y = x.sort()
print(y)
# 把x的副本赋值给y，然后对y进行排序。
x = [4, 6, 2, 1, 7, 9]
# x[:]得到的是包含了x所有元素的分片，这是一种很有效率的复制整个列表的方法。
y = x[:]
y.sort()
print(x)
print(y)
# 只是简单地把x赋值给y是没用的，因为这样做就让x和y都指向同一个列表了。
y = x
y.sort()
print(x)
print(y)
# 另一种获取已排序的列表副本的方法是，使用sorted的函数：
x = [4, 6, 2, 1, 7, 9]
y = sorted(x)
print(x)
print(y)
# 这个函数实际上可以用于任何序列，却总是返回一个y=x.sort()列表：
d = sorted('Python')
print(d)
# 如果想把一些元素按相反的顺序排列，可以先使用sort(或者sorted),然后再调用reverse方法，或者也可以使用reverse参数。
# 10高级排序
# 如果希望元素能按照特定的方式进行排序，可以通过compare(x,y)的形式自定义比较函数。compare(x,y)函数会在x<y时返回负数，
# #在x>y时返回正数，如果x=y则返回0。定义好该函数后，就可以提供给sort方法作为参数了。内建函数cmp提供了比较函数的默认实现方式：
numbers = [5, 2, 9, 7]
numbers.sort()
print(numbers)
# sort方法有另外两个可选的参数-key和reverse。如果要使用它们，那么就要通过名字来指定（这叫做关键字参数）。
# 必须提供一个在排序过程中使用的函数。然而，该函数并不是直接用来确定对象的大小，而是为每个元素创建一个键，然后所有元素根据键来排序。
# 如果要根据元素的长度进行排序，那么可以使用len作为键函数：
x = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
x.sort(key=len)
print(x)
# 关键字参数reverse是简单的布尔值（True或者False）用来指明列表是否要进行反向排序。
x = [4, 6, 2, 1, 7, 9]
x.sort(reverse=True)
print(x)
