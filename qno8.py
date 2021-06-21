# User se 10 students ke naam aur marks lekar unhe ek dictionary me store karaye. Output :- 

dict={}
for i in range (10):
    student_name=input("enter the name.")
    marks=input(":enter the marks")
    dict.update({student_name:marks})
    print(dict)

