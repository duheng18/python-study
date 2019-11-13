'''
编写一个程序，通过命令行接受电子邮件地址和文本字符串。然后利用selenium登录到你的邮件账号，
将该字符串作为邮件,发送到提供的地址（你也许希望为这个程序建立一个独立的邮件账号）。这是为
程序添加通知功能的一种好方法。你也可以编写类似的程序，从Facebook或Twitter账号发送消息。 
'''
from selenium import webdriver
import sys, time

if len(sys.argv) != 4:
    print('Wrong format!!!')
    print('Usage: python program.py <address> <title> <content>')
    sys.exit()

address = sys.argv[1]
title = sys.argv[2]
content = sys.argv[3]

# Go to the 163 mail page
url = 'https://mail.163.com/'
browser = webdriver.Firefox()
browser.get(url)
time.sleep(3)

# Write the login information and click login button
browser.switch_to.frame('x-URS-iframe')
browser.find_element_by_name('email').send_keys('a74327833')
browser.find_element_by_name('password').send_keys('8859507388595073')
browser.find_element_by_id('dologin').click()
time.sleep(3)

# Click write letter button
browser.find_element_by_id('_mail_component_69_69').click()
time.sleep(3)

# Write address, title and content
browser.find_element_by_class_name('nui-editableAddr-ipt').send_keys(f"{address}")
browser.find_elements_by_class_name("nui-ipt-input")[2].send_keys(f"{title}")
browser.switch_to.frame(browser.find_element_by_class_name('APP-editor-iframe'))
browser.find_element_by_class_name('nui-scroll').send_keys(f"{content}")

# Click send letter button
browser.find_elements_by_class_name("nui-btn-text")[2].click()
time.sleep(10)
browser.quit()