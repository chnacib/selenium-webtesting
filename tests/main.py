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


def test_website():
    driver = webdriver.Remote('http://selenium:4444/wd/hub',options=webdriver.ChromeOptions())
    remote_url = "https://www.google.com"
    driver.get(remote_url)
    driver.maximize_window()
    #check title
    title = "Google"
    assert title == driver.title
    text_box = driver.find_element(By.NAME,"q")
    text_box.send_keys("python.org")
    text_box.send_keys(Keys.ENTER)
    sleep(2)
    try:
        search_response = driver.find_element(By.ID,"result-stats")
        search_response = True
    except:
        search_response = False
    
    assert search_response == True, "Search didn't worked or page not loaded"
    
    link = driver.get("https://www.python.org/")
    sleep(4)
    link_url = driver.current_url
    assert link_url == "https://www.python.org/"


    driver.close()

test_website()
