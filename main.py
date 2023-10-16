import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Browser:
    browser, service, chromeOptions = None, None, None

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
        self.handle_cookies()
        self.add_input(by=By.ID, value='customer_login_email', text=username)
        self.add_input(by=By.ID, value='customer_login_password', text=password)

        self.check_eCAPTCHA_box()
        time.sleep(4)

        self.click_button(by=By.XPATH, value='//*[@id="shopfront-app"]/div[4]/div/section/div[2]/div/div[1]/div/div/div/div[1]/form/div[7]/div/button')

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
        WebDriverWait(self.browser, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

    def handle_cookies(self):
        cookieButton = self.browser.find_element(By.CLASS_NAME, 'cookies-banner-module_dismiss-button_24Z98')
        cookieButton.click()

if __name__ == '__main__':
    browser = Browser('drivers/chromedriver')

    # opening the page
    browser.open_page('https://www.takealot.com/account/login')
    # time.sleep(1)

    browser.login_takealot('techsavvy094@gmail.com', 'Techsavvy@123')
    time.sleep(10)

    # login via google
    # browser.login_to_takealot_by_google()
    # time.sleep(10)


    browser.close_browser()