from .models import Models
from .api import API

class CHRLINE(Models, API):

    def __init__(self):
        Models.__init__(self)
        API.__init__(self)
       

    def initAll(self):
        pass