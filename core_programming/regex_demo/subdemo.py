import re

# attn: Mr.Smith
#
# Dear Mr.Smith,
print(re.sub('X', 'Mr.Smith', 'attn: X\n\nDear X,\n'))

# ('attn:Mr.Smith\n\nDear Mr.Smith,\n', 2)
print(re.subn('X', 'Mr.Smith', 'attn:X\n\nDear X,\n'))

# XbcdXf
print(re.sub('[ae]', 'X', 'abcdef'))

# ('XbcdXf', 2)
print(re.subn('[ae]', 'X', 'abcdef'))

# 2/20/91
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '20/2/91'))

# ('20/2/1991', 1)
print(re.subn(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3','2/20/1991'))