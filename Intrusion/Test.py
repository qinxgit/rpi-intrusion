import PIR
from PIR import *
import ptvsd


ptvsd.enable_attach(secret='my_secret')

x=PIRDetector()
x.Init()
try:
    x.Detect()
except KeyboardInterrupt:
    x.Clearup()
