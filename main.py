import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_takealot(self, username: str, password: str):
        self.add_input(by=By.ID, value='customer_login_email', text=username)
        self.add_input(by=By.ID, value='customer_login_password', text=password)

        self.click_button(by=By.XPATH, value='//*[@id="body"]/div[10]/div/div/div/div/div/div/div[1]/div/div/div[1]/form/div[7]/div/button')

    def login_to_takealot_by_google(self):
        self.click_button(by=By.CLASS_NAME, value='google-login-button-module_google-text_2VK9a')
        time.sleep(6)
        self.add_input(by=By.XPATH, value='//*[@id="identifierId"]', text='techsavvy094@gmail.com')
        self.click_button(by=By.XPATH, value='//*[@id="identifierNext"]/div/button')
        time.sleep(3)
        self.add_input(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input', text='D3v3loper$z@')
        self.click_button(by=By.XPATH, value='//*[@id="passwordNext"]/div/button')
        time.sleep(4)


    def check_eCAPTCHA_box(self):
        iframe = self.browser.find_element(by=By.CLASS_NAME, value='recaptcha-checkbox ')
        self.browser.switch_to(iframe)

        checkbox = self.browser.find_element(by=By.CLASS_NAME, value='recaptcha-checkbox-border')
        checkbox.click()
        time.sleep(2)

        self.browser.switch_to.default_content()




if __name__ == '__main__':
    browser = Browser('drivers/chromedriver')

    # opening the page
    browser.open_page('https://www.takealot.com/')
    time.sleep(3)

    # clicking the login button to show the login form
    browser.click_button(By.XPATH, value='//*[@id="shopfront-app"]/div[2]/div/div/div[2]/div/div[1]/ul/li[1]/a')
    time.sleep(2)

    # validating if robot or not
    browser.check_eCAPTCHA_box()
    time.sleep(3)

    browser.login_takealot('techsavvy094@gmail.com', 'Techsavvy@123')
    time.sleep(10)

    # login via google
    # browser.login_to_takealot_by_google()
    # time.sleep(10)


    browser.close_browser()