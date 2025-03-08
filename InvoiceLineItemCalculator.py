
"""
Student Name: N'din Assi 
COURSE: CIS 261 Object Oriented Computer Programming 1 
title: Invoice Line Item Calculator 


"""
def main():
    header()
    response="start"
    while response !="n":
        response= input("Enter another line item? (y,n): ").lower()
        if response=="y":
            myprice= price()
            myquantity= quantity()
            print(f"PRICE:  {myprice}")
            print(f"QUANTITY: {myquantity}")
            total = myprice*myquantity
            print(f"TOTAL:  {total}")
        elif response=="n":
            print("Bye!!")
            break 
        else:
            print("Command Not Found try again ")
        
    

def header():
    print("The Invoice Line Item Calculator \n Develpoed by N'din Assi ")
    
def price():
    check=False
    while check ==False :
        try:
            my_price= float(input(" Enter price: "))
            check=True
        
        
        except:
            print("Invalid decimal number please try again.")
        #my_price=float(input("Enter price: "))
    return my_price
def quantity():
    check=False
    while check ==False :
        try:
            my_quantity= int(input(" Enter quantity: "))
            check=True
        
        
        except:
            print("Invalid decimal number please try again.")
        #my_price=float(input("Enter price: "))
    return my_quantity

if __name__=="__main__":
    main()