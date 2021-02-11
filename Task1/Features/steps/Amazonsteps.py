import time

from behave import *

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    executable_path="C:/Users/hanna/Downloads/chromedriver_win32/chromedriver_win.exe")

@given(u'browser is open')
def step_impl(context):
    context.driver = driver
    context.driver.get("https://www.amazon.de")
    context.driver.maximize_window()
    time.sleep(1)


@given(u'user is on Amazon search page and accepts the cookies')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//input[@name='accept']").click()
    except:
        pass


@when(u'user enters "{thing}"  in search box and hits enter')
def step_impl(context, thing):
    context.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys(thing)
    context.driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").submit()


@when(u'clicks Sort by: Price: Low to High button')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[@class='a-dropdown-prompt']").click()
    time.sleep(1)
    context.driver.find_element_by_xpath("//a[@id='s-result-sort-select_1']").click()
    time.sleep(1)

@when(u'clicks the first "{thing}"  product')
def step_impl(context, thing):
    context.driver.find_elements_by_xpath("//a[@class='a-link-normal a-text-normal']")[0].click()
    time.sleep(1)


@when(u'clicks the show all option')
def step_impl(context):
    context.driver.find_element_by_xpath("//span[@class='a-button-inner']")
    time.sleep(1)
    context.driver.find_element_by_xpath("//a[@id='buybox-see-all-buying-choices-announce']").click()
    time.sleep(1)

@when(u'clicks add to cart of the first "{thing}"  product and check the price')
def step_impl(context, thing):
    context.driver.find_element_by_xpath("//span[@class='a-button-inner']")
    time.sleep(1)
    context.driver.find_element_by_xpath("//input[@name='submit.addToCart']").click()
    time.sleep(1)
    context.driver.find_element_by_xpath("//span[@id='nav-cart-count']").click()
    time.sleep(1)



@Then(u'user clicks the cart')
def step_impl(context):
    text = context.driver.find_element_by_xpath("//span[@id='nav-cart-count']").text
    if text == "2":
        context.driver.find_element_by_xpath("//span[@class='a-button-inner']")
        time.sleep(1)
        context.driver.find_element_by_xpath("//input[@name='proceedToRetailCheckout']").click()
        time.sleep(1)
        context.driver.close()








