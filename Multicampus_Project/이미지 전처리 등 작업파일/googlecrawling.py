from urllib.request import urlretrieve
from selenium.webdriver.common.by import By
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import urllib.request

search = 'チワワ'
url = f'https://www.google.com/search?q={quote_plus(search)}&sxsrf=APq-WBv-g2wTQpx6nyYB8xQypBBowrqZ9Q:1647328210419&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjPwL3mx8f2AhVws1YBHWqDBoEQ_AUoAXoECAIQAw&biw=1920&bih=937&dpr=1'

driver = webdriver.Chrome()
driver.get(url)
for i in range(500) :
    driver.execute_script('window.scrollBy(0,10000)')

SCROLL_PAUSE_TIME = 1
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height :
        try :
            driver.find_element(By.CSS_SELECTOR, '.mye4qd').click()
        except :
            break
    last_height = new_height

img = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
cnt = 1
for i in img:
    try:
        i.click()
        time.sleep(2)
        imgurl = driver.find_element(By.XPATH,
            '/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img').get_attribute("src")
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgurl, 'C:/project/チワワ/' + search + str(cnt) + '.jpg')
        cnt += 1
        if cnt == 400:
            break

    except:
        pass

driver.close()