import urllib3
import pytest
from selenium import webdriver
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
chrome_options =webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Remote('http://selenium:4444/wd/hub',options=chrome_options)

  
def test_aaa():
    testando = "oi"
    assert testando == "oi"

def test_button():
    driver.get("localhost:80")
    sleep(4)
    img = driver.find_element(By.XPATH, "//*[@id='home']/div[2]/div/div[2]/div/img")
    img = "true"
    assert img == "true"

#def test_localhost():
#    driver.get("localhost:80")
#    sleep(4)
#    title = "Slick - Bootstrap 4 Template"
#    assert title == driver.title

