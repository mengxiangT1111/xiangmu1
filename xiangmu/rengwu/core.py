import os
import json
class ChatServer:

    # 注册
    def register(self):
        name=input("请输入用户名")
         # 写入文件
        id=input("请输入ID")
        password=input("请输入密码")
        user_info = {
            "name": name,
            "password": password,
            "ID": id
        }
        file_path = r"D:\xiangmu1\ChatClient\name_data"
        with open(fr"{file_path}\{name}.json", "w", encoding="utf-8") as f:
            json.dump(user_info, f)
            # 登录
    def login(self):
        name = input("请输入用户名")
        # 写入文件
        id = input("请输入ID")
        password = input("请输入密码")

def run():
    while 1:
        print("欢迎来到聊天室")
