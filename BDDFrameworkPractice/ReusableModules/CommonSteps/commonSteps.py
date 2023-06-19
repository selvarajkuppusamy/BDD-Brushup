from behave import given, step
from ReusableModules.CommonMethods import commonMethods


@step("user navigates to '{page_name}' page")
@given("user navigates to site {page_name}")
def navigate_to_login_page(context, page_name):

    commonMethods.open_browser_with_url(context, page_name)

    print("This is just a quick print to confirm the GIVEN step is executed")
    print("")






















#
# #========================================================================================#
# @then('the page title should be "{expected_title}"')
# def verify_homepage_title(context, expected_title):
#     """
#     Verifies the home page title is as expected.
#     :param context:
#     :param expected_title:
#     :return:
#     """
#
#     webcommon.assert_page_title(context, expected_title)
#
# #========================================================================================#
# @then('current url should be "{expected_url}"')
# def verify_current_url(context, expected_url):
#     """
#     Verifies the current uls is as expected_url
#     :param context:
#     :param expected_url:
#     """
#
#     webcommon.assert_current_url(context, expected_url)