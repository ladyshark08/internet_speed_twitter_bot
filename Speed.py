from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class InternetSpeedTwitter:
    def __init__(self, down, up):
        self.up = up
        self.down = down
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH, '// *[ @ id = "container"] / div / div[3] / div / div / div / '
                                                       'div[2] / div[3] / div[1] / a')
        go_button.click()
        time.sleep(60)
        download_score = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                            '1]/div/div[2]/span')
        upload_score = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                          '3]/div[3]/div/div[3]/div/div/div[2]/div['
                                                          '1]/div[2]/div/div[2]/span')
        final_down = float(download_score.text)
        final_up = float(upload_score.text)
        if final_down < self.down or final_up < self.up:
            return f"Hey Internet Provider, why is my internet speed {final_down} down/{final_up} up when I pay for {self.down}/{self.up}?"
        # print(f"down: {download_score.text}\nup:{upload_score.text}")

    def tweet_at_provider(self, email, password, message):
        self.driver.get("https://twitter.com/")
        time.sleep(2)
        sign_in_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div['
                                                            '1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        sign_in_button.click()
        time.sleep(4)
        email_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div['
                                                         '2]/div/input')
        email_field.send_keys(email)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')

        next_button.click()
        time.sleep(2)

        username_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div['
                                                            '2]/label/div/div[2]/div/input')
        username_field.send_keys("@m43217438")
        time.sleep(1)
        sec_next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div['
                                                             '2]/div[2]/div/div/div[2]/div[2]/div['
                                                             '2]/div/div/div/div/div/span/span')

        sec_next_button.click()
        time.sleep(1)

        password_field = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                            '3]/div/label/div/div[2]/div[1]/input')
        password_field.send_keys(password)

        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')

        login_button.click()
        time.sleep(2)
        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                         '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                         '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                                         '1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_field.send_keys(message)
        time.sleep(2)
        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                         '1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                         '2]/div[2]/div/div/div/div[3]/div')

        post_button.click()
