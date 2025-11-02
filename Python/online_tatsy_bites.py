pbacon = 15 
plettuce = 5 
pcucumber = 5 
pchicken_patty = 20 
pegg = 3 
pcheese = 5
ptomato = 5
pfries = 25 
pbeef_patty = 25 
ppepper = 6 
ppeppers = 4 
psauce = 3 
phot = 36
psweet = 22
poriginal = 10
pmild = 28
psauces = 7
pmushroom = 4
ppaperoni = 7
pany_sauce = 6  
ptomato_sauce = 2 
pchicken = 12
pbeef = 17
pdelivery = 37 
pBurgerPizza = 50
pflavor = 15
pmeat = 46

prices = {"bacon":pbacon, "chicken":pchicken, "sauces":psauces, "mild":pmild, "hot":phot, "sweet":psweet, "original":poriginal, "beef":pbeef, "paperoni":ppaperoni, "cheese":pcheese, "lettuce":plettuce, "cucumber":pcucumber, "mushroom":pmushroom, "chicken patty":pchicken_patty, "tomato":ptomato, "egg":pegg, "fries":pfries, "beef patty":pbeef_patty, "peppers":ppeppers, "pepper":ppepper, "sauce":psauce, "any sauce":pany_sauce, "tomato sauce":ptomato_sauce, "flavor":pflavor}

restuarentName = ("Tasty Bites")
print("welcome to",restuarentName)

print()
print('             prices')
print('     Bacon                R15')
print('     Lettuce              R5') 
print('     Cucumber             R5') 
print('     Chicken_patty        R20')
print('     Egg                  R3')
print('     Cheese               R5')
print('     Tomato               R5')
print('     Fries                R25')
print('     Beef patty           R22')
print('     Pepper               R6')
print('     Peppers              R4')
print('     Sauce                R3')
print('     Hot                  R36')
print('     Sweet                R22')
print('     Original             R10')
print('     Mild                 R28')
print('     Sauces               R7')
print('     Mushroom             R4')
print('     Paperoni             R7')
print('     Any_sauce            R6')
print('     Tomato_sauce         R2') 
print('     Chicken              R12')
print('     Beef                 R17')
print('     Delivery             R37')
print('     Burger or Pizza      R50')
print('     Flavor               R15')
print('     Meat                 R46')
print()


menu = ["Pizza", "Burger", "Grilled meat"]
for m in menu:
    print(" ",m)
    
likes = input("what would you like? ").lower()

if (likes) == 'grilled meat':
    
    cart3 = []
    
    meat = ["beef", "chicken", "pork"]
    for k in meat:
        print(k)
        
    meat = input("what kind of meat? ").lower()
    
    flavor = ["mild", "hot", "original", "sweet"]
    for f in flavor:
        print(f,"flavor")
    
    while True:
            
        meat = input(f"what flavor would you like your {meat}? type 'done' to finish: ").lower()
        
        if meat in flavor:
            cart3.append(meat)
        else:
            print("ingredient not found.")
            
        if meat == 'done':
            break

    print("your flavors are: ")
    for item in cart3:
        print(item)
        
    meatPrice = 0
    for e in cart3:
        meatPrice += prices[e]

    while True:
        print("Options:")
        print("1. Remove flavor")
        print("2. Finish")
        choice2 = input("Choose an option: ")
        if choice2 == '1':
            itemtoRemoved = input("Enter the flavor to remove: ").lower()
            if itemtoRemoved in cart3:
                cart3.remove(itemtoRemoved)
                print(f"{itemtoRemoved} removed.")
            else:
                print("flavor not found.")
        elif choice2 == '2':
            break
    else:
            print("Invalid option.")

    print("your meat will taste:")
    for item in cart3:
        print(item)
    
elif (likes) == 'pizza':
        
        cart1 = []
        
        ingredients = ["bacon", "cheese", "tomato sauce", "any sauce", "paperoni", "chicken", "beef", "mushroom", "peppers"]
        for i in ingredients:
            print("ingredient: ", i)

        while True:
            pizza = input("what would you like in your pizza? type 'done' to finish: ").lower()
            
            if pizza in ingredients:
                cart1.append(pizza)
            else:
                print("ingredient not found.")
            if pizza == 'done':
                break

        print("your ingredients are: ")
        for item in cart1:
            print(item)
            
        pizzaPrice = 0
        for q in cart1:
            pizzaPrice += prices[q]

        while True:
            print("Options:")
            print("1. Remove ingredient")
            print("2. Finish")
            choice = input("Choose an option: ")
            if choice == '1':
                itemRemove = input("Enter the ingredient to remove: ").lower()
                if itemRemove in cart1:
                    cart1.remove(itemRemove)
                    print(f"{itemRemove} removed.")
                else:
                    print("ingredient not found.")
            elif choice == '2':
                break
        else:
                print("Invalid option.")

        print("your pizza will have the following:")
        for item in cart1:
            print(item)
      
elif (likes) == 'burger':
    
        
        cart2 = []
        
        ingredients2 = ["bacon", "lettuce", "cucumber", "beef patty", "chicken patty", "sauces", "tomato", "egg", "fries", "pepper"]
        for n in ingredients2:
            print(f"ingredient: {n}" )


        while True:
            burger = input("what would you like in your burger? type 'done' to finish: ").lower()
            
            if burger in ingredients2:
                cart2.append(burger)
            else:
                print("ingredient not found.")
                
            if burger == 'done':
                break

        print("your ingredients are: ")
        for item in cart2:
            print(item)
            
        burgerPrice = 0
        for w in cart2:
            burgerPrice += prices[w]

        while True:
            print("Options:")
            print("1. Remove ingredient")
            print("2. Finish")
            choice1 = input("Choose an option: ")
            if choice1 == '1':
                itemRemoved = input("Enter the ingredient to remove: ").lower()
                if itemRemoved in cart2:
                    cart2.remove(itemRemoved)
                    print(f"{itemRemoved} removed.")
                else:
                    print("ingredient not found.")
            elif choice1 == '2':
                break
        else:
                print("Invalid option.")

        print("your burger will have the following:")
        for item in cart2:
            print(item)

else:
    print("your cart is empty")
    
if (likes) == 'pizza':
    totalFoodPrice = (pBurgerPizza + pizzaPrice)
    print("Amount to be paid: R",totalFoodPrice)
elif (likes) == 'grilled meat':
    totalFoodPrice = (pmeat + meatPrice)
    print("Amount to be paid: R",totalFoodPrice)
elif (likes) == 'burger':
    totalFoodPrice = (pBurgerPizza + burgerPrice)
    print("Amount to be paid: R",totalFoodPrice)
    
deliveryCollect = input("how would you like your order? delivery or collect? ").lower()

if (deliveryCollect) == 'delivery':
    print("delivery is R37")
    home = input("house or building? ").lower()
    if (home) == 'house':
        house = int(input("house number: "))
        street = input("stree name: ").lower()
        totalAmount = (pdelivery + totalFoodPrice)
        print("total Amount to pay : R",totalAmount)


    elif (home) == 'building':
        building = int(input("building number: "))
        buildName = input("building name: ").lower()
        unit = int(input("unit number: "))
        streetName = input("street name: ").lower()
        totalAmount = (pdelivery + totalFoodPrice)
        print("total Amount to pay : R",totalAmount)
    else:
        print("your order might get missing.")
    
else:
    print()
    
print ("cash or online")

pay = input("how would you like to pay? ").lower()

if (pay) == 'online':
    print("enter banking details")
    
    bank =["capitec", "nedbank", "absa", "standard bank", "FNB", "time bank"]
    
    for b in bank:
        print(b)
        
    bankName = input("enter bank name: ").lower()

    while True:
        bankName = input("enter bank name: ").lower()
        
        if bankName in bank:
            bank.append(bankName)
            break
        else:
            print("bank not found.")   
        
    holderName = input("enter card holder's name: ").lower()
    
    def length(accNo):
        accNo = int(input("enter account number: ")).lower()
        return len(str(abs(accNo)))        
    while True:                
        if (length ('accNo')) != 14:
            print("invalid account number!")
            continue
        else:
            print()
            break                
        
    def length(securityNo):    
        securityNo = int(input("enter security number: ")).lower()
        return len(str(abs(securityNo)))        
    while True:                
        if (length ('securityNo')) != 3:
            print("invalid security number!")
            continue
        else:
            print()
            break       
    
    if (deliveryCollect) == 'collect':
        print(f"{restuarentName} is preparing your order")
    elif (deliveryCollect) == 'delivery':
        print("your order will arrive in less than 59 minutes")
    else:
        print("no order placed")
        
elif (pay) == 'cash':
    if (deliveryCollect) == 'collect':
        print(f"{restuarentName} is preparing your order")
    elif (deliveryCollect) == 'delivery':
        print("your order will arrive in lesss than 59 minutes")
    else:
        print("no order placed")
        
else:
    print("no order placed")

print(f"{restuarentName} thanks you for eating with us, ENJOY!")

text = input("leave a text for our delivery guy: ").lower()







    
