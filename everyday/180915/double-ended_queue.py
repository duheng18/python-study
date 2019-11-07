# 双端队列deque
# 双端队列在需要按照元素增加的顺序来移除元素时非常有用。
# collections模块deque类型 defaultdict类型
from collections import deque

q = deque(range(5))
# 增加元素
q.append(5)
# 在左侧(开头)增加元素
q.appendleft(6)
print(q)
# deque([6, 0, 1, 2, 3, 4, 5])
# 弹出右侧的元素
print(q.pop())
# 5
# 弹出左侧（开头）的元素
print(q.popleft())
# 6
# rotate旋转元素（将它们左移或右移使头尾相连）
q.rotate(3)
print(q)
# deque([2, 3, 4, 0, 1])
q.rotate(-1)
print(q)
# deque([3, 4, 0, 1, 2])
# extend和extendleft方法，extend和列表的extend方法差不多，extendleft则类似于appendleft。
# extendleft使用的可迭代对象中的元素会反序出现在双端队列中。
q.appendleft(0.1)
print(q)
# deque([0.1, 3, 4, 0, 1, 2])
