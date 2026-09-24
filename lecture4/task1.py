age =int (input ("enter your age: "))

if age <0:
    print ("Invalid age entered.")

elif age <5:
    print ("Your ticket price is free $0.")
    
elif age <=12:
    print ("Your ticket price is $8.")

elif age <=64:
    print ("Your ticket price is $15.")

else:
    print ("Your ticket price is $10.")