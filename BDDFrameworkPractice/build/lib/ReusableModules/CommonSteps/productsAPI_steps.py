
from behave import step
from ReusableModules.CommonDAO_DataAccessObjects.productsDAO import  ProductsDAO

@step("I get number of available products from db")
def get_products_from_db(context):

    #get all available products with SQL
    all_rows = ProductsDAO().get_all_products_from_db()

    # Then set the number of available as context variable, so can be used for further steps in scenario
    context.no_of_products = len(all_rows)


