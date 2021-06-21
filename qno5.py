list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]  
y={}
for i in list1:
    for value in list2:
        y[i]=value
        list2.remove(value)
        break
print(y)



