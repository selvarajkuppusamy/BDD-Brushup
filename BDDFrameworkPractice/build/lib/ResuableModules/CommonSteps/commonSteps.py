from behave import given, when, then, step


@step("user navigates to 'my account' page")
@given("user navigates to login page")
def navigate_to_login_page(context):
    # pdb.set_trace()
    print ("This is just a quick print statement")
    print("")