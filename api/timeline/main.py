# -*- coding: utf-8 -*-

import json, time, base64

class Timeline():


    def changeGroupAlbumName(self, mid, albumId, name):
        data = json.dumps({'title': name})
        params = {'homeId': mid}
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "PUT",
            'Content-type': "application/json",
            'x-lpv': 1, #needless
            'x-lsr':'TW', #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode('https://gwz.line.naver.jp/ext/album', '/api/v3/album/%s' % albumId, params)
        r = self.server.postContent(url, data=data, headers=hr)
        #r.json()['code'] == 0: success
        return True