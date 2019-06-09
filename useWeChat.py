import itchat,time
import requests
import re
# 实现登录和登录状态保存
itchat.auto_login(hotReload=True)
itchat.dump_login_status()
# 保存土味情话前后句
qa = []
#设置发送土味情话的对象 匹配昵称 备注任一即可
send_userid='王武杰'
user_name = itchat.search_friends(name=send_userid)[0]['UserName']
# 第一句开场白
greet = "土味五姐正式上线"
# 发送开场白
itchat.send(greet,user_name)
# 设置再次发送土味的标志
again = False
# 定义发送一句土味情话的方法
def send_sentence(user_name):
    global qa
    response= requests.get("https://api.lovelive.tools/api/SweetNothings")
    texts = response.text
    # 分割语句形成两句话
    qa = re.split("？|，",texts,1)
    if len(qa) > 1:
        itchat.send(qa[0],user_name)
    else:
        itchat.send(texts,user_name)
#调用方法 发送土味情话
send_sentence(user_name)
# 监听对方回复 
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    global qa
    global user_name
    global again
    if again:  
        send_sentence(user_name)
        again = False   
    elif len(qa) > 1:
        itchat.send(qa[1],user_name)
        again = True
#运行自动回复          
itchat.run() 


   

