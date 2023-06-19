@smoke @user_api_smoke
Feature: Users API

  @TC29
  Scenario: Verify if POST /customers create user

    Given I generate random email and password
    When I call 'create customer' API
    Then customer should be created
