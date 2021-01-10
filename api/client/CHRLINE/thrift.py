from struct import pack, unpack
from io import BytesIO as BufferIO

class Thrift(object):
    
    def __init__(self):  
        self.TYPE_MASK = 0x000000ff