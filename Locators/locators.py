from selenium.webdriver.common.by import By

class Locators:

    clothes_menu ="//div/ul/li[1]/a[@data-depth='0']"
    clothes_woman ="//div/ul/li[2][@id='category-5']"
    confirm_women = "//div/h1[contains(text(),'Women')]"

    #selec size M
    size_m = "//ul/li[2]//span[contains(@class,'custom-checkbox')]"
    select_size_M = "//div/select[@id='group_1']/option[@value='2']"
    confirm_size_m = "//div[contains(@class,'product-line-info')]/span[contains(text(),'M')]"
    verify_filters = "//section[contains(@class,'active_filters')]/ul/li"
    quick_view_xpath = "//div[contains(@class,'product-description')]"
    quick_view_click = "//div/a[contains(@class,'quick-view')]"
    up_quantity = "//span/button[contains(@class,'btn btn-touchspin js-touchspin bootstrap-touchspin-up')]"
    add_to_card = "//div/button[contains(@class,'btn btn-primary add-to-cart')]"
    quantity_confirm = "//div/span[@class='label js-subtotal']"
    total_price = "//div[@id='cart-subtotal-products']/span[contains(@class='value')]"
    confirm_total_price = "//div[contains(@class,'cart-summary-line cart-total')]/span[contains(text(),'PLN70.65')]"
    go_to_checkout = "//div/a[contains(text(),'Proceed to checkout')]"

    proces_to_checkout = "//div/a[contains(text(),'Proceed to checkout')]"

class Locators_cart:

    first_add = "//div/h1/a[contains(text(),'Hummingbird printed t-shirt')]"
    second_add = "//div/h1/a[contains(text(),'The best is yet to come')]"
    third_add = "//div/h1/a[contains(text(),'Today is a good day Framed...')]"
    home_button = "//div//a/span[contains(text(),'Home')]"
    continue_shoping_button = "//div/button[contains(text(),'Continue shopping')]"
    add_co_cart_button = "//div/button[contains(@class,'btn btn-primary add-to-cart')]"
    cart_button = "//div/a/span[contains(text(),'Cart')]"
    confirm_shopping_cart = "//h1[contains(text(),'Shopping Cart')]"
    delete_button = "//*[contains(@class,'remove-from-cart')]"
    no_items = "//div/span[contains(@class,'no-items')]"
    continue_button = "//div/a[contains(@class,'label')]"
    confirm_main_page = "//section/h1[contains(text(),'Popular Products')]"


