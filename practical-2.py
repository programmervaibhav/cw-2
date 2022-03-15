# result analysis of student
fname = (input("Enter your Full Name: "))
email = input("Enter your Uni registerd Email ID: ")
brn = (input("Enter your branch name: "))
print("Enter only the number for roll No. and Semester")
roll = int(input("What's your Roll no? "))
sem = input("What Semester are you in? ")

print('''Let's check your marks
(Enter marks out of 70)''')
os = int(input("Enter your Operating System(OS) Marks: "))
oop = int(input("Enter your Object Oriented Programming with Java (OOP+JAVA) Marks: "))
mth = int(input("Enter your Maths Marks: "))
cads = int(input("Enter your Computer architecture and digital system Marks: "))

        

#Total Marks
tol = str(os + oop + mth + cads) + "/280"

#percentage calculation
peros = (os*100)//70
peroop = (oop*100)//70
permth = (mth*100)//70
percads = (cads*100)//70
percent = (peros + peroop + permth + percads)//4

#Grade Calculation
if percent >= 80 :
    grd = "AA"
    sta = "PASS"
if percent >= 70 and percent < 80:
    grd = "AB"
    sta = "PASS"
if percent >= 60 and percent < 70:
    grd = "BB"
    sta = "PASS"
if percent >= 55 and percent < 60:
    grd = "BC"
    sta = "PASS"
if percent >= 50 and percent < 55:
    grd = "CC"
    sta = "PASS"
if percent >= 45 and percent < 50:
    grd = "CD"
    sta = "PASS"
if percent >= 40 and percent < 45:
    grd = "DD"
    sta = "PASS"
if percent >= 0 and percent < 40:
    grd = "FF"
    sta = "FAIL"



#MarkSheet 
print("\nCreating your MarkSheet...")
print("Name:", fname, "\t\t\tRoll No.", roll)
print("Email:", email, "\t\t\tSemester: ", sem)
print("Subject\t\t\tMarks\t\t\tPercentage")
print("os\t\t\t", os, "\t\t\t", peros )
print("oop\t\t\t", oop, "\t\t\t",peroop)
print("Maths\t\t\t", mth, "\t\t\t", permth)
print("cads","\t\t\t",cads,"\t\t\t",percads)
print("Percentage: ",percent,"\t\t\tTotal Marks:",tol)
print("Grade: ",grd,"\t\t\tStatus: ",sta)
