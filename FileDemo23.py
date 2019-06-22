import _csv
with open('abcsc._csv','w')as f:
    w=_csv.writer(f)
    w.writerow(['NAME','ROLLNO','MARKS','ADDRESS'])
    while True:
        name=input("Enter student name :")
        rollno=input("Roll no :")
        marks=input("Marks :")
        address=input("Address :")
	w.writerow([name,rollno,marks,address])
        option=input("do you want insert one more records Y/N")
	if option.lower()=='No':
	    break
print("Total students files written in to file")

