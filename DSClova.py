
import requests, json


class DSClova(object):

    def __init__(self, token, udid):
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

    def sendMessage(self, sharedAccountBotId, text):
        payload = {
          "method": "GET",
          "path": f"/shared_accounts/{sharedAccountBotId}/add_bot_scheme"
        }
        id = self._request.post(self.gwUrl, data=json.dumps(payload)).text #URL
        return id

    def sendMessageV2(self, sharedAccountBotId, text):
        payload = {
          "method": "GET",
          "path": f"/shared_accounts/{sharedAccountBotId}/add_bot_scheme"
        }
        id = self._request.post(self.gwUrl, data=json.dumps(payload)).text #URL
        return id

    def sendMessageV3(self, sharedAccountBotId, text):
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
        # LINE Security Team
        # If you know how to use it
        # Please don't make it public
        # !!! If you are using it for profit, LINE will demand compensation from you in December, and they are currently continuously reviewing the usage records !!!
        return {}

    def deleteAccount(self, sharedAccountBotId):
        payload = {
          "method": "DELETE",
          "path": f"/shared_accounts/{sharedAccountBotId}"
        }
        res = json.loads(self._request.post(self.gwUrl, data=json.dumps(payload)).text)
        return res
        