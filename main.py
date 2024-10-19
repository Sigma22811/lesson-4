print("lesson 4")

class Human:
    def __init__(self, name):
        self.Name=name

class Auto:
    def innit(self,brand):
        self.Brand=brand
        self.Humans= []
    def addHuman(self, human):
        self.Humans.append(human)
    def PrintHumans(self):
        if self.Humans != []:
            print("Names humans")
            for Human in self.Humans:
                print("\t",Human.Name)
        else:
            print("this auto is empty")

human1= Human("Zitraks Sigma")
human2= Human("Stray 228")

autoDog=Auto("Sigmoid666")

print("Brand of auto:", autoDog.Brand)

autoDog.AddHuman(human1)
autoDog.AddHuman(human2)

autoDog.Add.Human(Human("Samchuk Maxim"))

autoDog.PrintHumans()