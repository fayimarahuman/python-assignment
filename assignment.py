#Assignments
#1.print the names Patricia, Phionah and Anitah
#2.Add masha at the 4th position
#3.Update the Phionah to Phiona Aladina
#4.Display the length of the students list
#5.print all the students name using a for loop
#6.calculate the total marks for the student mark variable and the total mark is 304
studentNames=['Sandra','Patricia','Phiona','Anitah']
studentMarks=[80,56,78,90]
#Ans.1
print(studentNames[1])
print(studentNames[2])
print(studentNames[3])
#Ans.2
studentNames.insert(4,'Masha')
print(studentNames)
#Ans.3
studentNames[2]='Phionah Aladina'
print(studentNames)
#Ans.4
studentNames=['Sandra','Patricia','Phiona','Anitah']
print(len(studentNames))
#Ans.5
studentNames=['Sandra','Patricia','Phiona','Anitah']
for items in studentNames:
    print(items)
#Ans.6
totalMark=(80+56+78+90)
print(totalMark)

