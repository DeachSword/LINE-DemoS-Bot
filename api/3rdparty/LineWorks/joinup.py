import requests, json


class LineWorksJoinClient():
    def __init__(self):
        self.headers = {
            'Referer': 'https://join.worksmobile.com/jp/joinup-v3/step1?isLoad=true',
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        self.stepKey = None
        self.req = requests.session()
        
    def initStep(self):
        response = self.req.get(
            'https://join.worksmobile.com/jp/joinup-v3/step1?isLoad=true',
        )

    def getStepKey(self):
        self.headers["Referer"] = 'https://join.worksmobile.com/jp/joinup-v3/step1?isLoad=true'
        response = self.req.get(
            'https://join.worksmobile.com/jp/joinup/initInfo?isLoadPage=false&campaignNo=',
            headers=self.headers
        )
        self.stepKey = response.json()["stepKey"]
        return self.stepKey
        
    def translate(self, lastName, firstName):
        headers = {
            "Referer": 'https://join.worksmobile.com/jp/joinup-v3/step3-other?isLoad=true',
            'Content-Type': "application/json",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        data = {
            'companyName': "deachsword", 
            'lastName': lastName, 
            'firstName': firstName
        }
        response = self.req.post(
            f"https://join.worksmobile.com/jp/joinup/v2/{self.stepKey}/translate",
            headers=headers,
            data=json.dumps(data)
        )
        
    def getGroupCache(self, groupId, userId, userPassword,
        userFirstName, userLastName):
        self.headers["Referer"] = 'https://join.worksmobile.com/jp/joinup-v3/step3-other?isLoad=true'
        response = self.req.post(
            f'https://join.worksmobile.com/jp/joinup/v2/{self.stepKey}/domains/cache',
            headers=self.headers,
            json={
                "lastName": userLastName,
                "countryCode": "+81",
                "joinEnv": "PC",
                "domain": groupId,
                "joinType": "B_WORKS",
                "companyName": "deachsword",
                "cellphone": "",
                "invitedCompanyName": "",
                "lineId": "",
                "invitedGroupName": "",
                "campaignNo": "",
                "stepKey": self.stepKey,
                "groupInviteCode": "",
                "emailId": userId,
                "firstName": userFirstName,
                "password": userPassword,
                "personalEmail": "",
                "domainId": ""
            }
        )
        return response.json()["code"] == "SUCCESS"
    def checkCompanyName(self):
        self.headers["Referer"] = 'https://join.worksmobile.com/jp/joinup-v3/step1?isLoad=true'
        response = self.req.post(
            f'https://join.worksmobile.com/jp/joinup/v2/{self.stepKey}/checkCompanyName',
            headers=self.headers,
            json={
                "companyName": "deachsword"
            }
        )
        return response.json()
    def checkGroupId(self, groupId):
        self.headers["Referer"] = 'https://join.worksmobile.com/jp/joinup-v3/step3-other?isLoad=true'
        response = self.req.post(
            f'https://join.worksmobile.com/jp/joinup/v2/{self.stepKey}/groupName/check',
            headers=self.headers,
            json={
                "domain": groupId,
                "stepKey": self.stepKey
            }
        )
        return response.json()["code"] == "SUCCESS"

    def createGroup(self, groupId, userId, userPassword, userFirstName, userLastName):
        self.headers["Referer"] = 'https://join.worksmobile.com/jp/joinup-v3/step5?isLoad=true'
        self.headers["Referer"] = 'https://join.worksmobile.com/jp/joinup-v3/step5?isLoad=true'
        response = self.req.post(
            f'https://join.worksmobile.com/jp/joinup/v2/{self.stepKey}/domains',
            headers=self.headers,
            json={
                "lastName": userLastName,
                "countryCode": "+81",
                "joinEnv": "PC",
                "domain": groupId,
                "joinType": "B_WORKS",
                "companyName": "deachsword",
                "joinAuthType": "",
                "cellphone": "",
                "invitedCompanyName": "",
                "lineId": "",
                "invitedGroupName": "",
                "campaignNo": "",
                "stepKey": self.stepKey,
                "groupInviteCode": "",
                "emailId": userId,
                "firstName": userFirstName,
                "password": userPassword,
                "personalEmail": "",
                "domainId": ""
            }
        )
        resp = response.json()
if __name__ == "__main__":
    for i in range(50):
        cl = LineWorksJoinClient()
        cl.initStep()
        cl.getStepKey()
        userFirstName = "Dear"
        userLastName = "Sakura"
        cl.translate(userLastName, userFirstName)
        userId = 'dsss.' + str(i)
        userPassword = "f78g781a7" + str(i)
        groupId = "ds-" + str(i)
        cl.getGroupCache(groupId, userId, userPassword, userFirstName, userLastName)
        response = cl.createGroup(groupId, userId, userPassword, userFirstName, userLastName)
        print(f"https://works.do/R/ti/p/{userId}@{groupId}")