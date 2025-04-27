#声明一个装饰器函数
#导入core里src模块，要判断login_user这个变量
#接受一个函数，在内层函数调用+添加功能
#如果login_user有值，那就是已登入不做任何操作，只是备份函数信息
#如果没有值就显示未登入，并且跳转到src里login函数，执行登入操作
from core import src
def is_login(f):
     def check(*args,**kwargs):
         if src.login_user:
             res= f(*args,**kwargs)#保留备份原函数
             return  res
         else:
             print("你还未登入，请登入后使用该功能")
             src.login()
     return check
