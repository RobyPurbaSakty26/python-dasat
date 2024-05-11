class Herro:
    def __init__(self, inputName, inputAttack, inputHelath, inputPower) :
        self.name = inputName
        self.attack = inputAttack
        self.health = inputHelath
        self.power = inputPower
        
    def Serang (self, inputHerrorAttack):
        result = self.name + " diserang oleh " + inputHerrorAttack.name
        return result
        
budi = Herro("budi", 20, 100, 100)
ucup = Herro("ucup", 25, 200, 200)

print("Serrang =====")
print(budi.Serang(ucup))