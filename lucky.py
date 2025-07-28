Name of student = input("enter the student name")
eng = 90
sci = 98
math = 88
total = ((eng+sci+math)/3)

if total > 90:
    print("Grade A")
elif total > 80 and total < 90:
    print("Grade B")
elif total < 35:
    print("fail")
else:
    print("Avrage grade")
    
