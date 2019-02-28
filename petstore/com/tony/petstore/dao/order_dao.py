import pymssql
from com.tony.petstore.dao.base_dao import BaseDao

class OrderDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        orders=[]
        try:
            with self.conn.cursor() as cursor:
                sql='SELECT [orderid] ,[userid],[orderdate] FROM [study].[dbo].[orders]'
                cursor.execute(sql)
                result=cursor.fetchall()

                for row in result:
                    order={}
                    order['orderid']=row[0]
                    order['userid']=row[1]
                    order['orderdate']=row[2]
                    orders.append(order)
        finally:
            self.close()

        return orders

    def create(self,order):
        try:
            with self.conn.cursor() as cursor:
                sql='insert into orders (orderid,userid,orderdate,status,amount) values (%s,%s,%s,%s,%s)'
                affectedcount=cursor.execute(sql,order)
                print('成功输入第{0}条数据'.format(affectedcount))
                self.conn.commit()
        except pymssql.DatabaseError as e:
            self.conn.rollback()
            print(e)
        finally:
            self.close()

