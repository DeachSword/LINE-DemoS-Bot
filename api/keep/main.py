# -*- coding: utf-8 -*-

import json, time, base64

class LineKeep():


    def syncKeep(self, revision=0, limit=30):
        params = {
            'revision': revision,
            'limit': limit
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/sync.json', params)
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()

    def fetchKeep(self, revision=0, limit=30):
        params = {
            'revision': revision,
            'limit': limit
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/fetch.json', params)
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()

    def createKeep(self, revision=0, limit=30):
        params = {
            'revision': revision,
            'limit': limit
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/create.json', params)
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()

    def updateKeep(self, revision=0, limit=30):
        params = {
            'revision': revision,
            'limit': limit
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/update.json', params)
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()

    def deleteKeep(self, revision=0, limit=30):
        params = {
            'revision': revision,
            'limit': limit
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/delete.json', params)
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def getKeep(self):
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/get.json')
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def deleteKeepMessage(self):
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/message/delete.json')
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def pinKeepContents(self):
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/contents/pin')
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def unpinKeepContents(self):
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/contents/unpin.json')
        #application/x-thrift: application/json -> /enc
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def getKeepUsedSize(self):
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/size.json')
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def initKeep(self):
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/init.json')
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def deleteKeepObs(self):
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'X-LAP': 5, #needless
            'x-lsr':'TW', #needless
            'x-lal': 'zh-Hant_TW' #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/kp', '/api/v26/keep/obs/delete.json')
        r = self.server.postContent(url, data="", headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
        
    def forwardKeepObject(self, oid, contentType, reqseq, contentId):
        data = {} #private :p
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/oa/r/talk/m/reqseq/copy.nhn', data=data)
 