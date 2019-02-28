from com.tony.petstore.dao.base_dao import  BaseDao

class AccountDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findbyid(self,userid):
        account= None
        try:
            with self.conn.curser() as curser:
                sql= 'SELECT [userid] ,[password],[email] ,[name],[addr],[city] ,[country],[phone] FROM [study].[dbo].[accounts] where [userid]=%s'
                curser.execute(sql,userid)
                result=curser.fetchone()

                for row in result:
                    account={}
                    account['userid']=row[0]
                    account['password']=row[1]
                    account['email']=row[2]
                    account['name'] = row[3]
                    account['addr'] = row[4]
                    account['city'] = row[5]
                    account['country'] = row[6]
                    account['phone'] = row[7]
        finally:
            self.close()

        return account

