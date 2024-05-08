class Hero:
    #  class variable
    jumlah = 0 
    names = []
    def __init__(self, inputName, inputHealt, inputPower, inputArmor) :
        # instace variable 
        # variabele yang dimiliki oleh sebuah object
        self.name = inputName
        self.health = inputHealt
        self.power = inputPower
        self.health = inputHealt
        Hero.jumlah += 1
        Hero.names.append(inputName)
        

# membuat object dari kelas
hero1 = Hero("ucup", 200, 400, 900)
print("Jumlah Hero: ", Hero.jumlah)
hero2 = Hero("Jajang", 200, 400, 900)
print("Jumlah Hero: ", Hero.jumlah)
hero3 = Hero("Dadang", 200, 400, 900)
print("Jumlah Hero: ",Hero.jumlah)

print("List name hero: ",Hero.names)