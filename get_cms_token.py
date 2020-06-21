from linepy import *
import requests
import json
import random
import string

def randstr(n):
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])
    return random_str

host = 'https://gwk.line.naver.jp'
LA = "BIZIOS\t1.7.5\tiOS\t10.2"
udidHash = randstr(10)
print('udidHash: %s'%udidHash)
header = {
    'Accept':"application/json",
    "Accept-Language":"zh-TW",
    "X-LHM":'POST',
    "X-LPV":'1',
    'X-Line-Application':LA,
    'User-Agent':LA
}
line = LINE('AUTH TOKEN', appName='IOS\t8.9.0\tiPhone_OS\t11.3')
channel_token = line.approveChannelAndIssueChannelToken('1417913499').channelAccessToken
print('channel_token: %s'%channel_token)
payload = {"channelAccessToken":channel_token, "udidHash":'a'} # yea just do it
endpoint = '/plc/api/core/auth/cmsToken'
res = requests.post(host+endpoint, data=json.dumps(payload), headers=header)
print('accessToken: %s'%res.json()["accessToken"]) # CMSToken