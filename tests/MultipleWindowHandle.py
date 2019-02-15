import time

from selenium import webdriver

browser = 'chrome'

if browser == 'chrome':
    driver = webdriver.Chrome(executable_path="C:/Users/rahul/PycharmProjects/All_Class/drivers/chromedriver.exe")
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/rahul/PycharmProjects/All_Class/drivers/geckodriver.exe")
elif browser == 'ie':
    driver = webdriver.Ie(executable_path="C:/Users/rahul/PycharmProjects/All_Class/drivers/IEDriverServer.exe")
else:
    print("Provide appropriate browser name")

driver.get("https://phptravels.com/demo/")
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_xpath("//*[@class='login']").click()
time.sleep(5)
handles = driver.window_handles;
size = len(handles)
print(type(handles))
print(size)
parent_handle = driver.current_window_handle
print(parent_handle)
for x in range(size):
    if handles[x] != parent_handle:
        driver.switch_to.window(handles[x])
        print(driver.title)
        driver.find_element_by_xpath("//*[@name='username']").send_keys("Test")
        time.sleep(5)
        driver.close()
        break

driver.switch_to.window(parent_handle);
driver.find_element_by_xpath("//*[@class='login']").click()
time.sleep(10)
driver.quit()