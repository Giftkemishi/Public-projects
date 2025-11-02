import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def log_in():
    win2 = tk.Toplevel()
    win2.title("Log In")
    win2.geometry("700x700")
    label = tk.Label(win2, text = "Log In", font = ("Calibri", 22, "bold"))
    label.pack()

    email = tk.Label(win2, text = "Enter Email")
    email.pack(pady = 5)
    entryEmail = tk.Entry(win2, width = "80")
    entryEmail.pack()

    password = tk.Label(win2, text = "Enter Password")
    password.pack(pady = 5)
    entryPassword = tk.Entry(win2, width = "80")
    entryPassword.pack()

    entryEmail.delete(0, tk.END)
    entryPassword.delete(0, tk.END)

    BtnF1 = tk.Frame(win2)
    BtnF1.pack()

    logIn = tk.Button(BtnF1, text = "Log in", width = "15", height = "2", command=index)
    logIn.pack(side=tk.LEFT, padx=5, pady = 40)

    signIn = tk.Button(BtnF1, text = "Sign in", width = "15", height = "2", command=sign_in)
    signIn.pack(side=tk.LEFT, padx=5, pady = 40)
    
   # messagebox.showinfo("Warning", "The management won't take any blame of ingredients you put in your food")

    win2.mainloop()


def sign_in():
    win3 = tk.Toplevel()
    win3.title("Sign In")
    win3.geometry("700x700")

    SFrame = tk.Frame(win3)
    SFrame.pack(pady ='70' )

    label = tk.Label(SFrame, text = "Sign In", font = ("Calibri", 26, "bold"))
    label.pack()

    Fname = tk.Label(SFrame, text = "First Name", font = ("calibri",13))
    Fname.pack(pady = 5, padx = 50)
    entryFname = tk.Entry(SFrame, width = "80")
    entryFname.pack()

    Sname = tk.Label(SFrame, text = "Second Name:", font = ("calibri",13))
    Sname.pack(pady = 5)
    entrySname = tk.Entry(SFrame, width = "80")
    entrySname.pack()

    Num = tk.Label(SFrame, text = "Enter Number", font = ("calibri",13))
    Num.pack(pady = 5)
    entryNum = tk.Entry(SFrame, width = "80")
    entryNum.pack()

    Email = tk.Label(SFrame, text = "Enter email", font = ("calibri",13))
    Email.pack(pady = 5)
    entryEmail = tk.Entry(SFrame, width = "80")
    entryEmail.pack()

    password = tk.Label(SFrame, text = "Enter password", font = ("calibri",13))
    password.pack(pady = 5)
    entrypassword = tk.Entry(SFrame, width = "80")
    entrypassword.pack()

    Cpassword = tk.Label(SFrame, text = "Confirm Password", font = ("calibri",13))
    Cpassword.pack(pady = 5)
    entryCpassword = tk.Entry(SFrame, width = "80")
    entryCpassword.pack()

    entryFname.delete(0, tk.END)
    entrySname.delete(0, tk.END)
    entryNum.delete(0, tk.END)
    entryEmail.delete(0, tk.END)
    entrypassword.delete(0, tk.END)
    entryCpassword.delete(0, tk.END)

    def Btnclick():

        mssg = tk.Label(win3, text = "Welcome! \n Signing in complete. \n Go back to log in page to log in and continue ordering your food.", font = ("Helvetica", 14,))
        mssg.pack(pady = 7)

        logIn = tk.Button(win3, text = "Log in", width = "15", height = "2", command=log_in)
        logIn.pack(pady = 10)

        signIn.configure(text = "Signed In", bg = "darkgrey")

    signIn = tk.Button(win3, text = "Sign in", width = "15", height = "2", command=Btnclick)
    signIn.pack(pady = 20)

    win3.mainloop()


def index():
    win4 = tk.Toplevel()
    win4.title("Home")
    win4.geometry("700x700")

    prep = tk.Label(win4, text = "Prepare your own Dream Meal", font = ("times new roman", 28, "bold"))
    prep.pack(pady = 50)

    menuBtnFrame = tk.Frame(win4)
    menuBtnFrame.pack(pady = 60)

    pizzaBtn = tk.Button(menuBtnFrame, text = "Pizza", width = "15", height = "2", command=pizza)
    pizzaBtn.pack(side=tk.LEFT, padx=15)

    burgerBtn = tk.Button(menuBtnFrame, text = "burger", width = "15", height = "2", command=burger)
    burgerBtn.pack(side=tk.LEFT, padx=15)

    chickBtn = tk.Button(menuBtnFrame, text = "chicken", width = "15", height = "2", command=chicken)
    chickBtn.pack(side=tk.LEFT, padx=15)

    win4.mainloop()


def pizza():
    win5 = tk.Toplevel()
    win5.title("Pizza Menu")
    win5.geometry("700x700")

    head = tk.Label(win5, text = "Pizza", font = ("times new roman", 30, "italic"))
    head.pack(pady=10)

    firstrow = tk.Frame(win5)
    firstrow.pack(pady = 20)

    secrow = tk.Frame(win5)
    secrow.pack(pady = 10)

    thirdrow = tk.Frame(win5)
    thirdrow.pack(pady = 5)

    def paperoni():
        quantity = int(ing.get())
        price = quantity * 7
        paper_label.config(text=f"Paperoni \n R{price}")
            
    paper_label = tk.Label(firstrow, text="Paperoni \n R7", font = ("Arial", 13))
    paper_label.pack(side=tk.LEFT, padx=10)
    ing = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=paperoni)
    ing.pack(side=tk.LEFT, padx=1)

    def cheese():
        quantity = int(ing1.get())
        price = quantity * 5
        cheese_label.config(text=f"Cheese \n R{price}")
            
    cheese_label = tk.Label(firstrow, text="Cheese \n R5", font = ("Arial", 13))
    cheese_label.pack(side=tk.LEFT, padx=10)
    ing1 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=cheese)
    ing1.pack(side=tk.LEFT, padx=1)

    def mushroom():
        quantity = int(ing2.get())
        price = quantity * 4
        mush_label.config(text=f"Mushroom \n R{price}")
            
    mush_label = tk.Label(firstrow, text="Mushroom \n R4", font = ("Arial", 13))
    mush_label.pack(side=tk.LEFT, padx=10)
    ing2 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=mushroom)
    ing2.pack(side=tk.LEFT, padx=10)

    def Tpaste():
        quantity = int(ing3.get())
        price = quantity * 3
        tompaste_label.config(text=f"Tomato \n Paste \n R{price}")
            
    tompaste_label = tk.Label(firstrow, text="Tomato \n Paste \n R3", font = ("Arial", 13))
    tompaste_label.pack(side=tk.LEFT, padx=10)
    ing3 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=Tpaste)
    ing3.pack(side=tk.LEFT, padx=10)

    def mayo():
        quantity = int(ing4.get())
        price = quantity * 3
        mayo_label.config(text=f"Mayo \n R{price}")
            
    mayo_label = tk.Label(firstrow, text="Mayo \n R3", font = ("Arial", 13))
    mayo_label.pack(side=tk.LEFT, padx=10)
    ing4 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=mayo)
    ing4.pack(side=tk.LEFT, padx=10)

    def chicken():
        quantity = int(ing5.get())
        price = quantity * 12
        Chicken_label.config(text=f"Chicken \n R{price}")
            

    Chicken_label = tk.Label(secrow, text="Chicken \n R12", font = ("Arial", 13))
    Chicken_label.pack(side=tk.LEFT, padx=10)
    ing5 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=chicken)
    ing5.pack(side=tk.LEFT, padx=10)

    def Beef():
        quantity = int(ing6.get())
        price = quantity * 15
        Beef_label.config(text=f"Beef \n R{price}")
            
    Beef_label = tk.Label(secrow, text="Beef \n R15", font = ("Arial", 13))
    Beef_label.pack(side=tk.LEFT, padx=10)
    ing6 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Beef)
    ing6.pack(side=tk.LEFT, padx=10)

    def Chilli_pepper():
        quantity = int(ing7.get())
        price = quantity * 5
        Chilli_pepper_label.config(text=f"Chilli pepper \n R{price}")
            
    Chilli_pepper_label = tk.Label(secrow, text="Chilli pepper \n R5", font = ("Arial", 13))
    Chilli_pepper_label.pack(side=tk.LEFT, padx=10)
    ing7 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Chilli_pepper)
    ing7.pack(side=tk.LEFT, padx=10)

    def Pineapple():
        quantity = int(ing8.get())
        price = quantity * 6
        Pineapple_label.config(text=f"Pineapple \n R{price}")
            
    Pineapple_label = tk.Label(secrow, text="Pineapple \n R6", font = ("Arial", 13))
    Pineapple_label.pack(side=tk.LEFT, padx=10)
    ing8 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Pineapple)
    ing8.pack(side=tk.LEFT, padx=10)

    def Ran_swee_sauce():
        quantity = int(ing9.get())
        price = quantity * 3
        Ran_swee_sauce_label.config(text=f"sweet sauce \n R{price}")
            
    Ran_swee_sauce_label = tk.Label(secrow, text="sweet sauce \n R3", font = ("Arial", 13))
    Ran_swee_sauce_label.pack(side=tk.LEFT, padx=10)
    ing9 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Ran_swee_sauce)
    ing9.pack(side=tk.LEFT, padx=10)

    def Otaste():
        quantity = int(ing10.get())
        price = quantity * 3
        Otaste_label.config(text=f"Original \n Taste \n R{price}")
            
    Otaste_label = tk.Label(thirdrow, text="Original \n Taste \n R3", font = ("Arial", 13))
    Otaste_label.pack(side=tk.LEFT, padx=10)
    ing10 = tk.Spinbox(thirdrow, from_=0, to=10, width=4, command=Otaste)
    ing10.pack(side=tk.LEFT, padx=10)

    def pork():
        quantity = int(ing11.get())
        price = quantity * 8
        pork_label.config(text=f"Pork \n R{price}")
            
    pork_label = tk.Label(thirdrow, text="Pork \n R8", font = ("Arial", 13))
    pork_label.pack(side=tk.LEFT, padx=10)
    ing11 = tk.Spinbox(thirdrow, from_=0, to=10, width=4, command=pork)
    ing11.pack(side=tk.LEFT, padx=10) 


    exitBtnFrame = tk.Frame(win5)
    exitBtnFrame.pack(pady = 40)

    exitBtn = tk.Button(exitBtnFrame, text = "Cancel", width = "15", height = "2", bg = "red", command=index)
    exitBtn.pack(side=tk.LEFT, padx=10)

    procBtn = tk.Button(exitBtnFrame, text = "Proceed", width = "15", height = "2", bg = "green", command=location)
    procBtn.pack(side=tk.LEFT, padx=10)

    win5.mainloop()

def burger():
    win6 = tk.Toplevel()
    win6.title("Burger Menu")
    win6.geometry("700x700")

    Bhead = tk.Label(win6, text = "Burger", font = ("times new roman", 30, "italic"))
    Bhead.pack(pady=10)

    firstrow = tk.Frame(win6)
    firstrow.pack(pady = 20)

    secrow = tk.Frame(win6)
    secrow.pack(pady = 2)

    thirdrow = tk.Frame(win6)
    thirdrow.pack(pady = 2)

    def Cpatty():
        quantity = int(ing.get())
        price = quantity * 20
        Cpatty_label.config(text=f"Chicken \n Patty \n R{price}")
            
    Cpatty_label = tk.Label(firstrow, text="Chicken \n Patty \n R20", font = ("Arial", 13))
    Cpatty_label.pack(side=tk.LEFT, padx=10)
    ing = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=Cpatty)
    ing.pack(side=tk.LEFT, padx=10)

    def egg():
        quantity = int(ing1.get())
        price = quantity * 5
        egg_label.config(text=f"Egg \n R{price}")
            
    egg_label = tk.Label(firstrow, text="Egg \n R5", font = ("Arial", 13))
    egg_label.pack(side=tk.LEFT, padx=10)
    ing1 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=egg)
    ing1.pack(side=tk.LEFT, padx=10)

    def Bpatty():
        quantity = int(ing2.get())
        price = quantity * 25
        Bpatty_label.config(text=f"Beef \n Patty \n R{price}")
            
    Bpatty_label = tk.Label(firstrow, text="Beef \n Patty \n R25", font = ("Arial", 13))
    Bpatty_label.pack(side=tk.LEFT, padx=10)
    ing2 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=Bpatty)
    ing2.pack(side=tk.LEFT, padx=10)

    def lettuce():
        quantity = int(ing3.get())
        price = quantity * 3
        lettuce_label.config(text=f"Lettuce \n R{price}")
            
    lettuce_label = tk.Label(firstrow, text="Lettuce \n R3", font = ("Arial", 13))
    lettuce_label.pack(side=tk.LEFT, padx=10)
    ing3 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=lettuce)
    ing3.pack(side=tk.LEFT, padx=10)

    def tomato():
        quantity = int(ing4.get())
        price = quantity * 2
        tomato_label.config(text=f"Tomato \n R{price}")
            
    tomato_label = tk.Label(firstrow, text="Tomato \n R2", font = ("Arial", 13))
    tomato_label.pack(side=tk.LEFT, padx=10)
    ing4 = tk.Spinbox(firstrow, from_=0, to=10, width=4, command=tomato)
    ing4.pack(side=tk.LEFT, padx=10)

    def Cucumber():
        quantity = int(ing5.get())
        price = quantity * 5
        Cucumber_label.config(text=f"Cucumber \n R{price}")
            

    Cucumber_label = tk.Label(secrow, text="Cucumber \n R5", font = ("Arial", 13))
    Cucumber_label.pack(side=tk.LEFT, padx=10)
    ing5 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Cucumber)
    ing5.pack(side=tk.LEFT, padx=10)

    def BSauce():
        quantity = int(ing6.get())
        price = quantity * 5
        BSauce_label.config(text=f"Burger \n Sauce \n R{price}")
            
    BSauce_label = tk.Label(secrow, text="Burger \n Sauce \n R5", font = ("Arial", 13))
    BSauce_label.pack(side=tk.LEFT, padx=10)
    ing6 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=BSauce)
    ing6.pack(side=tk.LEFT, padx=10)

    def Chilli_pepper():
        quantity = int(ing7.get())
        price = quantity * 5
        Chilli_pepper_label.config(text=f"Chilli pepper \n R{price}")
            
    Chilli_pepper_label = tk.Label(secrow, text="Chilli pepper \n R5", font = ("Arial", 13))
    Chilli_pepper_label.pack(side=tk.LEFT, padx=10)
    ing7 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Chilli_pepper)
    ing7.pack(side=tk.LEFT, padx=10)

    def Pineapple():
        quantity = int(ing8.get())
        price = quantity * 6
        Pineapple_label.config(text=f"Pineapple \n R{price}")
            
    Pineapple_label = tk.Label(secrow, text="Pineapple \n R6", font = ("Arial", 13))
    Pineapple_label.pack(side=tk.LEFT, padx=10)
    ing8 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Pineapple)
    ing8.pack(side=tk.LEFT, padx=10)

    def Hot_sauce():
        quantity = int(ing9.get())
        price = quantity * 3
        hot_sauce_label.config(text=f"Hot \n Sauce \n R{price}")
            
    hot_sauce_label = tk.Label(secrow, text="Hot \n Sauce \n R3", font = ("Arial", 13))
    hot_sauce_label.pack(side=tk.LEFT, padx=10)
    ing9 = tk.Spinbox(secrow, from_=0, to=10, width=4, command=Hot_sauce)
    ing9.pack(side=tk.LEFT, padx=10)

    def sweet_sauce():
        quantity = int(ing10.get())
        price = quantity * 3
        sweetSauce_label.config(text=f"sweet sauce \n R{price}")
            
    sweetSauce_label = tk.Label(thirdrow, text="sweet sauce \n R3", font = ("Arial", 13))
    sweetSauce_label.pack(side=tk.LEFT, padx=10)
    ing10 = tk.Spinbox(thirdrow, from_=0, to=10, width=4, command=sweet_sauce)
    ing10.pack(side=tk.LEFT, padx=10)

    def Otaste():
        quantity = int(ing11.get())
        price = quantity * 3
        Otaste_label.config(text=f"Original \n Taste \n R{price}")
            
    Otaste_label = tk.Label(thirdrow, text="Original \n Taste \n R3", font = ("Arial", 13))
    Otaste_label.pack(side=tk.LEFT, padx=10)
    ing11 = tk.Spinbox(thirdrow, from_=0, to=10, width=4, command=Otaste)
    ing11.pack(side=tk.LEFT, padx=10)

    def mayo():
        quantity = int(ing12.get())
        price = quantity * 3
        mayo_label.config(text=f"Mayo \n R{price}")
            
    mayo_label = tk.Label(thirdrow, text="Mayo \n R3", font = ("Arial", 13))
    mayo_label.pack(side=tk.LEFT, padx=10)
    ing12 = tk.Spinbox(thirdrow, from_=0, to=10, width=4, command=mayo)
    ing12.pack(side=tk.LEFT, padx=10)   

    def bacon():
        quantity = int(ing13.get())
        price = quantity * 7
        bacon_label.config(text=f"Bacon \n R{price}")
            
    bacon_label = tk.Label(thirdrow, text="Bacon \n R7", font = ("Arial", 13))
    bacon_label.pack(side=tk.LEFT, padx=10)
    ing13 = tk.Spinbox(thirdrow, from_=0, to=10, width=4, command=bacon)
    ing13.pack(side=tk.LEFT, padx=10) 

    exit2BtnFrame = tk.Frame(win6)
    exit2BtnFrame.pack(pady = 40)

    canBtn = tk.Button(exit2BtnFrame, text = "Cancel", width = "15", height = "2", bg = "red", command=index)
    canBtn.pack(side=tk.LEFT, padx=10)

    conBtn = tk.Button(exit2BtnFrame, text = "Proceed", width = "15", height = "2", bg = "green", command=location)
    conBtn.pack(side=tk.LEFT, padx=10)

    win6.mainloop()

def chicken():
    win7 = tk.Toplevel()
    win7.title("Chicken Menu")
    win7.geometry("700x700")

    def chickPrice():
        quantity = int(menu.get())
        price = quantity * 35
        chick_label.config(text=f"Grilled Chicken \n R{price}")
            
    chick_label = tk.Label(win7, text="Grilled Chicken \n R35", font = ("Arial", 13))
    chick_label.pack()
    menu = tk.Spinbox(win7, from_=1, to=10, width=10, command=chickPrice)
    menu.pack()

    exit3BtnFrame = tk.Frame(win7)
    exit3BtnFrame.pack(pady = 40)

    cancelBtn = tk.Button(exit3BtnFrame, text = "Cancel", width = "15", height = "2",bg = "red", command=index)
    cancelBtn.pack(side=tk.LEFT, padx=10)

    contBtn = tk.Button(exit3BtnFrame, text = "Proceed", width = "15", height = "2", bg = "green", command=location)
    contBtn.pack(side=tk.LEFT, padx=10)
    
    win7.mainloop()

def location():
    win8 = tk.Toplevel()
    win8.title("Address")
    win8.geometry("700x700") 

    locationFrame = tk.Frame(win8)
    locationFrame.pack(pady = "50")

    AbtnFrame = tk.Frame(win8)
    AbtnFrame.pack(pady = "10")

    address = tk.Label(locationFrame, text = "Address", font = ("Arial", 28, "bold"))
    address.pack(pady = "10")

    house = tk.Label(locationFrame, text = "House number", font = ("calibri",13))
    house.pack()
    Ehouse = tk.Entry(locationFrame, width = "80")
    Ehouse.pack()

    town = tk.Label(locationFrame, text = "town, city", font = ("calibri",13))
    town.pack()
    Etown = tk.Entry(locationFrame, width="80")
    Etown.pack()

    zip = tk.Label(locationFrame, text = "Zip Code", font = ("calibri",13))
    zip.pack()
    Ezip = tk.Entry(locationFrame, width = "80")
    Ezip.pack()

    Bbtn = tk.Button(AbtnFrame, text = "Back", bg = "red", width = "15", height = "2", command=index)
    Bbtn.pack(side = tk.LEFT, padx = "10")

    Pbtn = tk.Button(AbtnFrame, text = "Proceed", bg = "green", width = "15", height = "2", command=pay)
    Pbtn.pack(side = tk.LEFT, padx = "10")

    win8.mainloop()


def pay():
    win9 = tk.Toplevel()
    win9.title("Payment")
    win9.geometry("700x700") 

    payFrame = tk.Frame(win9)
    payFrame.pack(pady = "50")

    PbtnFrame = tk.Frame(win9)
    PbtnFrame.pack(pady = "10")

    head1 = tk.Label(payFrame, text = "Enter Banking Details", font = ("Arial", 24, "bold"))
    head1.pack()

    Bname = tk.Label(payFrame, text = "Bank Name", font = ("calibri",13))
    Bname.pack()
    EBname = tk.Entry(payFrame, width = "80")
    EBname.pack()

    Cholder = tk.Label(payFrame, text = "Card Holder Name", font = ("calibri",13))
    Cholder.pack()
    ECholder = tk.Entry(payFrame, width = "80")
    ECholder.pack()

    acc = tk.Label(payFrame, text= "Account Number", font = ("calibri",13))
    acc.pack()
    Eacc = tk.Entry(payFrame, width = "80")
    Eacc.pack()

    Scode = tk.Label(payFrame, text = "Security Code", font = ("calibri",13))
    Scode.pack()
    EScode = tk.Entry(payFrame, width = "80")
    EScode.pack()

    Bbtn = tk.Button(PbtnFrame, text = "Back", bg = "red", width = "15", height = "2", command=location)
    Bbtn.pack(side = tk.LEFT, padx = "10")

    Pbtn = tk.Button(PbtnFrame, text = "Proceed", bg = "green", width = "15", height = "2", command=waiting)
    Pbtn.pack(side = tk.LEFT, padx = "10")

    win9.mainloop()

def waiting():
    win10 = tk.Toplevel()
    win10.title("Waiting Room")
    win10.geometry("700x700") 

    msg = tk.Label(win10, text = "Waiting Room", font = ("Times new roman", 30, "bold", "underline", "italic"))
    msg.pack(pady = "30")



    win10.mainloop()


root = tk.Tk()
root.title("Welcome")
root.geometry("700x700")

messagebox.showinfo("Warning", "From The Management \n The management will not take any blame of what you have put in your food. \n Enjoy")

msgFrame = tk.Frame(root)
msgFrame.pack(pady = 150)

intrancemssg = tk.Label(msgFrame, text = "Tasty Bites", font = ("palatino", 100, "bold", "italic"))
intrancemssg.pack()

intrancemssg2 = tk.Label(msgFrame, text = "Taste your Dreams", font = ("times new roman", 30, "italic", "bold"))
intrancemssg2.pack()

BtnFrame = tk.Frame(root)
BtnFrame.pack(pady = 30)

logIn = tk.Button(BtnFrame, text = "Log in", width = "15", height = "2", command=log_in)
logIn.pack(side=tk.LEFT, padx=10)

signIn = tk.Button(BtnFrame, text = "Sign in", width = "15", height = "2", command=sign_in)
signIn.pack(side=tk.LEFT, padx=10)

root.mainloop()
