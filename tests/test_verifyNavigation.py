import pytest

from Config.config import TestData
from pages.verifyNavigation import AutoDemoNavigation


@pytest.mark.usefixtures("setup")
class TestNavigation:

    def test_verify_nav(self):
        self.nav = AutoDemoNavigation(self.driver)
        self.driver.refresh()
        confirm_women_page = self.nav.verify_nav()
        assert confirm_women_page == TestData.confirm_page

    def test_verify_checkout(self):
        self.nav = AutoDemoNavigation(self.driver)
        self.driver.refresh()
        self.nav.verify_nav()
        self.driver.refresh()
        self.nav.verify_checkout()
        self.driver.refresh()
        #verify_price, verify_size = self.nav.verify_checkout()
       # assert verify_price == "PLN70.65"

    def test_verify_cart(self):
        self.nav = AutoDemoNavigation(self.driver)
        self.driver.refresh()
        self.nav.verify_cart()
        no_item_confirm = self.nav.verify_cart()
        assert no_item_confirm == TestData.no_item






