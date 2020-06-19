text_to_be_posted='your post message here'
group_links=['https://www.facebook.com/groups/#########','https://www.facebook.com/groups/#############'] #groups links here

from bs4 import BeautifulSoup
import time
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications");
options.add_argument('--headless')
#edit the chromedriver path to path in your PC
driver = webdriver.Chrome(executable_path=r'C:/Users/saini/Downloads/chromedriver_win32/chromedriver.exe',chrome_options=options)
driver.maximize_window()
driver.delete_all_cookies()
url = 'https://www.facebook.com/' # 
driver.get(url)

print("entering login details")
login=driver.find_element_by_xpath("//input[contains(@name, 'email')]")
login.send_keys("####@email.com") #enter email for bot account

password=driver.find_element_by_xpath("//input[contains(@name, 'pass')]")
password.send_keys("#########") #enter password
submit=driver.find_element_by_xpath("//input[contains(@type, 'submit')]")
submit.click()

for i in group_links:
    time.sleep(6)
    driver.get(i)
    print(i)
    time.sleep(4)
    status_upddd=driver.find_element_by_xpath("//textarea[contains(@placeholder, 'Write something...')]")
    status_upddd.click()
    time.sleep(2)
    status_upd=driver.find_element_by_xpath("//div[contains(@role, 'combobox')]")
    status_upd.send_keys(text_to_be_posted)
    submit_stat=driver.find_element_by_xpath("//span[.='Post']")
    submit_stat.click()
    print('Done')
