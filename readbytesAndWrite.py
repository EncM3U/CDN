import os
import chardet
f = open(input("What to open:"), mode='rb')
byt=f.read()
f.close()
l=open(input("What to write:"),mode="w")
l.write(byt)
l.close()