class Hero:
    #  class variable
    jumlahHero = 0
    heroNames = []
    def __init__(self, inputName, inputHealth, inputPower, inputArmor) :
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
    # method can't return / void method
    def siapa(self):
        print("my name is : ", self.name)
     
    # method dengan argument tanpa return
    def healthUp(self, up):
        self.armor += up
        
    # method dengan return 
    def getHealth (self):
        return self.health
        
hero1 = Hero("sniper", 100, 200, 300)

print("How many yor health? \n", hero1.getHealth())