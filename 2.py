#coding=utf-8
from appium import webdriver
import time
import unittest
import HTMLTestRunner

caps = {}
caps["platformName"] = "Android"
caps["appPackage"] = "com.whty.eschoolbag.teachercontroller"
caps["appActivity"] = "com.whty.eschoolbag.teachercontroller.AppActivity"
caps["deviceName"] = "demo"
caps["noReset"] = True
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
def findItem(el):
    source = driver.page_source
    if el in source:
        return True
    else:
        return False




driver.implicitly_wait(10)
try:
    print(time.ctime())
    el1 = driver.find_element_by_xpath("//*[@text='文博']")
    el1.click()
except RuntimeError as e:
    print(e)

a="随堂拍摄"
print(findItem(a))



