a="MISSISSIPPI" 
dic={}
for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)


dic={}
num=input("enter the name:")
for i in num:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]=dic[i]+1
print(dic)

