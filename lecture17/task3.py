class SmartDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def get_status (self):
        return self.__is_on

class SmartLight(SmartDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)
        if brightness <0:
            self.brightness =0
        elif brightness >100:
            self.brightness = 100
        else:
            self.brightness = brightness

    def turn_on(self):
        super().turn_on()
        print (f"{self.brand} light is ON")

    def turn_off(self):
        super().turn_off()
        print (f"{self.brand} light is OFF")
    
brand = input("Enter brand: ")
brightness = int(input ("Enter brightness range 0-100: "))

light= SmartLight (brand, brightness)


print ("brand:", light.brand)
print ("brightness:" , light.brightness)


light.turn_on()
print("Satus:", light.get_status())

light.turn_off()
print("Satus:", light.get_status())