cart_total = float (input ("Enter cart total : $"))

is_vip = input ("Are you a VIP member? (yes or no):") .strip()  .lower() == "yes"


if cart_total >= 50 or is_vip:
    print ("Free shipping")
else :
    print ("You have to pay for shipping")



is_guest = input ("Are you a guest? (yes or no) :") .strip()  .lower() == "yes"
valid_promo_code ="SAVE10"
promo_code = input ("Enter promo code (or leave empty):") .upper () .strip()

if promo_code and promo_code == valid_promo_code and not is_guest:
    final_total = cart_total * 0.90
    print ("10% discount applied")
else:
    final_total = cart_total
    print ("No discount applied")

print (f"Final total: $ {final_total}")