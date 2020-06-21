from DeachSword.linepy import *
from DeachSword.LINEBASE import ttypes
import requests, json, time, os, string, random

def randstr(n):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    return random_str

CMSToken = 'input you cms token'
udidHash = 'a' #any :v

def createOA():
    host = 'https://gwk.line.naver.jp'
    LA = "BIZIOS\t1.7.5\tiOS\t10.2"
    header = {
        'Accept': "application/json",
        "Accept-Language": "zh-TW",
        "X-LHM": 'GET',
        "X-LPV": '1',
        'X-Line-Application': LA,
        'User-Agent': LA
    }
    path = os.path.dirname(os.path.abspath(__file__))

    count = 1 # Number what you want to create
    base_name = 'YinMo@'
    random_str = randstr(14) # 規制を避ける
    name = base_name + random_str
    header.update({'X-CMSToken': CMSToken})

    # phase1
    header.update({'X-LHM': 'GET'})
    endpoint = '/plc/api/core/account/prepare'
    res = requests.post(host + endpoint, headers=header)
    registerToken = res.json()['registerToken']

    # phase2
    endpoint = '/plc/api/core/account/register'
    header.update({'X-LHM': 'POST'})
    payload = {"registerToken": registerToken, "majorCategory": 117, "minorCategory": 1153, "ageVerified": False,
               "displayName": name, "allowBcoaFriendship": 'false',
               "deviceInfo": {"udidHash": udidHash,
                              "model": "iPad5,1"}, "country": "TW"}
    res = requests.post(host + endpoint, data=json.dumps(payload), headers=header)
    print(res.json())
    accessToken = res.json()['accessToken']
    mid = res.json()['mid']
    print('token: %s\nmid: %s'%(accessToken, mid))
    line = LINE(idOrAuthToken=accessToken, appName=LA)
    path = './base.jpeg' #bot pic
    line.updateProfilePicture(path=path)

    # phase3
    endpoint = '/plc/api/core/auth/atCC/1418234097'
    payload = {"botMid": mid}
    res = requests.post(host + endpoint, data=json.dumps(payload), headers=header)
    atcc = res.json()['at_cc']

    # phase4
    header = {
        'Accept': "application/json",
        "Accept-Language": "zh-TW",
        "X-LHM": 'POST',
        "X-LPV": '1',
        'X-Line-Application': LA,
        'X-CMSToken': CMSToken,
        'X-ATCC': atcc,
        'User-Agent': LA
    }
    endpoint = '/plc/api/core/account/resign'

    random_str = randstr(40)
    payload = {"resignToken": random_str.upper()}

    res = requests.post(host + endpoint, data=json.dumps(payload), headers=header)
    accessPermissions(channelId, AuthToken)
    return accessToken
createOA()
def accessPermissions(channelId, AuthToken):
    url = 'https://access.line.me/dialog/api/permissions'
    payload = {
        "on": [
            "P",
            "CM"
        ],
        "off": []
    }
    data = json.dumps(payload)
    hr = {
        'X-LINE-ChannelId': channelId,
        'X-LINE-Access': AuthToken,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.1; SAMSUNG Realise/DeachSword; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36',
        'Content-Type': 'application/json',
        'X-Line-Application': '',
        'X-Requested-With': 'XMLHttpRequest',
        'Accept-Language': 'zh-TW,en-US;q=0.8'
    }

    r = requests.post(url, data=data, headers=hr)
    print('accessPermissions: %s'%(r.status_code))
#print(createOA())
#accessPermissions('1604231486', 'I+IjUBvrRWVxsmo8PoOrNcTcXIUU72XBlhfOqpLSG7l5ntay+MqqeLNe97Sts9Ot/Hnz98hW6k+K5MMbEuwhLZ5TCodN9Jo0RFUpyfxBHTuS0D3yu4HEW5zOaq0yBZ7g3dRB+jvaTkS/amII4f9vrjb3s3jjjbbfHa3aUv8sZaR1ARgOxmdNc3bcWdxDXU9ipul23aD5JJpKsi4bpyu5x8mI0ijnPpu0BwDONj7/yEClEhw/vCk5X9Vo5HGdJk0uBQzrA3z9IUGMHTgMUFmAPjWp5KUDqoon1YsqWLssqM+sUUblI8POqnJPEaeA==')