from woocommerce import API
from ReusableModules.CommonHelpers.credentialsHelper import CredentailsHelper

class WooRequestsHelper(object):

    def __init__(self):

        creds_helper = CredentailsHelper()
        wc_creds = creds_helper.get_wc_api_keys()

        wcapi = API(
            url="http://myfirstwebsite.local",
            consumer_key = wc_creds['wc_key'],
            consumer_secret= wc_creds['wc_secret'],
            version="wc/v3"
        )
        self.wcapi = wcapi


    def assert_status_code(self):
        assert self.rs.status_code == self.expected_status_code, "Bad status code. Endpoint : {}, Params : {}"\
                            "Actual status code : {}, Expected status code : {}, Response Body : {}"\
                                                        "".format(self.wc_endpoint, self.params, self.rs.status_code,
                                                                    self.expected_status_code, self.rs.json())


    def get(self, wc_endpoint, params=None, expected_status_code=200):

        self.rs = self.wcapi.get(wc_endpoint, params=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()


    def post(self, wc_endpoint, params=None, expected_status_code=200):

        self.rs = self.wcapi.post(wc_endpoint, data=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()

        return self.rs.json()

    def delete(self):
        pass


    def put(self):
        pass


if __name__ == '__main__':

    myObj = WooRequestsHelper()
    #myObj.get("products")

    payload = {
        "email": "dummasdfyemail@gmail.com",
        "password": "Password12!"
        }

    response = myObj.post("customers", params = payload, expected_status_code=201)
    import pprint; pprint.pprint(response)


