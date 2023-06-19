
LOCATORS = {
    'main navigation' : {'type': 'id', 'locator':'mainnav'},
    'top navigation' : {'type': 'id', 'locator':'top'},
    'options' : {'type': 'css selector', 'locator':'.options-bar'}
}


MY_ACCOUNT_LOCATORS = {

    'login_username' : {'type': 'id', 'locator':'username'},
    'login_password' : {'type': 'id', 'locator':'password'},
    'login_button' : {'type': 'css selector', 'locator':'[name="login"]'},
    'left_nav' : {'type': 'css selector', 'locator':'nav.woocommerce-MyAccount-navigation'},
    'left_nav_logout' : {'type': 'css selector', 'locator':'nav.woocommerce-MyAccount-navigation ul li:nth-of-type(6)'},
    'login_error_box' : {'type': 'css selector', 'locator':'ul.woocommerce-error'}

}