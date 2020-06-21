from LINEBASE.LINEBASE import *
from LINEBASE.LINEBASE import ttypes, SecondaryQrCodeLoginPermitService, SecondaryQrCodeLoginService
from LINEBASE.LINEBASE.hooks import HooksTracer
from copy import deepcopy
import sys, traceback, json, os, hashlib, threading
import time
import random
import traceback

# Start Initialize
cl = LINE('token')
tracer = HooksTracer(cl, noError=True)
    
myWife = "狗狗"
myWifeList = ['狗狗','聖夜', '獨眼龍貓驢子']
class OpHook(object):
    myWife = "狗狗"
    @tracer.Before("Operation")
    def __before(self,cl,op):
        pass
        '''
        if op.type != 0:
            self.log("[GOT_OPERATION][%s] <Param1 %s> <Param2 %s> <Param3 %s>"%(op.type,op.param1,op.param2,op.param3))
            self.log(op)
        '''
    
    @tracer.After("Operation")
    def __after(self,cl,op):
        pass

    @tracer.Operation(26)
    def got_message(self,cl,op):
        global myWife
        global myWifeList
        msg = op.message
        if msg.to == group_id: # change group_id
            if msg.contentType == 7:
                if myWife == myWifeList[-1]:
                    myWife = myWifeList[0]
                else:
                    index = myWifeList.index(myWife)
                    myWife = myWifeList[(index+1)]
                print('change my wife : %s'%myWife)
            ck = cl.talk.getRecentMessagesV2(msg.to,1)
            if len(ck) > 0:
                if ck[0]._from != cl.profile.mid:
                    cl.sendMessage(msg.to, '%s我婆\n\n%s'%(myWife, time.strftime("%H:%M")))
                else:
                    print('is me!')

class ContentHook(object):
    @tracer.Content(0)
    def MESSAGE(self,cl,msg):
        # This is required to execute command.
        if self.getPermissionById(msg._from) == []:
            self.addPermission(msg._from,"normal")
            self.resetUser(msg._from)

tracer.addClass(OpHook())
tracer.addClass(ContentHook())
tracer.run()