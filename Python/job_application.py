
print("user, with this you figure out what position you qualify to work as at stark industries.")


while True:
    age = int(input("user please enter your age to continue: "))

    if int(age) >= 18:
        print("user you are eligible to continue.")
        break
    else:
        print("you are still young, only 18 years and above are allowed to use this program.")
    
print("we can't keep on calling you user.")

name = input("let us know you, please enter your name and surname: ")
print(f"well from user to {name} welcom to STARK INDUSTRY ENROLMENT PROGRAM.")

print("as we mentioned before with this program you check what you qualify for. Well let's get to business.")

print(f"{name} let's start with high school, every learner in matric did 7 subjects, we don't require any additional subjects...")

sub1 = input("enter name of first subject: ")
sub2 = input("enter name of second subject: ")
sub3 = input("enter name of third subject: ")
sub4 = input("enter name of fourth subject: ")
sub5 = input("enter name of fifth subject: ")
sub6 = input("enter name of sixth subject: ")
sub7 = input("enter name of seventh subject: ")

print("we also wanna know your grades.")

grade1 = int(input(f"enter grades for {sub1}: "))
grade2 = int(input(f"enter grades for {sub2}: "))
grade3 = int(input(f"enter grades for {sub3}: "))
grade4 = int(input(f"enter grades for {sub4}: "))
grade5 = int(input(f"enter grades for {sub5}: "))
grade6 = int(input(f"enter grades for {sub6}: "))
grade7 = int(input(f"enter grades for {sub7}: "))

print(f"{name} let's calculate your percentage...")

avarage = (grade1 + grade2 + grade3 + grade4 + grade5 + grade6 + grade7)/7
print(f"{name} you got {avarage}%")
print("as you total matric grades, let's check your qualification...")

if avarage >= 80:
    print(f"{name} you passed with Bachelor, you qualify to be designer.")
elif avarage >= 60:
    print(f"{name} you passed with Diploma, you qualify to be an engeneer.")
elif avarage >= 40:
    print(f"{name} you passed with Higher Certificate, you qualify to be a receptionist or clerk.")
else:
    print("unfortunately you have failed your matric, no position found for your grades, but don't lose hope you migh be hired as delivery guy.")
    
cell_number = int(input("please enter your cellphone number: "))
print(f"{name} we will defenately get back to you when the position is found for you.")

def check_paragraph(paragraph):
    while True:
        paragraph = input("please write a paragraph about yourself: ")
        if len(paragraph) >= 100:
            print(f"THANK YOU! {name} we will consider you.")
            break
        else:
            print("the paragraph did not exceed 100 letters.")

paragraph = ("thank you.")

check_paragraph(paragraph)

print = (f"{name} farewell we will get back to you. and right the program is still under mintanance you will not be able to continue.")
