# -*- coding: utf-8 -*-

# ------------------------------------------------ #
# 模仿DemoS Bot製作的Python版本
# 很少碰python 有語法錯誤請進行回報
# 改寫源項目: DemoS Bot (最後星塵[PHP])
# 作者: YinMo
# 注意: 此仿製檔使用的API是Linepy, 並不是最後星塵
# ------------------------------------------------ #

from linepy import *
import os, sys, time, json, random, threading, datetime, math

#import locale
#locale.setlocale(locale.LC_CTYPE, 'chinese')

DoREV = {
    'text':[],
    'image':[],
    'sticker':[]
} #Review Group
DEBUG = {
    'IMG':{},
    'VIE':{},
    'MSG':{}
}

REVMSGID = []
REVMSG = {}
REVIMG = {}
REVSTK = {}
READ = {}
BOT_NAME = 'DemoS@仿製機'
BOT_TOKEN = LINE().authToken
BOT_SUPERTOKEN = '1339e07174bac5bfb64d8a443ac43b7a'
GROUP_MAX = 100
GROUP_JOIN_NP = 15
GPS = {}
GAME = {}
ReadyGame = []

NEWS = ''''''
VERSION = '1.0 Alpha (1.0.0.0)'

ADMIN = ['ud4045303d1cf300eca5f32fb1ba85376']
VIP = ['ud4045303d1cf300eca5f32fb1ba85376']

try:
    client = LINE(BOT_SUPERTOKEN, systemName="DeachSword")
    #linepy login...by token
    ###帳密登入請使用 LINE('帳號', '密碼')
    ###qrcode網址登入使用 LINE()
    print(client.authToken)
except Exception as e:
    print('Error: ' + str(e))



def RECEIVE_MESSAGE(Op):
    msg = Op.message

    text = msg.text
    msg_id = msg.id
    receiver = msg.to
    sender = msg._from

    if msg.contentType == 0:
        if msg.toType == 0:
            pass
        elif msg.toType == 1:
            client.leaveRoom(receiver) #自動離開副本
        elif msg.toType == 2:
            if receiver in READ:
               pass
            if msg.contentType == 0:
                if receiver in DoREV['text']:
                    BuildRMSG = {}
                    BuildRMSG['type'] = 'text'
                    BuildRMSG['sender'] = sender
                    BuildRMSG['text'] = text
                    contentMetadata = None
                    BuildRMSG['data'] = contentMetadata
                    BuildRMSG['time'] = time.strftime("%M%D%H%M")
                    REVMSG[msg.id] = BuildRMSG
                elif msg.contentType == 1:
                    if receiver in DoREV['image']:
                        igp = r'./%s'%(msg.id)
                        client.downloadObjectMsg(msg.id, 'path', igp)
                        BuildRIMG = {}
                        BuildRIMG['type'] = 'image'
                        BuildRIMG['MCI'] = 'image'
                        BuildRIMG['sender'] = sender
                        BuildRIMG['data'] = None
                        BuildRIMG['time'] = time.strftime("%M%D%H%M")
                        REVMSG[msg.id] = BuildRIMG
                elif msg.contentType == 7:
                    if receiver in DoREV['sticker']:
                        BuildRSTK = {}
                        BuildRSTK['type'] = 'sticker'
                        BuildRSTK['sender'] = sender
                        BuildRSTK['data'] = msg.contentMetadata['STKID']
                        BuildRSTK['time'] = time.strftime("%M%D%H%M")
                        REVMSG[msg.id] = BuildRSTK
            if msg.contentType == 0:
                if text == "#review:text":
                    s = GroupSetting(receiver)
                    if s.get('review', False) == True:
                        s['review'] = False
                        DoREV['text'].remove(receiver)
                        reply = '關閉'
                    else:
                        s['review'] = True
                        DoREV['text'].append(receiver)
                        reply = '開啟'
                    #SaveGST(receiver, s)
                    sendMessage(u'成功更改設定: %s'%(reply), receiver, _from)
                elif text == "#review:image" and msg.toType == 2:
                    s = GroupSetting(receiver)
                    if s.get('review', False) == True:
                        s['review_image'] = False
                        DoREV['image'].remove(receiver)
                        reply = '關閉'
                    else:
                        s['review_image'] = True
                        DoREV['image'].append(receiver)
                        reply = '開啟'
                    #SaveGST(receiver, s)
                    sendMessage(u'成功更改設定: %s'%(reply), receiver, _from)
                elif text == "#review:sticker" and msg.toType == 2:
                    s = GroupSetting(receiver)
                    if s.get('review_sticker', False) == True:
                        s['review_sticker'] = False
                        DoREV['sticker'].remove(receiver)
                        reply = '關閉'
                    else:
                        s['review_sticker'] = True
                        DoREV['sticker'].append(receiver)
                        reply = '開啟'
                    #SaveGST(receiver, s)
                    sendMessage(u'成功更改設定: %s'%(reply), receiver, _from)

def NOTIFIED_DESTROY_MESSAGE(Op):
    if op.param2 in REVMSG:
        GRM = REVMSG[op.param2]
        if GRM['type'] == 'text':
            client.sendMessage(op.param1, "@player嘗試想收回訊息www\n他想收回的內容是: %s"%(GRM['text']), {'MENTION':'{"MENTIONEES":[{"S":"0","E":"7","M":"%s"}]}'})
        elif GRM['type'] == 'sticker':
            client.sendMessage(op.param1, "@player嘗試想收回訊息www\n他想收回的內容是一則貼圖OxO", {'MENTION':'{"MENTIONEES":[{"S":"0","E":"7","M":"%s"}]}'%(GRM['sender'])})
            url = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/' + GRM['data'] + '/ANDROID/sticker.png'
            try:
                client.sendImageWithURL(op.param1, url)
            except:
                client.sendMessage(op.param1, "嘛...也罷, 就放妳一馬吧(゜∀。)")
        elif GRM['type'] == 'image':
            client.sendMessage(op.param1, "@player嘗試想收回訊息www\n他想收回的內容是一張圖片(Ŏ艸Ŏ)\n來看看他想收回甚麼不可告人的圖片吧w", {'MENTION':'{"MENTIONEES":[{"S":"0","E":"7","M":"%s"}]}'%(GRM['sender'])})
            igp = r'./%s'%(op.param2)
            try:
                client.sendImage(op.param1, igp)
            except:
                client.sendMessage(op.param1, "嘛...也罷, 就放妳一馬吧(゜∀。)")
        else:
            client.sendMessage(op.param1, "@player嘗試想收回訊息www\n他想收回的內容是我不能解析的類型_(:3」∠)_", {'MENTION':'{"MENTIONEES":[{"S":"0","E":"7","M":"%s"}]}'%(GRM['sender'])})
        del REVMSG[op.param2] #釋放


def GroupSetting(group):
    if group not in GPS:
        GPS[group] = {}
    return GPS[group]


oepoll = OEPoll(client)
oepoll.addOpInterruptWithDict({
    OpType.RECEIVE_MESSAGE: RECEIVE_MESSAGE,
    OpType.NOTIFIED_DESTROY_MESSAGE: NOTIFIED_DESTROY_MESSAGE
})

while True:
    oepoll.trace()