'''
    THIS FILE IS MADE BY DeachSword Team
    
    * You promise that you will not sell this file or its functions for profit-making behavior
    * You use this file only for research
    * This is a public file, so you should not modify any content of this header
    * It contains dangerous functions, if you know how to use it, please do not modify it for secondary dissemination
    
    
    version: 1.0.1
    author:  YinMo

'''
import requests, json


class DSClova(object):

    def __init__(self, token, udid):
        """
        if u need the token
        u can add DearSakura bot (Line ID: yinmo.dearsakura)
        send .createqrcode
        and enter clova
        login the qrcode, u will get the token and udid
        if failed, try again or report issue
        """
        self.gwUrl = "https://clova-cic.line-apps.com/internal/v1/messenger-gw/"
        self.token = token
        self.udid = udid
        self._request = requests.session()
        self._request.headers.update({
            'Authorization': f"Bearer {self.token}",
            'X-Client-DeviceId': self.udid,
            'Content-Type': "application/json"
        })

    def createAccountV3(self, displayName):
        payload = {
          "data": {
            "clovaHardwareId": self.udid,
            "displayName": f"{displayName}"
          },
          "method": "POST",
          "path": "/v3/shared_accounts"
        }
        botInfo = json.loads(self._request.post(self.gwUrl, data=json.dumps(payload)).text)
        return botInfo

    def updateName(self, sharedAccountBotId, displayName):
        # 也許有一些限制存在...?
        # 我使用v2進行改名, 並且以3秒間隔持續了6小時
        # 最後, 我收到了"資源不存在"
        # 它表示v2已不支援? 或是bot受到了規制?
        # 
        # 更新: 我必須暫時關閉此專案, 因為官方對其進行了調整
        #       調整內容包含了/v2, 所以這解釋了為甚麼我得到了"資源不存在"的錯誤
        #       如果你已經看到此檔案, 則代表它已被更新, 也許你可以正常使用它, 也許不能.
        payload = {
          "data": {
            "displayName": f"{displayName}"
          },
          "method": "PUT",
          "path": f"/shared_accounts/v2/{sharedAccountBotId}"
        }
        botInfo = json.loads(self._request.post(self.gwUrl, data=json.dumps(payload)).text)
        return botInfo

    def getLineSchemeToAddBotAsFriend(self, sharedAccountBotId):
        payload = {
          "method": "GET",
          "path": f"/shared_accounts/{sharedAccountBotId}/add_bot_scheme"
        }
        id = self._request.post(self.gwUrl, data=json.dumps(payload)).text #URL
        return id

    def getOwnerJoinGroups(self, sharedAccountBotId):
        ''' 主要帳號的所有群組 '''
        payload = {
          "method": "GET",
          "path": f"/shared_accounts/{sharedAccountBotId}/groups"
        }
        groups = json.loads(self._request.post(self.gwUrl, data=json.dumps(payload)).text)
        return groups

    def getGroup(self, sharedAccountBotId):
        ''' bot的群組 '''
        payload = {
          "method": "GET",
          "path": f"/shared_accounts/{sharedAccountBotId}/group"
        }
        groupInfo = json.loads(self._request.post(self.gwUrl, data=json.dumps(payload)).text)
        return groupInfo

    def addBotToGroup(self, sharedAccountBotId, groupMid):
        payload = {
          "method": "POST",
          "path": f"/shared_accounts/{sharedAccountBotId}/group/{groupMid}"
        }
        res = self._request.post(self.gwUrl, data=json.dumps(payload)).text
        return res

    def createLineGroupAndInviteFriends(self, sharedAccountBotId, groupName, inviteeIds):
        # LINE Security Team will keep an eye on u
        payload = {
          "data": {
            "groupName": groupName,
            "inviteeIds": inviteeIds
          },
          "method": "POST",
          "path": f"/v1/shared_accounts/{sharedAccountBotId}/group_invitation"
        }
        res = self._request.post(self.gwUrl, data=json.dumps(payload)).text
        return res

    def deleteAccount(self, sharedAccountBotId):
        payload = {
          "method": "DELETE",
          "path": f"/shared_accounts/{sharedAccountBotId}"
        }
        res = json.loads(self._request.post(self.gwUrl, data=json.dumps(payload)).text)
        return res

    def updateProfilePic(self, sharedAccountBotId, path):
        data = open(path, 'rb').read()
        headers = {
            "Authorization": f"Bearer {self.token}", 
            "X-Clova-Messenger-Bot-Id": sharedAccountBotId, 
            'Content-Type': 'image/jpeg'
            }
        res = self._request.post(self.gwUrl + 'profile-image', data=data, headers=headers)
        return res
        