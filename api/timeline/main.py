# -*- coding: utf-8 -*-

import json, time, base64

class Timeline():


    """ ALBUM """

    def changeGroupAlbumName(self, mid, albumId, name):
        data = json.dumps({'title': name})
        params = {'homeId': mid}
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "PUT",
            'Content-type': "application/json",
            'x-lpv': '1', #needless
            'x-lsr':'TW', #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/ext/album', '/api/v3/album/%s' % albumId, params)
        r = self.server.postContent(url, data=data, headers=hr)
        #r.json()['code'] == 0: success
        return r.json()


    def deleteGroupAlbum(self, mid, albumId):
        params = {'homeId': mid}
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "DELETE",
            'Content-type': "application/json",
            'x-lpv': '1', #needless
            'x-lsr':'TW', #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/ext/album', '/api/v4/album/%s' % albumId, params)
        r = self.server.postContent(url, headers=hr)
        return r.json()
        

    def addImageToAlbum(self, mid, albumId, oid):
        #oid like 6cbff2e4100006b58db80f87ad8666bc.20121408
        params = {'homeId': mid}
        data = json.dumps({"photos":[{"oid": oid}]})
        
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': 'PUT',
            'content-type': "application/json",
            'x-album-stats': "e2FsYnVtUGhvdG9BZGRDb3VudD0xfQ==" #change it if you want update many images
        })

        url = self.server.urlEncode('https://gwz.line.naver.jp/ext/album', '/api/v3/photos/%s' % albumId, params)
        r = self.server.postContent(url, data=data, headers=hr)
        
        #{"code":0,"message":"success","result":true}
        return r.json()