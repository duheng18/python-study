# ls[i]x 替换列表ls第i元素为x
# ls[i:j:k]=lt 用列表lt替换ls切片后所对应元素子列表
# del ls[i] 删除列表ls中第i元素
# del ls[i:j:k] 删除列表ls中第i到第j以k为步长的元素
# ls+=lt 更新列表ls,将列表lt元素增加到列表ls中
# ls*=n 更新列表ls，将列表lt元素增加到列表ls中

# ls.append(x)在列表ls最后增加一个元素x
# ls.clear()删除列表ls中所有元素
# ls.copy()生成一个新列表，赋值ls中所有元素
# ls.insert(i,x)在列表ls的第i位置增加元素x
# ls.pop(i)将列表ls中第i位置元素取出并删除该元素
# ls.remove(x)将列表ls中出现的第一个元素x删除
# ls.reverse()将列表ls中的元素反转
ls = ["cat", "dog", "tiger", 2014]
ls.append(1234)
print(ls)
ls.insert(3, "human")
print(ls)
ls[1:2] = [1, 2, 3, 4]
print(ls)
del ls[::3]
print(ls)
lt = ls * 2
print(lt)
