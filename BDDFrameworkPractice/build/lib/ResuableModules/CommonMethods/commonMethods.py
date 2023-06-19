from selenium import webdriver


def open_browser_with_url(url, browser_type=None):

    if not browser_type:
        driver = webdriver.Firefox()
    elif browser_type.lower() == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise Exception("The browser type {} is not recognised".format(browser_type))

    url = url.strip()
    driver.get(url)

    return driver





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
#     return driver
