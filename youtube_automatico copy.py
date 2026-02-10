from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

pesquisa = (input('Qual canal quer ver?: '))

time.sleep(5)

browser = Chrome()
wait = WebDriverWait(browser, 15)

linkk = "https://www.youtube.com/"
browser.get(linkk)

time.sleep(3)

search_bar = browser.find_element(By.NAME, "search_query")

search_bar.click()

search_bar.send_keys(pesquisa)

search_bar.submit()

time.sleep(3)

entrar = browser.find_element(By.ID, "channel-title")

entrar.click()

time.sleep(3)

browser.get(browser.current_url + "/videos")
time.sleep(5)

primeiro_video = browser.find_element(By.ID, "thumbnail")

primeiro_video.click()

time.sleep(3)

browser.find_element(By.TAG_NAME, "body").send_keys("f")


time.sleep(50)
#rowser.quit()
