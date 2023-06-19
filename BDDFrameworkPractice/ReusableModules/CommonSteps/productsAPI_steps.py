import pprint
from behave import step
from ReusableModules.CommonDAO_DataAccessObjects.productsDAO import ProductsDAO
from ReusableModules.CommonAPIs import products_API

@step("I get number of available products from db")
def get_products_from_db(context):

    #get all available products with SQL
    all_rows = ProductsDAO().get_all_products_from_db()

    print("Number of products in DB : {}".format(len(all_rows)))
    print ("")

    # Then set the number of available as context variable, so can be used for further steps in scenario
    context.no_of_products_db = len(all_rows)



@step("I get number of available products from api")
def get_products_from_api(context):

    #call API
    list_of_products = products_API.list_all_products()
    number_of_products = len(list_of_products)
    print ("")
    print("Number of products in API : {}".format(number_of_products))
    import pdb; pdb.set_trace()

    context.no_of_products_api = number_of_products
    #set context variable with no.of producs


@step("total number of products in api should be same as in db")
def compare_api_db_products(context):

    assert context.no_of_products_api == context.no_of_products_db, "Number of products in DB response and API response dont match." \
                                                                    "DB products : {}, API products : {}".format(context.no_of_products_db, context.no_of_products_api)


@step("I get {quantity} random product from database")
def random_products_from_database(context, quantity):

    context.random_products = ProductsDAO().get_random_products_from_db(quantity)



@step("I verify the product api returns correct product by id")
def verify_if_product_api_returns_correct_product_by_id(context):

    product_id = context.random_products[0]['ID']

    rs_get_product = products_API.get_product_by_id(product_id)

    assert rs_get_product['id'] == product_id, "Wrong product id when calling GET product by id."
    assert rs_get_product['name'] == context.random_products[0]['post_title'],"" \
        "Wrong product name when calling GET product by id, API : {}, DB : {}".format(rs_get_product['name'], context.random_products[0]['post_title'])