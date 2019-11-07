from selenium import webdriver

broswer=webdriver.Firefox()
broswer.get('http://inventwithpython.com/')
linkElem=broswer.find_element_by_link_text('Read Online for Free')
print(type(linkElem))
linkElem.click()