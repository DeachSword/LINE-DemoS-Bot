# -*- coding: utf-8 -*-
from DeachSword.LINEBASE.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from DeachSword.LastStardust.server import Server
from DeachSword.LastStardust.session import Session

import rsa, os

class GenerateToken():

    def __init__(self, authToken=None, appName=None, channelId=''):
        if authToken is None:
            raise Exception('Please provide Auth Token')
        self.server = Server()
        #self.TEST_APP_NAME = 'ANDROID\t8.8.3\tAndroid OS\t8.0.0'
        #self.USER_AGENT = 'AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 Line/8.8.3'
        #self.USER_AGENT = 'Android Mobile Line/8.8.3'
        self.Headers = {
            'User-Agent': 'Line/8.8.3',
            'X-Line-Carrier': '51089, 1-0',
            'x-lal': 'zh_TW',
            'X-Line-Application': 'ANDROID\t8.8.3\tAndroid OS\t8.0.0',
            'X-Line-Access': authToken
        }
        self.APP_NAME = appName
        #self.authToken = authToken
        if channelId != '':
            print("即將登入頻道: %s"%(channelId))
            ch = self.__loadChannel(channelId)
        else:
            self.__loadSession()
    
    def __loadSession(self):
        try:
            self.talk = Session('https://ga2.line.naver.jp', self.Headers, '/S3').TalkV3()
            print("登入成功: %s"%(self.talk.getProfile().displayName))
            a = self.getQrCode(self.APP_NAME)
            print("即將登入網址: ", a)
            b = self.talk.verifyQrcode(a, '')
            self.LoginQrCode(a, self.APP_NAME)
        except Exception as e:
            print(e)
    
    def __loadChannel(self, channelId):
        try:
            self.talk = Session('https://ga2.line.naver.jp', self.Headers, '/S3').TalkV3()
            self.channel = Session('https://ga2.line.naver.jp', self.Headers, '/CH3').ChannelV3()
            print("即將登入 ")
            self.channelResult  = self.channel.approveChannelAndIssueChannelToken(channelId)
            return self.channelResult
        except Exception as e:
            print(e)

    def getQrCode(self, appName='CLOVAFRIENDS\t5.8.0\tDeachSword\t2.0.3'):
        testHeaders = {
            'User-Agent': 'Line/5.8.0',
            'X-Line-Carrier': '51089, 1-0',
            'x-lal': 'zh_TW',
            'X-Line-Application': appName
        }

        self.tauth = Session('https://ga2.line.naver.jp', testHeaders, '/api/v4/TalkService.do').TalkV4(isopen=False)
        qrCode = self.tauth.getAuthQrcode(True, 'DeachSword')
        return qrCode.verifier

    def LoginQrCode(self, verifier, appName='CLOVAFRIENDS\t5.8.0\tDeachSword\t2.0.3'):
        testHeaders = {
            'User-Agent': 'Line/5.8.0',
            'X-Line-Carrier': '51089, 1-0',
            'x-lal': 'zh_TW',
            'X-Line-Application': appName,
            'X-Line-Access': verifier
        }
        print('test')
        getAccessKey = self.server.getJson(self.server.parseUrl(self.server.LINE_CERTIFICATE_PATH), True, testHeaders)
        print(getAccessKey)
        auth = Session('https://ga2.line.naver.jp', testHeaders, '/api/v4p/rs').AuthV4(isopen=False)
        
        try:
            lReq = LoginRequest()
            lReq.type = LoginType.QRCODE
            lReq.keepLoggedIn = True
            lReq.identityProvider = 0
            lReq.accessLocation = '8.8.8.8'
            lReq.systemName = 'DeachSword'
            lReq.verifier = getAccessKey['result']['verifier']
            lReq.e2eeVersion = 0
            result = auth.loginZ(lReq)
            print('Auth Token: ' + result.authToken)
        except Exception as e:
            print('[*]' + str(e))
            
    def setHeadersWithDict(self, headersDict):
        self.Headers.update(headersDict)