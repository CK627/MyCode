import itchat
import requests
from retry import retry


@retry(tries=3)
def robot_chat(text):
    url = "http://www.tuling123.com/robot-chat/robot/chat/759052/CUZW?geetest_challenge=&geetest_validate=&geetest_seccode="
    return requests.post(url, json={
        "perception": {"inputText": {"text": text}},
        "userInfo": {"userId": "demo"}
    }).json()['data']['results'][0]['values']['text']
@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def auto_reply(msg):
    reply = "execuse me?"
    try:
        reply = robot_chat(msg.text)
    except:
        pass
    finally:
        print(f'[In] {msg.text} \t [Out] {reply}')
        return reply


itchat.auto_login(hotReload=True)
itchat.run()