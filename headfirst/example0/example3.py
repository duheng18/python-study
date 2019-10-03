# 从标准库的string模块导入template类。它支持简单的字符串替换模板
from string import Template


# 这个函数需要一个可选的字符串作为参数，用它来插件一个CGI"Content-type:"
# 行。参数缺省值是"text/html".
def start_response(resp="text/html"):
    return ('Content-type:' + resp + '\n\n')


# 这个函数需要一个字符串作为参数，用在HTML页面最前面的标题中。页面本身存储在一个单独的文件
# "templates/header.html"中，可以根据需要替换标题
def include_header(the_title):
    # 打开模块文件(HTML),读入文件，换入所提供的"标题"。
    with open("templates/header.html") as headf:
        head_text = headf.read()
    hearder = Template(head_text)
    return (hearder.substitute(title=the_title))


# 与include_header函数类似，这个函数使用一个字符串作为参数，来创建一个HTML页面的尾部。页面
# 本身存储在一个单独的文件templates/footer.html中，参数用于动态地创建一组HTML链接标记。
# 从这些标记的使用来看，参数应当是一个字典。
def include_footer(the_links):
    with open("templates/footer.html") as footf:
        foot_text = footf.read()
    link_string = ''
    # 打开模块文件(HTML),读入文件，换入"the_links"中提供的HTML链接字典。
    for key in the_links:
        # 将链接字典转换为一个字符串，然后再换入模板      HTML在字符串中加入空格的一种强制做法&nbsp;
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return footer.substitute(links=link_string)


# 这个函数返回表单最前面的HTML，允许调用者指定URL（表单数据将发送到这个URL）,还可以指定所要使用的方法。
def start_form(the_url, form_type="POST"):
    return ('<form action="' + the_url + '" method="' + form_type + '">')


# 这个函数返回表单末尾的HTML标记，同时还允许调用者定制表单"submit"(提交)按钮的文本。
def end_form(submit_msg="Submit"):
    return ('<p></p><input type=submit value="' + submit_msg + '"></form>')


# 给定一个单选按钮名和值，创建一个HTML单选按钮（通常包括在一个HTML表单中）。注意：两个参数都是必要的。
def radio_button(rb_name, rb_value):
    return ('<input type="radio" name="' + rb_name + '"value="' + rb_value + '">' + rb_value + '<br />')


# 给定一个项列表，这个函数会把该列表转换为一个HTML无序列表。一个简单的for循环就可以完成全部工作。
# 每次迭代会向ul元素增加一个li元素。
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return (u_string)


# 创建并返回一个HTML标题标记(H1、H2、H3)，默认为2级标题。“header_text”参数是必要的
def header(header_text, header_level=2):
    return ('<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>')


# 用HTML段落标记包围一个文本段（一个字符串）。好像有些没必要，是不是？
def para(para_text):
    return ('<p>' + para_text + '</p>')


print(start_response())
print(start_response("text/plain"))
print(start_response("application/json"))
# print(include_header("Welcome to my home on the web!"))
# print(include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'}))
for fab in ['John', 'Paul', 'George', 'Ringo']:
    # <input type="radio" name="John"value="John">John<br />
    # <input type="radio" name="Paul"value="Paul">Paul<br />
    # <input type="radio" name="George"value="George">George<br />
    # <input type="radio" name="Ringo"value="Ringo">Ringo<br />
    print(radio_button(fab, fab))

# <ul><li>Life of Brian</li><li>Holy Grail</li></ul>
print(u_list(['Life of Brian', 'Holy Grail']))
# <h2>Welcome to my home on the web</h2>
print(header("Welcome to my home on the web"))
# <h5>This is a sub-sub-sub-sub heading</h5>
print(header("This is a sub-sub-sub-sub heading", 5))

# <p>Was it worth the wait? We hope it was...</p>
print(para("Was it worth the wait? We hope it was..."))
