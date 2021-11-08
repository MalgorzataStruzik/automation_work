import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager import driver

from Locators.locators import Locators, Locators_cart
from Config.config import TestData
from pages.basePage import BasePage


class AutoDemoNavigation(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.base_url)

#1.Open website 2.Go to Clothes 3.Select Women 4.Verify that you on Women page
    def verify_nav(self):
        ActionChains(self.driver)
        first_level_menu = self.driver.find_element(By.XPATH, Locators.clothes_menu)
        ActionChains(self.driver).move_to_element(first_level_menu).perform()
        self.do_click((By.XPATH, Locators.clothes_woman))
        return self.get_element_text((By.XPATH, Locators.confirm_women))

# 1.On Women page and Select SizeM
# 2.Verify active filters
# 3.Click quick view in first product
# 4.Add Quantity 2
# 5.Click Add to Cart
# 6.Verify quantity
# 7.Verify total price
# 8.Click Proceed to Checkout

    def verify_checkout(self):
        self.selected_element((By.XPATH, Locators.size_m))
        ActionChains(self.driver)
        first_level_menu = self.driver.find_element(By.XPATH, Locators.quick_view_xpath)
        ActionChains(self.driver).move_to_element(first_level_menu).perform()
        self.do_click((By.XPATH, Locators.quick_view_click))
        self.do_click((By.XPATH, Locators.select_size_M))
        self.do_click((By.XPATH, Locators.up_quantity))
        self.do_click((By.XPATH, Locators.add_to_card))
        self.do_click((By.XPATH, Locators.go_to_checkout))
        verify_size = self.get_element_text((By.XPATH, Locators.confirm_size_m))
        verify_price = self.get_element_text((By.XPATH, Locators.confirm_total_price))
        self.do_click((By.XPATH, Locators.proces_to_checkout))
        return verify_price, verify_size




#Verify Cart
# 1.Add 3 Clothes to Cart
# 2.Go to Cart
# 3.Verify Shopping Cart
# 4.Delete all Clothes
# 5.Verify there are no more items in your cart
# 6.Click continue shopping
# 7.Verify main page

    def verify_cart(self):
        # add first item to cart
        self.do_click((By.XPATH, Locators_cart.first_add))
        self.do_click((By.XPATH, Locators_cart.add_co_cart_button))
        self.do_click((By.XPATH, Locators_cart.continue_shoping_button))
        self.do_click((By.XPATH, Locators_cart.home_button))
        # add second item to cart
        self.do_click((By.XPATH, Locators_cart.second_add))
        self.do_click((By.XPATH, Locators_cart.add_co_cart_button))
        self.do_click((By.XPATH, Locators_cart.continue_shoping_button))
        self.do_click((By.XPATH, Locators_cart.home_button))
        # add third item to cart
        self.do_click((By.XPATH, Locators_cart.third_add))
        self.do_click((By.XPATH, Locators_cart.add_co_cart_button))
        self.do_click((By.XPATH, Locators_cart.continue_shoping_button))
        #  Go to cart
        self.do_click((By.XPATH, Locators_cart.cart_button))
        # 3.Verify Shopping Cart
        self.get_element_text((By.XPATH, Locators_cart.confirm_shopping_cart))
        # 4.Delete all Clothes
        self.do_click((By.XPATH, Locators_cart.delete_button))
        self.driver.refresh()
        self.do_click((By.XPATH, Locators_cart.delete_button))
        self.driver.refresh()
        self.do_click((By.XPATH, Locators_cart.delete_button))
        # 5.Verify there are no more items in your cart
        no_item_con = self.get_element_text((By.XPATH, Locators_cart.no_items))
        # 6.Click continue shopping
        self.do_click((By.XPATH, Locators_cart.continue_button))
        # 7.Verify main page
        # main_page = self.get_element_text((By.XPATH, Locators_cart.confirm_main_page))
        return no_item_con





