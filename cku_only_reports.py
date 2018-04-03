from selenium import webdriver


driver=webdriver.Chrome("C:\\Users\\T440s\\Desktop\\Selenium\\chromedriver.exe")

#Script navigates to Reports section
driver.get("https://www.myf2b.com/reports/reports_landing_page")
driver.maximize_window()

#Logging in as a Teacher with valid credentials
driver.find_element_by_id("login").send_keys("leomessi")
driver.find_element_by_name("password").send_keys("leomessi")
driver.implicitly_wait(5)
driver.find_element_by_name("commit").click()

#Verifying that script has landed on Reports section
print(driver.title)
assert "Reports" in driver.title

#Navigating to CKU only reports
driver.find_element_by_xpath('//*[@id="center_reports"]/div[3]/div/div[2]/a/img').click()

#Navigating to the specific class
driver.find_element_by_xpath('//*[@id="student_classes"]/tbody/tr/td[3]/a/img').click()

#Navigating to the specific students reports- In this case Autotest student
driver.find_element_by_xpath('//*[@id="report"]/table[2]/tbody/tr[3]/td[1]/a').click()

#getting the number of words read
words = driver.find_element_by_xpath('//*[@id="report"]/table[1]/tbody/tr/td[1]')
print("Your number of words read is : ", words.text)

#getting the number of in-game time
time = driver.find_element_by_xpath('//*[@id="report"]/table[1]/tbody/tr/td[4]')
print('Your total in-game time is: ', time.text)
