try:
    password = input ("enter  your password:")

    if len (password) < 6:
        raise ValueError ("password is too short! ")
    print ("password is valid! ")

except ValueError as e :
    print (e)