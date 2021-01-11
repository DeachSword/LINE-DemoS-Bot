from CHRLINE import *

cl = CHRLINE()
token = cl.requestSQR()
print(f"authToken: {token}")

print(cl.getProfile(token)) # Profile
print(cl.testFunc(token, '/S3', 'getContact', 'uaff1346eb5adc4928c6b99cda0272226', 2)) # Contact 