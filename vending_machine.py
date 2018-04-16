#PYTHON vending machine test
import sys

mmain = 1
msnacks = 2
mdrinks = 3
mdrinksprice = 4
mthankyou = 10
mcurrent = mmain
currentPrice = 1.5

def menumain():
    print "----- Welcome to Python Vending Machine -----"
    print "---------------------------------------------"
    print "-- BUY A DRINK: -------------------------1---"
    print "-- BUY A SNACK: -------------------------2---"
    print "-- EXIT: --------------------------------3---"
    print "---------------------------------------------"
    print "---------------------------------------------"
    return

def menudrinks():
    print "---------------- Drinks ---------------------"
    print "---------------------------------------------"
    print "-- ICED TEA: ----------------------------1---"
    print "-- COKE: --------------------------------2---"
    print "-- EXIT: --------------------------------3---"
    print "---------------------------------------------"
    print "---------------------------------------------"
    return

def menusnacks():
    print "---------------- Snacks ---------------------"
    print "---------------------------------------------"
    print "-- SANDWICH: ----------------------------1---"
    print "-- CAKE: --------------------------------2---"
    print "-- EXIT: --------------------------------3---"
    print "---------------------------------------------"
    print "---------------------------------------------"
    return

def menudrinkprice(price):
    print "---------------- Drinks ---------------------"
    print "---------------------------------------------"
    print "-- PRICE:    -----------------------"+str(price)+"eur--"
    print "-----------------------------------------2---"
    print "-- EXIT: --------------------------------3---"
    print "---------------------------------------------"
    print "---------------------------------------------"
    return

def menuthankyou():
    print "---------------- THANK YOU ------------------"
    print "--------------------*------------------------"
    print "--------------------*------------------------"
    print "--------------------*------------------------"
    print "--------------------*------------------------"
    print "--------------------*------------------------"
    print "---------------- THANK YOU ------------------"
    return

def showMenu(mcurrent):
    if mcurrent == mmain:
        menumain()
    if mcurrent == msnacks:
        menusnacks()
    if mcurrent == mdrinks:
        menudrinks()  
    if mcurrent == mdrinksprice:
        menudrinkprice(currentPrice)
    if mcurrent == mthankyou:
        menuthankyou()     

while (mcurrent == mmain):
    showMenu(mmain)
    option = raw_input("Enter an option: ")
    if option == '1' :
        mprevious = mcurrent
        mcurrent = mdrinks
    if option == '2':
        mprevious = mcurrent
        mcurrent = msnacks
    if option == '3':
        print "Thank you for buying with us..."
        sys.exit()

while (mcurrent == mdrinks):
    showMenu(mdrinks)
    option = raw_input("Enter an option: ")
    if option == '1':
        mcurrent = mdrinksprice
        currentPrice = 1.50
    if option == '3':
        print "Thank you for buying with us..."
        sys.exit()

while(mcurrent == mdrinksprice):
    difference = currentPrice
    while (difference > 0) :
        currentPrice = difference
        showMenu(mdrinksprice)
        option = raw_input("Insert coin: ")
        difference = currentPrice - float(option)
    else:
        mcurrent = mthankyou

while(mcurrent == mthankyou):
    showMenu(mthankyou)
    sys.exit()

while (mcurrent == msnacks):
    showMenu(msnacks)
    option = raw_input("Enter an option: ")
    if option == '3':
        print "Thank you for buying with us..."
        sys.exit()

