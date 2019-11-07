# 类的命名空间
# 位于class语句中的代码都在特殊的命名空间中执行-类命名空间。这个命名空间可由类内所有成员访问。
# 类的定义其实就是执行代码块
class MemberCounter:
    members = 0

    def init(self):
        MemberCounter.members += 1


m1 = MemberCounter()
m1.init()
print(MemberCounter.members)
m2 = MemberCounter()
m2.init()
print(MemberCounter.members)
print(m1.members)
print(m2.members)
m1.members = 'Two'
print(m1.members)
print(m2.members)
