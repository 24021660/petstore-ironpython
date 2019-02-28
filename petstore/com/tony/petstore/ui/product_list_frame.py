import wx
import wx.grid

from com.tony.petstore.dao.product_dao import ProductDao
from com.tony.petstore.ui.my_frame import MyFrame

CATEGORYS=['鱼类','狗类','爬行类','猫类','鸟类']

class ProductListFrame(MyFrame):
