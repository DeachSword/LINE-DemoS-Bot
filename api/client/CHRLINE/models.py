from Crypto.PublicKey import RSA
import Crypto.Cipher.PKCS1_OAEP as rsaenc
from base64 import b64encode, b64decode

class Models(object):

    def __init__(self):    
        self.PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0LRokSkGDo8G5ObFfyKiIdPAU5iOpj+UT+A3AcDxLuePyDt8IVp9HpOsJlf8uVk3Wr9fs+8y7cnF3WiY6Ro526hy3fbWR4HiD0FaIRCOTbgRlsoGNC2rthp2uxYad5up78krSDXNKBab8t1PteCmOq84TpDCRmainaZQN9QxzaSvYWUICVv27Kk97y2j3LS3H64NCqjS88XacAieivELfMr6rT2GutRshKeNSZOUR3YROV4THa77USBQwRI7ZZTe6GUFazpocTN58QY8jFYODzfhdyoiym6rXJNNnUKatiSC/hmzdpX8/h4Y98KaGAZaatLAgPMRCe582q4JwHg7rwIDAQAB\n-----END PUBLIC KEY-----"
        self.key = RSA.importKey(self.PUBLIC_KEY)
        self.encryptKey = b"DearSakura+2020/"
        self.cipher = rsaenc.new(self.key)
        self._encryptKey = b"0005" + b64encode(self.cipher.encrypt(self.encryptKey))
    
    def encHeaders(self):
        headers = {
            "X-Line-Access": "SQ4a4653687737647351757355464a546a78386675554974306f624b3352713442",
            "x-lpqs": "/acct/lp/lgn/sq/v1"
        }
        t = headers.keys()
        data = []
        for i in t:
            self.mFhrnmxnNF(len(t), data)
            print(data)
            self.mFhrnmxnNF(len(i), data)
            self.wYEpEYldst(i, data)
            self.mFhrnmxnNF(len(headers[i]), data)
            self.wYEpEYldst(headers[i], data)
        return data
        
    
    def mFhrnmxnNF(self, t, e):
        i = 65536 
        if t < -1 * 32768 or t >= i:
            raise Exception(t + " is incorrect for i16.")
        e.append(255 & t >> 8)
        e.append(255 & t)
        
    def wYEpEYldst(self, t, e):
        for i in range(len(t)):
            e.append(ord(t[i]))