from behave import when, step
from ReusableModules.CommonMethods import commonMethods
from ReusableModules.CommonSteps import commonSteps
from ReusableModules.Configs.locatorConfigs import MY_ACCOUNT_LOCATORS


@step("user types '{email}' into username field")
def input_username(context, email):

    locator_type = MY_ACCOUNT_LOCATORS['login_username']['type']
    locator_string = MY_ACCOUNT_LOCATORS['login_username']['locator']

    commonMethods.type_into_text_field(context, email, locator_type, locator_string)


@step("user types '{password}' into password field")
def input_password(context, password):

    locator_type = MY_ACCOUNT_LOCATORS['login_password']['type']
    locator_string = MY_ACCOUNT_LOCATORS['login_password']['locator']

    commonMethods.type_into_text_field(context, password, locator_type, locator_string)


@step("user clicks on '{button_name}' button")
def click_button(context, button_name):

    if button_name.lower() in ('login', 'log in'):
        locator_type = MY_ACCOUNT_LOCATORS['login_button']['type']
        locator_string = MY_ACCOUNT_LOCATORS['login_button']['locator']

    else:
        raise Exception ("To be Implemented, as only login is implemented for now")

    commonMethods.click_element(context, locator_type, locator_string)


@step("user should be logged in")
def verify_user_login(context):

    navbar_type = MY_ACCOUNT_LOCATORS['left_nav']['type']
    navbar_string = MY_ACCOUNT_LOCATORS['left_nav']['locator']

    logout_type = MY_ACCOUNT_LOCATORS['left_nav_logout']['type']
    logout_string = MY_ACCOUNT_LOCATORS['left_nav_logout']['locator']

    commonMethods.assert_element_visible(context, navbar_type, navbar_string)
    commonMethods.assert_element_visible(context, logout_type, logout_string)


@step("user sees an error message for this email address '{email}'")
def error_message_displayed(context, email):

    expected_msg = ("Error: The password you entered for the email address {} is incorrect. Lost your password?").format(email)

    login_errorbox_type = MY_ACCOUNT_LOCATORS['login_error_box']['type']
    login_errorbox_string = MY_ACCOUNT_LOCATORS['login_error_box']['locator']

    is_element_exist = commonMethods.get_text_from_element(context, expected_msg, login_errorbox_type, login_errorbox_string)

    if is_element_exist:
        print("Pass")
        print("")
    else:
        raise Exception ("Error message is not expected for the entered email")


@step("user sees an error message for this email id '{email}'")
def error_message_displayed_invalid_email(context, email):

    expected_msg = "Unknown email address. Check again or try your username."

    login_errorbox_type = MY_ACCOUNT_LOCATORS['login_error_box']['type']
    login_errorbox_string = MY_ACCOUNT_LOCATORS['login_error_box']['locator']

    is_element_exist = commonMethods.get_text_from_element(context, expected_msg, login_errorbox_type, login_errorbox_string)

    if is_element_exist:
        print("Pass")
        print("")
    else:
        raise Exception("Error message is wrong for this user {}".format(email))










