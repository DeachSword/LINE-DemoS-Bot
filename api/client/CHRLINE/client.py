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
        else:
            self.requestSQR(device, version, os_name, os_ver)
       

    def initAll(self):
        pass