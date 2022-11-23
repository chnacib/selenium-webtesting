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
    title = "teste"
    assert title == driver.title
    sleep(5)

test_website()
