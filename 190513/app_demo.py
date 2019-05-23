# -*- coding:utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_login")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
el3.click()
el5 = driver.find_element_by_xpath("//android.view.ViewGroup[@content-desc=\"第 3 屏，共 3 屏\"]/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[7]")
el5.click()
el6 = driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
el6.click()
el7 = driver.find_element_by_id("com.xueqiu.android:id/tv_login")
el7.click()
el8 = driver.find_element_by_id("com.xueqiu.android:id/rl_login_by_wx")
el8.click()
el9 = driver.find_element_by_id("android:id/navigationBarBackground")
el9.click()

driver.quit()