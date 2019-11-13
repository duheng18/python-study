'''
2048
2048 是一个简单的游戏，通过箭头向上、下、左、右移动滑块，让滑块合并.实际上,你可以通过一遍
一遍的重复“上、右、下、左”模式，获得相当高的分数。编写一个程序，打开
https://gabrielecirulli.github.io/2048/上的游戏，不断发送上、右、下/左按键，自动玩游戏。
'''
# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
url = 'https://gabrielecirulli.github.io/2048/'
browser.get(url)
game_elem = browser.find_element_by_class_name('game-container')
while True:
    retry_elem = browser.find_element_by_class_name('retry-button')
    # new game
    if retry_elem.text == 'Try again':
        retry_elem.click()
        game_elem = browser.find_element_by_class_name('game-container')
    game_elem.send_keys(Keys.UP)
    game_elem.send_keys(Keys.RIGHT)
    game_elem.send_keys(Keys.DOWN)
    game_elem.send_keys(Keys.LEFT)
