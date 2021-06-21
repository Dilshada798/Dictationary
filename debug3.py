dict={}
c=0
for i in range(1,16):
    i=i**2
    c+=1
    dict.update({c:i})
print(dict)
