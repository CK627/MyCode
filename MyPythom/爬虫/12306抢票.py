from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from selenium.webdriver.common.keys import Keys
import time
import select


def isElementExist(driver):
    flag=True
    ele = driver.find_elements(by=By.CLASS_NAME, value='btn72')
    if len(ele) == 0:
        flag = False
        return flag
    if len(ele) == 1:
        return flag
    else:
        flag = False
        return flag


def get_ticket(conf, driver, url):
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined})"""})
    driver.maximize_window()
    driver.get(url)
    driver.implicitly_wait(5)
    login = driver.find_element(by=By.ID, value='J-btn-login')
    login.click()
    driver.implicitly_wait(10)
    username_tag = driver.find_element(by=By.ID, value='J-userName')
    username_tag.send_keys(conf.username)
    password_tag = driver.find_element(by=By.ID, value='J-password')
    password_tag.send_keys(conf.password)
    login_now = driver.find_element(by=By.ID, value='J-login')
    login_now.click()
    time.sleep(2)
    picture_start = driver.find_element(by=By.ID, value='nc_1_n1z')
    ActionChains(driver).move_to_element(picture_start).click_and_hold(picture_start).move_by_offset(300, 0).release().perform()

    try:
        driver.find_element(by=By.XPATH, value='//div[@class="dzp-confirm"]/div[2]/div[3]/a').click()
        driver.implicitly_wait(5)
    except:
        pass

    driver.find_element(by=By.XPATH, value='//*[@id="link_for_ticket"]').click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').clear()
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').send_keys(conf.fromstation)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').send_keys(Keys.ENTER)
    destination_tag = driver.find_element(by=By.XPATH, value='//*[@id="toStationText"]')
    destination_tag.click()
    destination_tag.clear()
    destination_tag.send_keys(conf.destination)
    time.sleep(1)
    destination_tag.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)
    date_tag = driver.find_element(by=By.XPATH, value='//*[@id="train_date"]')
    date_tag.click()
    date_tag.clear()
    date_tag.send_keys(conf.date)
    time.sleep(1)
    query_tag = driver.find_element(by=By.XPATH, value='//*[@id="query_ticket"]')

    start = time.time()

    while True:
        driver.implicitly_wait(5)
        driver.execute_script("$(arguments[0]).click()", query_tag)
        if not isElementExist(driver):
            print(f"15点30分起售，现在是{time.strftime('%H:%M:%S', time.localtime())}，还未开始售票")
            if time.time() - start >= 120:
                driver.refresh()
                start = time.time()
            time.sleep(1)
            continue

        tickets = driver.find_elements(by=By.XPATH, value='//*[@id="queryLeftTable"]/tr')
        tickets = [tickets[i] for i in range(len(tickets) - 1) if i % 2 == 0]
        for ticket in tickets:
            if ticket.find_element(by=By.CLASS_NAME,value='number').text == conf.trainnumber and ticket.find_element(by=By.XPATH, value='//td[8]').text != "候补":
                ticket.find_element(by=By.CLASS_NAME, value='btn72').click()
                driver.find_element(by=By.XPATH, value='//*[@id="normalPassenger_0"]').click()
                driver.find_element(by=By.XPATH, value='//*[@id="submitOrder_id"]').click()
                try:
                    driver.find_element(by=By.XPATH, value='//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1F"]').click()
                except:
                    pass
                driver.find_element(by=By.ID, value='qr_submit_id').click()
                print(f"{conf.trainnumber}次列车抢票成功，请尽快在10分钟内支付！")
                return

if __name__ == '__main__':
    conf = Config()
    url = 'https://www.12306.cn/index/'
    s = Service('../venv/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe')
    driver = webdriver.Chrome()
    get_ticket(conf, driver, url)
    time.sleep(10)
    driver.quit()
