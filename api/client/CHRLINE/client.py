from .models import Models
from .api import API
from .thrift import Thrift

class CHRLINE(Models, API, Thrift):

    def __init__(self):
        Models.__init__(self)
        API.__init__(self)
        Thrift.__init__(self)
       

    def initAll(self):
        pass