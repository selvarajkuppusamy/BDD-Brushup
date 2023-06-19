
  Feature:

    @TC24
    Scenario: Verify get products returns the expected products

      Given I get number of available products from db
      When I get number of available products from api
      Then total number of products in api should be same as in db

    @TC25
    Scenario: Verify product details is returned for a specific product id

      Given I get 1 random product from database
      Then I verify the product api returns correct product by id