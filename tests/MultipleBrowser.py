from selenium import webdriver

browser = 'ie'

if browser == 'chrome':
    driver = webdriver.Chrome(executable_path="C:/Users/rahul/PycharmProjects/All_Class/drivers/chromedriver.exe")
elif browser == 'firefox':
    driver = webdriver.Firefox(executable_path="C:/Users/rahul/PycharmProjects/All_Class/drivers/geckodriver.exe")
elif browser == 'ie':
    driver = webdriver.Ie(executable_path="C:/Users/rahul/PycharmProjects/All_Class/drivers/IEDriverServer.exe")
else:
    print("Provide appropriate browser name")

driver.get("http://facebook.com")
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element_by_id("email").send_keys("Test")
driver.find_element_by_id("pass").send_keys("Pass")
driver.find_element_by_id("u_0_2").click()
driver.quit()
