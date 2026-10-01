try:
    price= float ( input ( "Enter price : " ))
    quantity = int ( input ("Enter quantity : "))

    total = price * quantity


except ValueError :
    print ("Error: Both price and quantity must be valid numbers! ")

else:
    print (f"Total price: ${total :.2f}")