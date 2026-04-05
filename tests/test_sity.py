import value
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from pages.homepage import HomePage
from pages.product import ProductPage

def test_open_s6(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    #driver.get("https://demoblaze.com/")
    #galaxy_s6 = driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
    #galaxy_s6.click()
    product_page = ProductPage(driver)
    product_page.check_title_is('Samsung galaxy s6')
    #title = driver.find_element(By.CSS_SELECTOR, 'h2')
    #assert title.text == 'Samsung Galaxy s6'
#УРА мой первый тестиииииик

def test_two_monitors(driver):
    homepage = HomePage(driver)
    homepage.open()
    homepage.click_monitor()
    #driver.get("https://demoblaze.com/")
    #monitor_link = driver.find_element(By.CSS_SELECTOR,  "[onclick=\"byCat('monitor')\"]")
    #monitor_link.click()
    time.sleep(3) #так делать плохо, просто пример
    homepage.check_products_count(2)
    product_page = ProductPage(driver)
    #monitors = driver.find_elements(By.CSS_SELECTOR, ".card")
    #assert len(monitors) == 2