# -*- coding: utf-8 -*-
import requests

class API(object):

    def __init__(self):
        self.req = requests.session()

    def requestSQR(self):
        _headers = {
            "x-lpqs": "/acct/lgn/sq/v1"
        }
        headers = {
            "x-line-application": "CHROMEOS\t2.4.1\tChrome_OS\t1",
            "x-lhm": "POST",
            "x-le": "18",
            "x-lcs": self._encryptKey,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "content-type": "application/x-thrift; protocol=TBINARY",
            "x-lst": "300000000",
            "x-lal": "zh_TW",
            "origin": "chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc",
            "cookie": "NNB=BNM4CAH53CCV6",
            "sec-ch-ua": '"Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "none",
            "accept": 'application/x-thrift',
            "accept-encoding": 'gzip, deflate, br',
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "authority": "gf.line.naver.jp",
            "method": "POST",
            "path": "/enc",
            "scheme": "https"
        }

        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 13, 99, 114, 101, 97, 116, 101, 83, 101, 115, 115, 105, 111, 110, 0, 0, 0, 0, 12, 0, 1, 0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data) + bytes([63, 151, 210, 246]) #last 4 bytes...
        headers["content-length"] = str(len(data))
        print(self.req.post("https://gf.line.naver.jp/enc", data=data, headers=headers))
        #todo decode res