from ReusableModules.CommonHelpers.apiRequestsHelper import WooRequestsHelper

def list_all_products():

    params = {'per_page' : 100}
    rs_api = WooRequestsHelper().get(wc_endpoint= 'products', params = params)

    return rs_api




def get_product_by_id(id):
    rs_api = WooRequestsHelper().get(wc_endpoint='products/{}'.format(id))

    return rs_api

