class Hero:
    def __init__(self, inputName, inputPower, inputHealth) :
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower


# buat obkect Hero
hero1 = Hero("Eko", 500, 100) 


print("Name Hero\t: ", hero1.name)
print("Health\t\t: ",hero1.health)
print("Power\t\t: ",hero1.power)