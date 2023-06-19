import os


class CredentailsHelper(object):

    def __init__(self):
        pass

    def get_wc_api_keys(self):

        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')

        if not wc_key or not wc_secret:
            raise Exception ("API keys and secret are missing and must be set as env variables.")
        else:
            return {'wc_key':wc_key, 'wc_secret': wc_secret}

    def get_db_credentials(self):

        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')

        if not db_user or not db_password:
            raise Exception("DB user name and password are missing and must be set as env variables.")
        else:
            return {'db_user': db_user, 'db_password': db_password}



if __name__ == '__main__':

    obj = CredentailsHelper()
    print(obj.get_wc_api_keys())
    print(obj.get_db_credentials())