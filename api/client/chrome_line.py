from CHRLINE import *

cl = CHRLINE()
#cl = CHRLINE(device="IOSIPAD", version="10.21.3", os_name="iOS", os_ver="11") with IOSIPAD
token = cl.authToken
print(f"authToken: {token}")

print(cl.profile) # Profile
print(cl.sendMessage('uaff1346eb5adc4928c6b99cda0272226', 'hello world')) # send message