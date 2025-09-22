grades=[]
num=float(input("Enter the first grade: "))
grades.append(num)
num=float(input("Enter the second grade: "))
grades.append(num)
num=float(input("Enter the third grade: "))
grades.append(num)
num=float(input("Enter the fourth grade: "))
grades.append(num)
num=float(input("Enter the fifth grade: "))
grades.append(num)
minimumGrade=(min(grades))
grades.remove(minimumGrade)
minimumGrade=(min(grades))
grades.remove(minimumGrade)
average=sum(grades)/len(grades)
print("Average Grade: {:.2f}".format(average))

#nyobapakeloop
grades=[]
n_str=input("Grade indeks: ")
n=int(n_str)
for i in range(n):
    num=float(input(f"Enter the {i+1} grade: "))
    grades.append(num)
    i+=1
minimumGrade=(min(grades))
grades.remove(minimumGrade)
minimumGrade=(min(grades))
grades.remove(minimumGrade)
average=sum(grades)/len(grades)
print("Average Grade: {:.2f}".format(average))
