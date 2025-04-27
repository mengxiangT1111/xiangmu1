#注册
#无限循环，让程序一直执行
#让用户输入用户名，密码，确认密码
#如果密码一致，在进行后续操作
#如果密码一致就转交给user_i.py进行逻辑判断，不一致就输出注册失败
from api import user_i
from lib.common import is_login

def register():
    while 1:
        #1让用户输入用户名，密码，确认密码
        user_name = input("请输入你的姓名>>>")
        password = input("请输入你的密码>>>")
        re_password =input("请确认你的密码>>>")
        #判断密码是否一致
        if password == re_password:
            flag,msg = user_i.register_info(user_name,password)
            if flag:#注册成功
                print(msg)#输出说明信息
                break
            else:
                print(msg)
        else:
            print("密码不一致，请重新注册")

#登录
#声明一个login_user,作用是判断是否登录的标志
#调用登录逻辑处理函数，并接受他的返回值：flag：登录结果，msg：说明信息
#如果登录成功，就修改全局变量login_user的值为用户名，输出说明信息并breal返回主页
#否则继续进行登录操作
login_user = None#初始值，默认是没有登录的状态，在登录之后用户名进行覆盖
def login():
    while 1:
        user_name = input("请输入你的姓名>>>")
        password = input("请输入你的密码>>>")
        flag,msg = user_i.login_info(user_name,password)
        if flag:
            print(msg)
            global login_user
            login_user = user_name
            break
        else:
            print(msg)

@is_login
def timi():
    while 1:
        user_name = input("请输入发送对象>>>")
        neirong = input("请输入发送内容>>>")
        flag = user_i.zaixian(user_name,neirong)
        if flag:
            print("向",user_name,"发送",neirong)
        else:
            print(user_name,"不在线")
        tout = input("退出请输入0,继续输入1>>>")
        if tout==0:
            break
#功能选择的字典
#1.值为列表，列表里下标为0的数据为描述功能的字符串，下标为1的数据才是函数本身
#2.这里的函数不要加括号，这里只是定义2，没有调用，如果加了括号就是直接调用了
fun_select={
    0:["退出",exit],
    1:["注册",register],
    2:["登录服务器",login],
    3:["聊天",timi]

}
def run():
    while 1:
        print("欢迎来到聊天室")
        for k in fun_select:#遍历字典，把字典里的第一个数据取出来（序号+序号功能）
            print(k,fun_select[k][0])
        select = int(input("请选择你要进行的操作》》》"))
        if select in fun_select:#如果输入的值在序号内，就调用对应功能函数
            fun_select[select][1]()
        else:
            print("输入错误")