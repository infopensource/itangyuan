import base64

def from_base64(string):
      return str(base64.b64decode(string))[2:-1]

path=input()

f= open(path,"r",encoding="utf-8",errors="ignore")
comments=[]
for each_line in f:
      comments.append(from_base64(str(each_line[:-1]+"=").replace(' ','')))
f.close()
