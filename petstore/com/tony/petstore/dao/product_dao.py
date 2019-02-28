from com.tony.petstore.dao.base_dao import BaseDao

class ProductDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        products=[]
        try:
            with self.conn.cursor() as cursor:
                sql='SELECT  [productid],[category] ,[cname],[ename],[image],[descn] ,[listprice],[unitcost] FROM [study].[dbo].[products]'
                cursor.execute(sql)
                result=cursor.fetchall()

                for row in result:
                    product={}
                    product['productid']=row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]
                    products.append(product)
        finally:
            self.close()

        return products

    def findbycat(self,catname):
        products=[]
        try:
            with self.conn.cursor() as  cursor:
                sql='SELECT  [productid],[category] ,[cname],[ename],[image],[descn] ,[listprice],[unitcost] FROM [study].[dbo].[products] where [category]=%s'
                cursor.execute(sql,catname)
                result=cursor.fetchall()

                for row in result:
                    product={}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]
                    products.append(product)
        finally:
            self.close()

        return products

    def findbyid(self,productid):

        try:
            with self.conn.cursor() as cursor:
                sql='SELECT  [productid],[category] ,[cname],[ename],[image],[descn] ,[listprice],[unitcost] FROM [study].[dbo].[products] where [productid]=%s'
                cursor.execute(sql,productid)
                result=cursor.fetchall()

                for row in result:
                    product = {}
                    product['productid'] = row[0]
                    product['category'] = row[1]
                    product['cname'] = row[2]
                    product['ename'] = row[3]
                    product['image'] = row[4]
                    product['listprice'] = row[5]
                    product['unitcost'] = row[6]
                    product['descn'] = row[7]


        finally:
            self.close()

        return product