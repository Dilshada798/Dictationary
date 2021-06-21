dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
dict={}
for i in dic:
    j=dic[i]
    for i in dic:
        a=dic[i]
        if j>a:
            dict[i]=a
for i in dic:
    j=dic[i]
    for i in dic:
        a=dic[i]
        if j<a:
            dict[i]=a
print(dict)
