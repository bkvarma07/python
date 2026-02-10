#student performance analyzer
n=int(input("Enter the number of Student: "))
marks=[0]*n
for i in range(n):
    marks[i]=int(input("enter mark: "))
valid=0
failed=0
#personalization details
student_id="AP24110011146"

for i in marks:
    if(i>=90 and i<=100):
        print("Mark:",i,"->Excellent")
        valid+=1
    elif(i>=75 and i<=89):
        print("Mark:",i,"->Very Good")
        valid+=1
    elif(i>=60 and i<=74):
        print("Mark:",i,"->Good")
        valid+=1
    elif(i>=40 and i<=59):
        print("Mark:",i,"->Average")
        valid+=1
    elif(i>=0 and i<=39):
        #personalization logic
        if(i==39 and student_id=="AP24110011146"):
            print("Mark:",i,"->Average(*)")
        else:
            print("Mark:",i,"->Fail")
            failed+=1
        valid+=1
    else:
        print("Mark:",i,"->Invalid")

print("Total Valid Studets: ",valid)
print("Total Failed Studets: ",failed)