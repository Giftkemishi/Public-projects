
print()
print("SO YOU WANT TO DATE WITH ME?")
print()

a ='isizulu'
b = 'tsonga'
c = 'venda'
d = 'pedi'
e = 'swati'
f = 'english'
g = 'afrikaans'
h = 'sotho'
i = 'khelobedu'
j = 'other languages'

tounge = ["Isizulu", "Tsonga", "Venda", "Pedi", "Swati", "English", "Afrikaans", "Sotho", "Khelobedu", "Other Languages"]
for letter, tounge in enumerate(tounge, start=1):
    print(f"number {letter}: {tounge}")
    
print()
    
while True:
    choose_tounge = int(input("Choose the number of your mother tounge: "))
    if choose_tounge > 9:
        print("no language found, number should be from 0 to 9!")
        continue
    elif choose_tounge >= 1:
        print(f"{tounge}")
        break
    else:
        print("no language found, number should be from 0 to 9!")
        
print()

name = input("1. enter your name: ")
print()
print("enter date of birth below...")
day  = int(input("2. enter DAY of birth: "))
month = str(input("3. enter MONTH of birth: "))
year = int(input("4. enter YEAR of birth: "))
print()
print(f"{name} born in {day}/{month}/{year}")

print()
while True:    
    kids = input("5. Do you want kids? yes or no? ")
    
    if kids == 'yes':
        how_many = int(input("6. how many? "))
        print()
        break
    elif kids == 'no':
        print("continue...")
        break
    else:
        print("The answer should be yes or no!")

print()
while True:
    pets = input("7. Do you have any pets? yes or no? ")
    if pets == 'no':
        print("answer the following question...")
        break
    elif pets == 'yes':
        print("Answer the following question with YES since you already have a pet. unless you won't need a pet.")
        break
    else:
        print("the answer should be yes or no!")
        
print()
while True:
    future = input("8. Would you want pets in the future? yes or no? ")
    if future == 'no':
        print()
        break
    elif future == 'yes':
        print()
        break
    else:
        print("The answer should be yes or no!")
  
print()
while True:      
    health = input("9. Is there a history of balding or any health related concern in your family? yes or no? ")
    if health == 'yes':
        print()
        break
    elif health == 'no':
        print()
        break
    else:
        print("the answer should be yes or no!")

print()
church = ["couldn't care less", "Atheist", "Zodiac Sign Believer", "Cristian", "Muslim", "Drunkard"]
for number, church in enumerate(church, start=1):
    print(f"number {number}: {church}")
    
print()
    
while True:
    choose = int(input("10. choose the number of your church: "))
    if choose > 5:
        print("no church found, number should be from 0 to 4!")
        continue
    elif choose >= 0:
        print()
        break
    else:
        print("no church found, number should be from 0 to 4!")
        
print()
while True:
    snore = input("11. Do you snore? yes or no? ")
    if snore == 'yes':
        print("We gonna have a hard sleep.")
        break
    elif snore == 'no':
        print()
        break
    else:
        print("The answer shoul be yes or no!")
        
print()
cloud = input('12. How would you respond if i say "ohh cloud looks like a croissant"? ')
print()

stress = input("13. How do you handle stress? ")
print()

love_language = input("14. what is your LOVE language: ")
print()

while True:
    ex = input("15. can we contact your exes as reference? yes or no? ")
    if ex == 'yes':
        ex_name = input("enter your Ex's name: ")
        def length(ex_number):
            ex_number = int(input("start the number with +27, enter your Ex's phone number: "))        
            return len(str(abs(ex_number)))        
        print
        while True:                
            if (length ('ex_number')) != 11:
                print("invalid cell phone number!")
                continue
            else:
                print()
                break                
        break
    elif ex == 'no':
        why = input("why...? ")
        break
    else:
        print("The answer should be yes or no!")

print()

def check_paragraph(paragraph):
    while True:
        paragraph = input("Write a paragraph of 50 words why you want to date me: ")
        if len(paragraph) >= 70:
            print("THANK YOU!")
            break
        else:
            print("the paragraph did not exceed 50 words .")

print()

from datetime import date
C_day = date.today()
print(f"Today is {C_day}") 

from datetime import date
current_year = date.today().year
print()

age = (current_year - year)

print(f"we have calculated your age and you are {age} old.")
print()

print(f"I {name} born in {day} {month} {year} while i am {age} years old. I promise I answered truthfully to all the questions.")

print()

print("PLEASE USE YOUR SURNAME AS SIGNATURE!!! AND DATE WILL BE AUTOMETICALLY FILLED.")

signature = input("please sign here: ")
print()

date = print(f" fill Date: {C_day}") 












    
    
    
    
    
    
    
    
    
    
    
