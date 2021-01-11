from .models import Models
from .api import API
from .thrift import Thrift

class CHRLINE(Models, API, Thrift):

    def __init__(self, authToken=None, device="CHROMEOS", version="2.4.1", os_name="Chrome_OS", os_ver="1"):
        Models.__init__(self)
        API.__init__(self)
        Thrift.__init__(self)
        self.headers['x-line-application'] = "%s\t%s\t%s\t%s" % (device, version, os_name, os_ver)
        if authToken:
            self.authToken = authToken
            self.profile = self.getProfile()['getProfile']
            if 'error' in self.profile:
                raise Exception(f"登入失敗... {self.profile['error']}")
            print(f"[{self.profile[20]}] 登入成功 ({self.profile[1]})")
        else:
            self.requestSQR(device, version, os_name, os_ver)
       

    def initAll(self):
        pass