import pymssql
from com.tony.petstore.dao.base_dao import  BaseDao

class OrderDetailDao(BaseDao):
    def __init__(self):
        super().__init__()

    def create(self,orderdetail):
        try:
            with self.conn.cursor() as cursor:
                sql='insert into orderdetails (orderid,productid,quatity,unitcost) values (%s,%s,%s,%s)'
                affectcount=cursor.execute(sql,orderdetail)
                print("受影响行数{0}".format(affectcount))
                self.conn.commit()
        except pymssql.DatabaseError as  e:
            print(e)
            self.conn.rollback()
        finally:
            self.close()

