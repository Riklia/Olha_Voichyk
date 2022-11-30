from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

username = 'Admin'
password = 'admin123'

delay_to_load_page = 10

emp_name = 'RandomName'

class PayGradesTest():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(EC.presence_of_element_located((By.XPATH, '//input['
                                                      '@name="username"]'))).send_keys(username)
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def main_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(EC.presence_of_element_located(
            (By.XPATH, '//span[text()="Admin"]'))).click()
        WebDriverWait(self.driver, delay_to_load_page).until(EC.presence_of_element_located(
            (By.XPATH, '//span[contains(text(),"Job")]'))).click()
        self.driver.find_element(By.XPATH, '//a[contains(text(),"Pay Grades")]').click()
        WebDriverWait(self.driver, delay_to_load_page).until(EC.presence_of_element_located(
            (By.XPATH, '//button[contains(.,"Add")]'))).click()

    def pay_grades_page(self):
        WebDriverWait(self.driver, delay_to_load_page).until(EC.presence_of_element_located(
            (By.XPATH, '//input[not(@placeholder)]'))).send_keys(emp_name)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Save")]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Add")]').click()

        self.driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]').click()
        self.driver.find_element(By.XPATH,'//span[contains(text(),"USD - United States Dollar")]').click()
        first_input, second_input = self.driver.find_elements(By.XPATH,
                                                              '//input[@class="oxd-input oxd-input--active"]')[2:]
        first_input.send_keys("80000")
        second_input.send_keys("150000")
        self.driver.find_elements(By.XPATH, '//button[contains(.,"Save")]')[1].click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Cancel")]').click()

    def check_record(self):
        xpath_check = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{emp_name}")]'
        found = WebDriverWait(self.driver, delay_to_load_page).until(EC.presence_of_element_located((By.XPATH, xpath_check)))
        found.find_element(By.XPATH, f'//div[contains(., "{emp_name}")]')
        found.find_element(By.XPATH, '//div[contains(., "United States Dollar")]')

    def remove_record_check(self):
        xpath_delete = f'//div[@class="oxd-table-row oxd-table-row--with-border" and contains(., "{emp_name}")]//i[@class="oxd-icon bi-trash"]'
        self.driver.find_element(By.XPATH, xpath_delete).click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[contains(.,"Yes, Delete")]').click()
        time.sleep(5)
        try:
            self.driver.find_element(By.XPATH, xpath_delete)
            assert 'Element was not removed'
        except NoSuchElementException:
            pass
        self.driver.close()
