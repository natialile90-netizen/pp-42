text = input ("Please enter the text : ")

for character in text :
    if character.isdigit () :
        continue 
    print (character, end="")