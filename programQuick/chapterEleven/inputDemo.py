from selenium import webdriver

browser=webdriver.Firefox()
browser.get('https://mail.qq.com/cgi-bin/loginpage')
emailElem=browser.find_element_by_name('u')
emailElem.clear()
emailElem.send_keys('1043175779@qq.com')
passwordElem=browser.find_element_by_name('p')
passwordElem.clear()
passwordElem.send_keys('dh18810075728')
passwordElem.submit()