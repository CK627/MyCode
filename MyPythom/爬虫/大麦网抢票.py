import os
import time
import pickle
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

damai_url = 'https://www.damai.cn/'
login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'
target_url = 'https://detail.damai.cn/item.htm?spm=a2oeg.search_category.0.0.749a2ecbX3EHsb&id=699777108426&clicktitle=KY%E4%B9%90%E5%9B%A2%E2%80%9C%E5%85%89%E8%BE%89%E5%B2%81%E6%9C%88%E2%80%9D%E7%BA%AA%E5%BF%B5%E9%BB%84%E5%AE%B6%E9%A9%B9%C2%B7%E8%87%B4%E6%95%ACBEYOND%E5%9B%9B%E5%8D%81%E5%91%A8%E5%B9%B4%E5%B7%A1%E5%9B%9E%E8%A7%86%E5%90%AC%E6%BC%94%E5%94%B1%E4%BC%9A%E2%80%94%E2%80%94(%E4%B8%8A%E6%B5%B7%E7%AB%99%EF%BC%89%E9%BB%84%E8%B4%AF%E4%B8%AD%E5%8A%9B%E8%8D%90%E7%9A%84%E5%A3%B0%E9%9F%B3'

class Concert:
    def __init__(self):
        self.status = 0
        self.login_method = 1
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
    def set_cookies(self):
        self.driver.get(damai_url)
        print('###请点击登录###')
        while self.driver.title.find('大麦网-全球演出赛事官方购票平台') != -1:
            sleep(1)
        print('###请扫码登录###')
        while self.driver.title != '大麦网-全球演出赛事官方购票平台-100%正品、先付先抢、在线选座！':
            sleep(1)
        print('###扫码成功###')
        pickle.dump(self.driver.get_cookies(), open('cookies.pkl', 'wb'))
        print('###cookie保存成功###')
        self.driver.get(target_url)
    def get_cookie(self):
        cookies = pickle.load(open('cookies.pkl', 'rb'))
        for cookie in cookies:
            cookie_dict = {
                'domain': '.damai.cn',
                'name': cookie.get('name'),
                'value': cookie.get('value')
            }
            self.driver.add_cookie(cookie_dict)
        print('###载入cookie###')

    def login(self):
        if self.login_method == 0:
            self.driver.get(login_url)
            print('###开始登录###')
        elif self.login_method == 1:
            if not os.path.exists('cookies.pkl'):
                self.set_cookies()
            else:
                self.driver.get(target_url)
                self.get_cookie()

    def enter_concert(self):
        print('###打开浏览器,进入大麦网###')
        self.login()
        self.driver.refresh()
        self.status = 2
        print('###登录成功###')
        if self.isElementExist('/html/body/div[2]/div[2]/div/div/div[3]/div[2]'):
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[3]/div[2]').click()
    def choose_ticket(self):
        if self.status == 2:
            print('=' * 30)
            print('###开始进行日期及票价选择###')
            while self.driver.title.find("确认订单") == -1:
                try:
                    buybutton = self.driver.find_element(By.CLASS_NAME, 'buybtn').text
                    if buybutton == '提交缺货登记':
                        self.status = 2
                        self.driver.get(target_url)
                    elif buybutton == '立即预定':
                        self.driver.find_element('buybtn').click()
                        self.status = 3
                    elif buybutton == '立即购买':
                        self.driver.find_element(By.CLASS_NAME, 'buybtn').click()
                        self.status = 4
                    elif buybutton == '选座购买':
                        self.driver.find_element(By.CLASS_NAME, 'buybtn').click()
                        self.status = 5
                except:
                    print('###没有跳转到订单结算界面###')
                title = self.driver.title
                if title == '选座购买':
                    self.choice_seats()
                elif title == '确认订单':
                    while True:
                        print('正在加载.......')
                        if self.isElementExist('//*[@id="container"]/div/div[9]/button'):
                            self.check_order()
                            break

    def choice_seats(self):
        while self.driver.title == '选座购买':
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[1]/div[2]/img'):
                print('请快速选择你想要的座位!!!')
            while self.isElementExist('//*[@id="app"]/div[2]/div[2]/div[2]/div'):
                self.driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div[2]/div[2]/button').click()

    def check_order(self):
        if self.status in [3, 4, 5]:
            print('###开始确认订单###')
            time.sleep(1)
            try:
                self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/div[2]/div[1]/div/label').click()
            except Exception as e:
                print('###购票人信息选中失败, 自行查看元素位置###')
                print(e)
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[9]/button').click()
            time.sleep(20)

    def isElementExist(self, element):
        flag = True
        browser = self.driver
        try:
            browser.find_element(By.XPATH, element)
            return flag
        except:
            flag = False
            return flag

    def finish(self):
        self.driver.quit()


if __name__ == '__main__':
    con = Concert()
    try:
        con.enter_concert()
        con.choose_ticket()
    except Exception as e:
        print(e)
        con.finish()

