from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import Crypto.Cipher.PKCS1_OAEP as rsaenc
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad

class Models(object):

    def __init__(self):    
        self.PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0LRokSkGDo8G5ObFfyKiIdPAU5iOpj+UT+A3AcDxLuePyDt8IVp9HpOsJlf8uVk3Wr9fs+8y7cnF3WiY6Ro526hy3fbWR4HiD0FaIRCOTbgRlsoGNC2rthp2uxYad5up78krSDXNKBab8t1PteCmOq84TpDCRmainaZQN9QxzaSvYWUICVv27Kk97y2j3LS3H64NCqjS88XacAieivELfMr6rT2GutRshKeNSZOUR3YROV4THa77USBQwRI7ZZTe6GUFazpocTN58QY8jFYODzfhdyoiym6rXJNNnUKatiSC/hmzdpX8/h4Y98KaGAZaatLAgPMRCe582q4JwHg7rwIDAQAB\n-----END PUBLIC KEY-----"
        self.key = RSA.importKey(self.PUBLIC_KEY)
        self.encryptKey = b"DearSakura+2020/"
        self.IV = bytes([78, 9, 72, 62, 56, 245, 255, 114, 128, 18, 123, 158, 251, 92, 45, 51])
        self.cipher = AES.new(self.encryptKey, AES.MODE_CBC, iv=self.IV)
        self.encEncKey()

    def encHeaders(self, headers):
        t = headers.keys()
        data = []
        self.mFhrnmxnNF(len(t), data)
        for i in t:
            self.mFhrnmxnNF(len(i), data)
            self.wYEpEYldst(i, data)
            self.mFhrnmxnNF(len(headers[i]), data)
            self.wYEpEYldst(headers[i], data)
        o = len(data);
        data = [255 & o] + data
        data = [255 & o >> 8] + data
        return data
        
    def encEncKey(self):
        # heh
        a = rsaenc.new(self.key)
        self._encryptKey = "0005" + b64encode(a.encrypt(self.encryptKey)).decode()
        
    def encData(self, data):
        _data = self.cipher.encrypt(pad(data, AES.block_size))
        return _data
        #return _data + self.XQqwlHlXKK(self.encryptKey, _data)
        
    def mFhrnmxnNF(self, t, e):
        i = 65536 
        if t < -1 * 32768 or t >= i:
            raise Exception(t + " is incorrect for i16.")
        e.append(255 & t >> 8)
        e.append(255 & t)
        
    def wYEpEYldst(self, t, e):
        for i in range(len(t)):
            e.append(ord(t[i]))
        
    def xZVpUuXFru(t):
        if 8 == len(t):
            return t
        e = ""
        i = 0
        n = 8 - len(t)
        while i < n:
            e += "0"
            i += 1
        return e + t
        
    def pmAWhahfKx(self, t):
        e = []
        i = 0 
        n = len(t)
        while i < n:
            _i = 0
            try:
                _i = int(t[i:i + 2])
            except:
                _i = 16
            e.append(_i);
            i += 2
        return e
        
    def XQqwlHlXKK(self, e, i):
        r = []
        for o in range(16):
            r[o] = 92 ^ ord(e[o])
        
        
        
        #n.update(new Uint8Array(r).buffer
        for o in range(16):
            r[o] ^= 106
        #s.update(new Uint8Array(r).buffer)
        s.update(i)
            

        #var a = this.xZVpUuXFru(s.digest().toString(16));
        #n.update(this.pmAWhahfKx(a).buffer);
        #var c = this.xZVpUuXFru(n.digest().toString(16));
        #return this.pmAWhahfKx(c)
        #[35, 62, 236, 68]
            