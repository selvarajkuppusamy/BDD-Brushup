
@smoke
Feature: My Account Smoke Test

@TC10
  Scenario: Valid user login


    Given user navigates to 'my account' page
    When user types 'aupython2023@gmail.com' into username field
    And user types 'RealPassword12!' into password field
    And user clicks on 'login' button
    Then user should be logged in

@TC11
  Scenario: Error message thrown for wrong password during Login


    Given user navigates to 'my account' page
    When user types 'aupython2023@gmail.com' into username field
    And user types '123456!' into password field
    And user clicks on 'login' button
    Then user sees an error message for this email address 'aupython2023@gmail.com'


  @TC12
  Scenario: Error message when an unregistered user tries to login


    Given user navigates to 'my account' page
    When user types 'asdfasdf@asdfasdf.com' into username field
    And user types '123456!' into password field
    And user clicks on 'login' button
    Then user sees an error message for this email id 'asdfasdf@asdfasdf.com'