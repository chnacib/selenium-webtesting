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

def test_website():   
    remote_url = "https://www.google.com"
    driver.get(remote_url)
    driver.maximize_window()
    #check title
    sleep(2)
    title = "Google"
    assert title == driver.title
  
def test_aaa():
    testando = "oi"
    assert testando == "oi"

def test_localhost():
    driver.get("127.0.0.1:80")
    sleep(2)
    title = "Slick - Bootstrap 4 Template"
    assert title == driver.title

