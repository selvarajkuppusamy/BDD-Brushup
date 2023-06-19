import random

from ReusableModules.CommonHelpers.dbHelper import DBHelper


class ProductsDAO(object):

    def __init__(self):

        self.db_helper = DBHelper()

    def get_all_products_from_db(self):

        sql = "SELECT * FROM local.wp_posts where post_type = 'product';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql

    def get_random_products_from_db(self,quantity):
        # import pdb;
        # pdb.set_trace()
        sql = "SELECT * FROM local.wp_posts WHERE post_type = 'product' ORDER BY id DESC LIMIT 5000;"
        rs_sql = self.db_helper.execute_select(sql)

        return random.sample(rs_sql, int(quantity))

