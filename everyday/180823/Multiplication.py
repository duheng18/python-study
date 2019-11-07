# 乘法
print('python' * 5)
print([42] * 10)
# None、空列表、初始化
# 初始化一个长度为10的列表
sequence = [None] * 10
print(sequence)

# 序列（字符串）乘法示例
# 以正确的宽度在居中的"盒子"内打印一个句子
# He's a very naughty boy!
sentence = input("Sentence:")
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width) // 2
print
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '|' + sentence + '|')
print(' ' * left_margin + '|' + ' ' * text_width + '|')
print(' ' * left_margin + '+' + '-' * (box_width - 2) + '+')
print
