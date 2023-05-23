import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/web_driver/chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service=service_obj, options=options)
driver.get("https://msys.keka.com/")

driver.maximize_window()
driver.implicitly_wait(35)

driver.find_element(By.CLASS_NAME,"login-option").click()
driver.find_element(By.ID,"identifierId").send_keys("vhirandagi@msystechnologies.com")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()
driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input").send_keys("Vishal#1432")
driver.find_element(By.XPATH,'//*[@id="passwordNext"]/div').click()
driver.find_element(By.XPATH,'//*[@id="accordion"]/li[2]').click()
driver.find_element(By.XPATH,'/html/body/xhr-app-root/div/employee-me/div/ul/li[2]').click()
driver.find_element(By.XPATH,'/html/body/xhr-app-root/div/employee-me/div/employee-attendance/div/div/div/employee-attendance-stats/div/div[3]/employee-attendance-request-actions/div/div/div/div/div[2]/div/div[2]/a[1]').click()
driver.find_element(By.XPATH,'/html/body/modal-container/div[2]/div/employee-attendance-working-remotely-request/div[2]/form/div/div/div[1]/div[1]/div[1]/div/span[2]').click()

today_date = driver.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[4]/td[3]/span').click()
today_date = driver.find_element(By.XPATH,'/html/body/bs-daterangepicker-container/div/div/div/div/bs-days-calendar-view[1]/bs-calendar-layout/div[2]/table/tbody/tr[4]/td[3]/span').click()
print(today_date)
driver.find_element(By.XPATH,'body > modal-container > div.modal-dialog.small-modal > div > employee-attendance-working-remotely-request > div.modal-footer > button.btn.btn-primary').click()

