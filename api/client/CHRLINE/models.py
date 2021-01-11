from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
import Crypto.Cipher.PKCS1_OAEP as rsaenc
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from hashlib import md5, sha1
import xxhash

class Models(object):

    def __init__(self):    
        self.PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0LRokSkGDo8G5ObFfyKiIdPAU5iOpj+UT+A3AcDxLuePyDt8IVp9HpOsJlf8uVk3Wr9fs+8y7cnF3WiY6Ro526hy3fbWR4HiD0FaIRCOTbgRlsoGNC2rthp2uxYad5up78krSDXNKBab8t1PteCmOq84TpDCRmainaZQN9QxzaSvYWUICVv27Kk97y2j3LS3H64NCqjS88XacAieivELfMr6rT2GutRshKeNSZOUR3YROV4THa77USBQwRI7ZZTe6GUFazpocTN58QY8jFYODzfhdyoiym6rXJNNnUKatiSC/hmzdpX8/h4Y98KaGAZaatLAgPMRCe582q4JwHg7rwIDAQAB\n-----END PUBLIC KEY-----"
        self.key = RSA.importKey(self.PUBLIC_KEY)
        self.encryptKey = b"DearSakura+2020/"
        self.IV = bytes([78, 9, 72, 62, 56, 245, 255, 114, 128, 18, 123, 158, 251, 92, 45, 51])
        self.cipher = AES.new(self.encryptKey, AES.MODE_CBC, iv=self.IV)
        self.d_cipher = AES.new(self.encryptKey, AES.MODE_CBC, iv=self.IV)
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
        _data = AES.new(self.encryptKey, AES.MODE_CBC, iv=self.IV).encrypt(pad(data, AES.block_size))
        debug = []
        return _data + self.XQqwlHlXKK(self.encryptKey, _data)
        
    def decData(self, data):
        data = pad(data, AES.block_size)
        _data = AES.new(self.encryptKey, AES.MODE_CBC, iv=self.IV).decrypt(data)
        i = 1
        data = self.yVdzCLDwMN(_data, i)
        i = 3
        return _data
        
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
                _i = int(t[i:i + 2], 16)
            except:
                _i = 16
            e.append(_i);
            i += 2
        return e
        
    def XQqwlHlXKK(self, e, i):
        r = []
        for o in range(16):
            r.append(92 ^ e[o])
        n = xxhash.xxh32(b'',seed=0)
        s = xxhash.xxh32(b'',seed=0)
        n.update(bytes(r))
        for o in range(16):
            r[o] ^= 106
        s.update(bytes(r))
        s.update(i)
        a = s.hexdigest() # is b8a7c677?
        n.update(bytes(self.pmAWhahfKx(a)))
        c = n.hexdigest() # is 3f97d2f6?
        d = self.pmAWhahfKx(c)
        return bytes(d)
        
    def yVdzCLDwMN(self, d, i):
        return (255 & self.xnEmbaRWhy(d, i)) << 8 | 255 & self.xnEmbaRWhy(d, i+1)
    
        
    def xnEmbaRWhy(self, d, i):
        t = d[i];
        if t > 127:
            t = 0 - (t - 1 ^ 255)
        return t
        
    def tryReadData(self, data):
        _data = {}
        if data[4] == 128:
            a = 12 + data[11]
            b = data[12:a].decode()
            _data[b] = {}
            c = data[a + 4]
            id = data[a + 6]
            if id == 0:
                if c == 11:
                    d = data[a + 10]
                    e = data[a + 11:a + 11 + d].decode()
                    _data[b] = e
                elif c == 12:
                    _data[b] = self.readContainerStruct(data[a + 7:])
            else:
                t_l = data[a + 20]
                _data[b] = {
                    "error": data[a + 21:a + 21 + t_l].decode()
                }
        return _data
        
    def readContainerStruct(self, data, get_data_len=False):
        _data = {}
        nextPos = 0
        id = data[2]
        if data[0] == 2:
            a = data[3]
            if a == 1:
                _data[id] = True
            else:
                 _data[id] = False
            nextPos = 8
        elif data[0] == 10:
            a = int.from_bytes(data[4:11], "big")
            _data[id] = a
            nextPos = 11
        elif data[0] == 11:
            a = int.from_bytes(data[5:7], "big")
            b = data[7:a+7]
            _data[id] = b.decode()
            nextPos = a + 7
        elif data[0] == 12:
            a = self.readContainerStruct(data[3:], True)
            print(a) # 解決 nextPos ?
            _data[id] = a[0]
            #nextPos = 3 + a[1]
        elif data[0] == 13:
            # list? dict?
            # 0D 00 24 0B 0B 00 00 00 02 00 00 00 07
            # what is 24?
            a = data[4] # value type? todo it?
            b = data[8] # count
            c = 12
            _d = {}
            for d in range(b):
                e = data[c] # key len
                f = c + 1 + e
                g = data[f + 3] # value len
                h = f + 4 + g
                _key = data[c+1:f].decode()
                _value = data[f + 4:h].decode()
                _d[_key] = _value
                c = h + 3
            _data[id] = _d
            nextPos = h
        else:
            print(f"[readContainerStruct]不支援Type: {data[0]} => ID: {id}")
        if _data and nextPos > 0:
            data = data[nextPos:]
            c = self.readContainerStruct(data, True)
            if c[0]:
                _data.update(c[0])
        if get_data_len:
            return [_data, nextPos]
        return _data