# -*- coding: utf-8 -*-
import requests

class API(object):

    def __init__(self):
        self.req = requests.session()
        self.headers = {
            "x-line-application": "CHROMEOS\t2.4.1\tChrome_OS\t1",
            "x-lhm": "POST",
            "x-le": "18",
            "x-lcs": self._encryptKey,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "content-type": "application/x-thrift; protocol=TBINARY",
            "x-lst": "300000000",
            "x-lal": "zh_TW",
        }

    def requestSQR(self):
        _headers = {
            "x-lpqs": "/acct/lgn/sq/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 13, 99, 114, 101, 97, 116, 101, 83, 101, 115, 115, 105, 111, 110, 0, 0, 0, 0, 12, 0, 1, 0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        
        data = self.decData(res.content)
        sqr = data[39:105].decode()
        url = self.createSession(sqr)
        print(f"URL: {url}")
        if self.checkQrCodeVerified(sqr):
            b = self.verifyCertificate(sqr)
            c = self.createPinCode(sqr)
            print(f"請輸入pincode: {c}")
            if self.checkPinCodeVerified(sqr):
                e = self.qrCodeLogin(sqr)
                return e.decode()
        return False
        
    def createSession(self, qrcode):
        _headers = {
            "x-lpqs": "/acct/lgn/sq/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 12, 99, 114, 101, 97, 116, 101, 81, 114, 67, 111, 100, 101, 0, 0, 0, 0, 12, 0, 1, 11, 0, 1, 0, 0, 0, 66]
        for qr in qrcode:
            sqrd.append(ord(qr))
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        #[127, 95, 38, 16]
        data = self.decData(res.content)
        url = data[38:128].decode()
        return url
        
    def checkQrCodeVerified(self, qrcode):
        _headers = {
            "X-Line-Access": qrcode,
            "x-lpqs": "/acct/lp/lgn/sq/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 19, 99, 104, 101, 99, 107, 81, 114, 67, 111, 100, 101, 86, 101, 114, 105, 102, 105, 101, 100, 0, 0, 0, 0, 12, 0, 1, 11, 0, 1, 0, 0, 0, 66]
        for qr in qrcode:
            sqrd.append(ord(qr))
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        if res.status_code == 200:
            return True
        return False
        
    def verifyCertificate(self, qrcode):
        _headers = {
            "x-lpqs": "/acct/lgn/sq/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 17, 118, 101, 114, 105, 102, 121, 67, 101, 114, 116, 105, 102, 105, 99, 97, 116, 101, 0, 0, 0, 0, 12, 0, 1, 11, 0, 1, 0, 0, 0, 66]
        for qr in qrcode:
            sqrd.append(ord(qr))
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        return data
        
    def createPinCode(self, qrcode):
        _headers = {
            "x-lpqs": "/acct/lgn/sq/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 13, 99, 114, 101, 97, 116, 101, 80, 105, 110, 67, 111, 100, 101, 0, 0, 0, 0, 12, 0, 1, 11, 0, 1, 0, 0, 0, 66]
        for qr in qrcode:
            sqrd.append(ord(qr))
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        return data[39:43].decode()
        
    def checkPinCodeVerified(self, qrcode):
        _headers = {
            "X-Line-Access": qrcode,
            "x-lpqs": "/acct/lp/lgn/sq/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 20, 99, 104, 101, 99, 107, 80, 105, 110, 67, 111, 100, 101, 86, 101, 114, 105, 102, 105, 101, 100, 0, 0, 0, 0, 12, 0, 1, 11, 0, 1, 0, 0, 0, 66]
        for qr in qrcode:
            sqrd.append(ord(qr))
        sqrd += [0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        if res.status_code == 200:
            return True
        return False
        
    def qrCodeLogin(self, qrcode):
        _headers = {
            "x-lpqs": "/acct/lgn/sq/v1"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 11, 113, 114, 67, 111, 100, 101, 76, 111, 103, 105, 110, 0, 0, 0, 0, 12, 0, 1, 11, 0, 1, 0, 0, 0, 66]
        for qr in qrcode:
            sqrd.append(ord(qr))
        sqrd += [11, 0, 2, 0, 0, 0, 8]
        for device in 'CHROMEOS':
            sqrd.append(ord(device))
        sqrd += [2, 0, 3, 0, 0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        pem = data[36:101] #64dig?
        print("證書: ", pem)
        _token = data[108:]
        return bytes(_token[:88]) # 88dig?
        token = []
        for t in _token:
            token.append(t)
            if t == b"=":
                break
        return bytes(token)
        
    def CPF(self, token):
        _headers = {
            'X-Line-Access': token, 
            'x-lpqs': "/CPF"
        }
        a = self.encHeaders(_headers)
        sqrd = []
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        return bytes(data)
        
    def getEncryptedIdentity(self, token):
        _headers = {
            'X-Line-Access': token, 
            'x-lpqs': "/S3"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 20, 103, 101, 116, 69, 110, 99, 114, 121, 112, 116, 101, 100, 73, 100, 101, 110, 116, 105, 116, 121, 0, 0, 0, 0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        return bytes(data)
        
    def getProfile(self, token):
        _headers = {
            'X-Line-Access': token, 
            'x-lpqs': "/S3"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 10, 103, 101, 116, 80, 114, 111, 102, 105, 108, 101, 0, 0, 0, 0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        return bytes(data)
        
    def getSettings(self, token):
        _headers = {
            'X-Line-Access': token, 
            'x-lpqs': "/S3"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 11, 103, 101, 116, 83, 101, 116, 116, 105, 110, 103, 115, 0, 0, 0, 0, 0]
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        return bytes(data)
        
    def issueChannelToken(self, token):
        _headers = {
            'X-Line-Access': token, 
            'x-lpqs': "/CH3"
        }
        a = self.encHeaders(_headers)
        sqrd = [128, 1, 0, 1, 0, 0, 0, 17, 105, 115, 115, 117, 101, 67, 104, 97, 110, 110, 101, 108, 84, 111, 107, 101, 110, 0, 0, 0, 0, 11, 0, 1, 0, 0, 0, 10, 49, 52, 51, 51, 53, 55, 50, 57, 57, 56, 0]
        # 1433572998
        # 49, 52, 51, 51, 53, 55, 50, 57, 57, 56
        sqr_rd = a + sqrd
        _data = bytes(sqr_rd)
        data = self.encData(_data)
        res = self.req.post("https://gf.line.naver.jp/enc", data=data, headers=self.headers)
        data = self.decData(res.content)
        return bytes(data)
        
