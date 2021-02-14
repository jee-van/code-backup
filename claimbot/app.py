# a robot which claim etherium itselef

from selenium import webdriver
import time
import os

email = os.environ['MAIL_ID']
password = os.environ['PASSWORD']

browser = webdriver.Chrome()
browser.get('https://ethereumfree.info/')

login1 = browser.find_element_by_link_text('Login')
login1.click()


def Login():
    email_form = browser.find_element_by_class_name('email-input')
    email_form.send_keys(email)

    password_form = browser.find_element_by_class_name('pass-input')
    password_form.send_keys(password)

    time.sleep(2)

    login2 = browser.find_element_by_id('btnform')
    login2.click()
    

def Claim():
    time.sleep(4)
    claim = browser.find_element_by_xpath("//div[@class='center-container']/div[@class='faucet-container']/div[text()='Claim Now']")
    claim.click()


Login()
Claim()

time.sleep(5)

minutes = browser.find_element_by_xpath("//div[@class='time']/div[@class='counter']/p[@class='title minutes']").text

if int(minutes) > 5:
    Claim()
    time.sleep(5)

browser.quit()
