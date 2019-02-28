import pymssql
import configparser


class BaseDao(object):
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read('config.ini',encoding='utf-8')

        host=self.config['db']['host']
        user=self.config['db']['user']
        password=self.config['db']['password']
        database=self.config['db']['database']

        self.conn=pymssql.connect(host=host,
                                  user=user,
                                  password=password,
                                  database=database)
    def close(self):
        self.conn.close()