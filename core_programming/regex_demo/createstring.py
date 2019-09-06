import re

m = re.match('[cr][23][dp][02]', 'c3p0')  # 匹配c3p0
if m is not None: print(m.group())

m = re.match('[cr][23][dp][02]', 'c2d0')  # 匹配c3p0
if m is not None: print(m.group())

m = re.match('r2d2|c3p0', 'c2d0')  # 不匹配 c2d0
if m is not None: print(m.group())

m = re.match('r2d2|c3p0', 'r2d2')  # 不匹配 r2d2
if m is not None: print(m.group())
