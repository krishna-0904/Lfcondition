# num=int(input("enter number:"))
# if num<0:
#     print("-ve number")
# elif num>0:
#     print("+ve number")
# else:
#     print("number is zero")

maths=int(input("enter marks for maths:"))
physics=int(input("enter marks for physics:"))
chemistry=int(input("enter marks for chemistry:"))
total_marks=600
sum_marks=maths+physics+chemistry
percentage=(sum_marks/total_marks)*100
print(percentage)
if percentage<35:
    print("Grade is F")
elif percentage>35 and percentage<=50:
    print("Grade is C")
elif percentage>50 and percentage<=90:
    print("Grade is B")
elif percentage in range(91,101):
    print("Grade is A")
else:
    print("invalid percentage")