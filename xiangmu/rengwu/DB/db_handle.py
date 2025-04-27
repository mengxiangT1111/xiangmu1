#导入json模块/文件路径信息
#声明一个函数用来实现保存数据操作
#该函数会接受到一个参数为用户数据
#以json文件的形式保持文件，文件名为用户名。json把用户数据里的名字取出来作为变量名
import json
import  os
from config.setting import file_path

def sava_data(user_info):
    name = user_info["user_name"]#把用户名取出来
    with open(fr"{file_path}\{name}.json","w",encoding="utf-8")as f:
        json.dump(user_info,f)#写入文件

#导入os模块
#声明一个函数用来实现获取用户数据功能
#该函数会接受一个参数
#用os函数判断用户文件是否存在。如果存在就读取并返回用户数据，有返回值，如不存在该函数默认返回None
def get_data(user_name):
    user=fr"{file_path}\{user_name}.json"
    if os.path.exists(user):
        with open(user,"r",encoding="utf-8") as f:
            user_data=json.load(f)
            return  user_data
def xiugai_data(user_name):
    user = fr"{file_path}\{user_name}.json"
    if os.path.exists(user):
        with open(user,"r",encoding="utf-8") as f:
            user_data = json.load(f)
        user_data["zaixian"] = 1
        with open(user,"w",encoding="utf-8") as f:
            json.dump(user_data, f)