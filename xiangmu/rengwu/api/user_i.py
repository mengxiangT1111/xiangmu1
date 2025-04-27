#声明一个函数，用于处理注册逻辑
#该函数会接受到两个参数，为用户名和密码
#用一个合适的容器/数据类型保持用户数据 字典
#导入db_handle模块
#保持好用户数据之后，返回两个值，1，注册结果，为布尔类型，2说明信息，为字符串类型
from DB import db_handle

def register_info(user_name,password):
    user_info = {
        "user_name":user_name,
        "password":password,
        "zaixian":0,
        "account":[]
    }
    user_data = db_handle.get_data(user_name)
    if user_data:
        return False,"注册失败，该用户已注册"
    db_handle.sava_data(user_info)
    return True,f"{user_name}注册成功"
def login_info(user_name,password):
    user_data=db_handle.get_data(user_name)
    if user_data:
        if password == user_data['password']:
            db_handle.xiugai_data(user_name)
            return True,f"{user_name}登录成功"
        return False,"登录失败，用户名不存在，请重新输入"
    return False,"登录失败，用户名不存在，请重新输入"
def zaixian(user_name,ti):
    user_data=db_handle.get_data(user_name)
    if user_data['zaixian']:
        return True
    return False