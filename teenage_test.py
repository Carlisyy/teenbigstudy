import requests
import time
import re


def get_accessToken(openid):
    url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/login/we-chat/callback'
    params = {
        'callback': 'https%3A%2F%2Fjxtw.h5yunban.cn%2Fjxtw-qndxx%2FsignUp.php',
        'scope': 'snsapi_userinfo',

        #必须要的参数
        'appid': 'wxe9a08de52d2723ba',   # 唯一
        'openid': openid,   # 需要获取的

        # 可以不用
        'sign': 'CD8CE7188161BCC08A1D80F9E341B5CB',
        'nickname': '%25E5%25BF%2583%25E5%2590%2591%25E5%25A4%25A7%25E6%25B5%25B7',

        'headimg': 'https%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FSY6aCyeNicIyiba94WZkSib9x625a0GQwOIqkgQVOYVeVCdRDaXhpxXFE4VIwhDfdXQMRFeibGAxGR6cKuWU1L0dwA%2F132',
        'time': str(int(time.time())),
        'source': 'common',
        't': str(int(time.time()))
    }
    headers = {
        'Host': 'jxtw.h5yunban.cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045435 Mobile Safari/537.36 MMWEBID/2026 MicroMessenger/7.0.21.1800(0x270015D5) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'Referer': 'https://wx.yunbanos.cn/wx/oauthInfoCallback?r_uri=https%3A%2F%2Fjxtw.h5yunban.cn%2Fjxtw-qndxx%2Fcgi-bin%2Flogin%2Fwe-chat%2Fcallback%3Fcallback%3Dhttps%253A%252F%252Fjxtw.h5yunban.cn%252Fjxtw-qndxx%252FsignUp.php%26scope%3Dsnsapi_userinfo&source=common&code=03136iml2hTUd640JMnl2v5TGd036imj&state=STATE&appid=wxe9a08de52d2723ba'
    }
    response = requests.get(url=url, params=params, headers=headers)
    print(response.status_code)
    print(response.text)
    accessToken = re.findall("\('accessToken', '(.*?)'\)", response.text, re.S)[0]

    return accessToken


def detail(accessToken):
    url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/user-api/course/last-info'
    params = {
        'accessToken': accessToken
    }
    headers = {
        'Host': 'jxtw.h5yunban.cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045435 Mobile Safari/537.36 MMWEBID/2026 MicroMessenger/7.0.21.1800(0x270015D5) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'Referer': 'https://jxtw.h5yunban.cn/jxtw-qndxx/signUp.php'
    }
    response = requests.get(url=url, params=params, headers=headers)
    print(response.json())
    result = response.json()['result']
    cardNo = result['cardNo']
    nid = result['nid']

    return cardNo, nid


def request(accessToken, cardNo, nid, course):
    url = 'https://jxtw.h5yunban.cn/jxtw-qndxx/cgi-bin/user-api/course/join'
    params = {
        'accessToken': accessToken
    }
    headers = {
        'Host': 'jxtw.h5yunban.cn',
        'Origin': 'https://jxtw.h5yunban.cn',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; V2002A Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.120 MQQBrowser/6.2 TBS/045435 Mobile Safari/537.36 MMWEBID/2026 MicroMessenger/7.0.21.1800(0x270015D5) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
        'Referer': 'https://jxtw.h5yunban.cn/jxtw-qndxx/signUp.php'
    }
    json = {
        'cardNo': cardNo,
        'course': course,
        'nid': nid,
        'subOrg': None
    }
    response = requests.post(url=url, params=params, headers=headers, json=json)

    return response.json()


openid = 'oc2p4jmWQeb48JLML9qqQmvRU3vc'
course = 'C0015'


# 获取accessToken
accessToken = get_accessToken(openid)
# time.sleep(3)
# 获取用户信息
cardNo, nid = detail(accessToken)
# time.sleep(3)
# 发起完成请求
result = request(accessToken, cardNo, nid, course)

print(result)



