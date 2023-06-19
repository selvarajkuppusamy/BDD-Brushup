import pymysql
from ReusableModules.CommonHelpers.credentialsHelper import CredentailsHelper

class DBHelper(object):

    def __init__(self):

        creds_helper = CredentailsHelper()
        creds = creds_helper.get_db_credentials()

        self.host = "localhost"
        self.db_user = creds['db_user']
        self.db_password = creds['db_password']
        self.socket = "/Users/surya/Library/Application Support/Local/run/Sd-alvgFH/mysql/mysqld.sock"

    def create_connection(self):

        self.connection = pymysql.connect(host = self.host, user = self.db_user, password = self.db_password, unix_socket = self.socket)

    def execute_select(self, sql):

        try:
            self.create_connection()
            cur = self.connection.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
            return rs_dict
        except Exception as e:
            raise Exception ("Failed running sql{}. Error {} ".format(sql, str(e)))

    def execute_sql(self):
        pass


if __name__ == '__main__':

    dbHelper = DBHelper()
    dbHelper.execute_select("SELECT * FROM local.wp_posts where post_type = 'product';")
