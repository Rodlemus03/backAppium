from appium import webdriver
import time
desired_caps=dict(
    devideName='Android',
    platformName='Android',
    browserName='Chrome'
)
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
driver.get('http://google.com')
print(driver.title)
time.sleep(2)
driver.quit()