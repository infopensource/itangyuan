import base64

def to_base64(string):
      string=string.encode("utf-8")
      return str(base64.b64encode(string))[2:-2]

inp=eval(input())
path=input()

f= open(path,"a",encoding="utf-8",errors="ignore")
for i in inp:
      f.write(to_base64(i)+'\n')
f.close()
