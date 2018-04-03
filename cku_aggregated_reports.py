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

#Navigating to cku aggregated reports
driver.find_element_by_xpath('//*[@id="center_reports"]/div[3]/div/div[1]/a/img').click()

#Searching for specific student
driver.find_element_by_xpath('//*[@id="nav_reports"]/a[2]').click()
driver.find_element_by_xpath('//*[@id="first_name"]').send_keys('Autotest')
driver.find_element_by_xpath('//*[@id="student_id"]').send_keys('123qa')
driver.find_element_by_xpath('//*[@id="search"]').click()

#Checking words read for aggregated reports
aggregated_words = driver.find_element_by_xpath('//*[@id="table"]/tbody[2]/tr[1]/td[11]')
print('Total amount of words read for words read: ', aggregated_words.text)

#Checking total in game time for both apps
ingame_time = driver.find_element_by_xpath('//*[@id="table"]/tbody[2]/tr[1]/td[12]')
print('Total ingame time is: ', ingame_time.text)