# 第三方库自动安装脚本
# 自动安装20个第三方库
import os

# 建立集合libs集合中保留了每个库的名称
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests", "jieba", "beautifulsoup4", "wheel", "networkx", "sympy",
        "pyinstaller", "django", "flask", "werobot", "pyqt5", "pandas", "pyopengl", "pypdf2", "docopt", "pygame"}
try:
    # 逐一遍历集合的每个元素
    for lib in libs:
        # 调用一条指令
        os.system(" pip install " + lib)
        print(lib)
    # 为了用户体验好，增加了两条print语句，告诉用户是否安装成功
    print("Sucessful")
except:
    print("Failed Somehow")
