from ReusableModules.CommonHelpers.dbHelper import DBHelper


class ProductsDAO(object):

    def __init__(self):

        self.db_helper = DBHelper()


    def get_all_products_from_db(self):

        sql = "SELECT * FROM local.wp_posts where post_type = 'product';"
        rs_sql = self.db_helper.execute_select(sql)
        return rs_sql
