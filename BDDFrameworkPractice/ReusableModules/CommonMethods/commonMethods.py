from selenium import webdriver
from ReusableModules.Configs import locatorConfigs, urlConfigs


def open_browser_with_url(context, page_name):

    # Construct URL to open in the browser
    if page_name.startswith('http'):
        url = page_name
    else:
        _url = urlConfigs.URLCONFIG.get(page_name)
        base_url = urlConfigs.URLCONFIG.get('base_url')
        url = base_url + _url

    # Gets the user data in CLI / config for browser, pass with "-D browser_name"
    browser = context.config.userdata.get('browser')
    if not browser:
        browser = "ff"

    if browser.lower() == 'chrome':
        context.driver = webdriver.Chrome()
    if browser.lower() in ('ff', 'firefox'):
        context.driver = webdriver.Firefox()
    else:
        raise Exception("The browser {} is not recognised".format(browser))

    # Clean URL from any spaces at end

    url = url.strip()
    context.driver.get(url)


def type_into_text_field(context_or_element, input_value, locator_attribute, locator_text):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        inputField = context_or_element
    else:
        inputField = context_or_element.driver.find_element(locator_attribute, locator_text)

    inputField.send_keys(input_value)


def click_element(context_or_element, locator_attribute, locator_text):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element_to_click = context_or_element
    else:
        element_to_click = context_or_element.driver.find_element(locator_attribute, locator_text)

    element_to_click.click()


def assert_element_visible(context_or_element, locator_attribute, locator_text):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element

    else:
        element = context_or_element.driver.find_element(locator_attribute, locator_text)

    if not element.is_displayed():
        raise AssertionError("The element is not displayed")
    # else:
    #     print("Quick print to ensure it worked")
    #     print("")


def get_text_from_element(context_or_element, expected_text, locator_attribute, locator_text, case_sensitive=False):

    if isinstance(context_or_element, webdriver.remote.webelement.WebElement):
        element = context_or_element
    else:
        element = context_or_element.driver.find_element(locator_attribute, locator_text)

    element_text = element.text

    if not case_sensitive:
        if expected_text.lower() in element_text.lower():
            return True
        else:
            return False
    else:
        return True if expected_text in element_text else False




# def go_to(url, browser_type=None):
#     """
#     Function to start instance of the specified browser and navigate to the specified url.
#
#     :param url: the url to navigate to
#     :param browser_type: the type of browser to start (Default is Firefox)
#
#     :return: driver: browser instance
#     """
#
#     if not browser_type:
#         # create instance of Firefox driver the browser type is not specified
#         driver = webdriver.Firefox()
#     elif browser_type.lower() == 'chrome':
#         # create instance of the Chrome driver
#         driver = webdriver.Chrome()
#     else:
#         raise Exception("The browser type '{}' is not supported".format(browser_type))
#
#     # clean the url and go to the url
#     url = url.strip()
#     driver.get(url)
#
# #     return driver
#
#
# def assert_page_title(context, expected_title):
#     """
#     Function to assert title of current page.
#     :param expected_title:
#     :param context:
#     """
#
#     actual_title = context.driver.title
#
#     print("The actual title is: {}".format(actual_title))
#     print("The expected title is: {}".format(expected_title))
#
#     assert expected_title == actual_title, "The title is not as expected." \
#                                            " Expected: {}, Actual: {}".format(expected_title, actual_title)
#     print("The page title is as expected.")
#
#
# def assert_current_url(context, expected_url):
#     """
#     Function to get the current url and assert it is same as the expected url.
#     :param context:
#     :param expected_url:
#     """
#
#     # get the current url
#     current_url = context.driver.current_url
#
#     if not expected_url.startswith('http') or not expected_url.startswith('https'):
#         expected_url = 'https://' + expected_url + '/'
#
#     assert current_url == expected_url, "The current url is not as expected." \
#                                         " Actual: {}, Expected: {}".format(current_url, expected_url)
#
#     print("The page url is as expected.")
#
# #======================================================================================#
# def find_element(context, locator_attribute, locator_text):
#     """
#     Finds an element and returns the element object.
#     :param context:
#     :param locator_attribute: what to use to locate (example, id, class, xpath,....)
#     :param locator_text: the locator text (ex. the id, the class, the name,...)
#     """
#
#     possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]
#
#     if locator_attribute not in possible_locators:
#         raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
#                             The approved attributes are : %s ' % possible_locators)
#     try:
#         element = context.driver.find_element(locator_attribute, locator_text)
#         return element
#     except Exception as e:
#         raise Exception(e)
# #======================================================================================#
# def is_element_visible(element):
#     '''
#     Checks if element is visible and returns True or False
#     '''
#
#     if element.is_displayed():
#         return True
#     else:
#         return False
# #======================================================================================#
# def assert_element_visible(element):
#     '''
#     Function to check if the passed in element is visible.
#     Raises and exception if it is not exception.
#     '''
#
#     if not element.is_displayed():
#         raise AssertionError('The element is not displayed')





