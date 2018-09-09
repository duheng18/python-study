class Secretive:
    def __inaccessible(self):
        print("Bet you can't see me ...")

    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()


s = Secretive()
# __inaccessible从外界是无法访问的，而在类内部还能使用accessible访问：
# s.__inaccessible()
# 双下划线开始的名字都被“翻译”成前面加上单下划线和类名的形式。
# __inaccessible->
Secretive._Secretive__inaccessible
#实际上还是能在类外访问这些私用方法：
s._Secretive__inaccessible()
s.accessible()
