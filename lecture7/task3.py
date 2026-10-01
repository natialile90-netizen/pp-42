fruits = [ "apple", "banana", "cherry", "orange"]

try:
    index = int(input ( "Enter fruit index: "))
    fruit = fruits [index]

except ValueError:
    print ("Error: please enter a valid number!")

except IndexError:
    print ("Error : index is out of range!")

else:
    print (f"selected fruit : {fruit}")