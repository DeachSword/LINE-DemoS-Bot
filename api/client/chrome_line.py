from CHRLINE import *

cl = CHRLINE()
headers = {
    "X-Line-Access": "SQ4a4653687737647351757355464a546a78386675554974306f624b3352713442",
    "x-lpqs": "/acct/lp/lgn/sq/v1"
}
#print(cl._encryptKey)
#h = cl.encHeaders(headers)
#print(h)
#print(len(h))
print(cl.requestSQR())