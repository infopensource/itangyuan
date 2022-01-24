
f = open("username.txt","r")
# print(f.read())
get = f.read()
 
#直接用splitlines（）放法来实现行分割
other_result = get.splitlines()
for i in range (len(other_result)):
 print(other_result[i])
 print("******")
 
f.close()
