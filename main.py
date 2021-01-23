from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent

insta_id = ''
insta_pas = ''
# insta_id = ''
# insta_pas = ''

# accounts = ['iloveaurangabad','nagpalgroup','khinvasararealty']
accounts = ['iloveaurangabad']

class InstaFollower:

    def __init__(self):
        options = Options()
        # ua = UserAgent()
        # userAgent = ua.random
        userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        options.add_argument(f'user-agent={userAgent}')
        chrome_drive_path = "G:\Some useful Sofwares\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_drive_path)


    def login(self,insta_id,insta_pas):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(insta_id)
        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(insta_pas)
        password.send_keys(Keys.ENTER)

    def find_followers(self,account_name):
        time.sleep(3)
        self.driver.get(f'https://www.instagram.com/{account_name}')
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        no_of_followers = self.driver.find_element_by_class_name('g47SY').text
        time.sleep(2)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for _ in range(3):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(0.5)
        time.sleep(1)
        followers_list = self.driver.find_elements_by_class_name('sqdOP')
        # print(followers_list)
        # print(len(followers_list))
        time.sleep(2)
        for each in followers_list:
            try:
                each.click()
            except ElementClickInterceptedException:
                try:
                    self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
                    time.sleep(1)
                except NoSuchElementException:
                    pass

            time.sleep(1)


obj = InstaFollower()
obj.login(insta_id, insta_pas)

for account_name in accounts:
    obj.find_followers(account_name)
