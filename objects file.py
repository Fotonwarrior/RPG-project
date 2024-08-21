class creature:
    def __init__(self,name, physiology):
        self.name = name        
        self.physiology = physiology

class human(creature):
    def __init__(self):
        self.physiology = physiology(2,2,1)

class physiology:
    def __init__(self, arms, legs,heads):
        self.arms = initialise('arm', limb, arms)
        self.legs = initialise('leg', limb, legs)
        self.heads = initialise('head', limb, heads)
class limb:
    def __init__(self, name):
        self.name = name
        self.equiped_items = []
        self.health = 100

def initialise(name, object, number):
    output = []
    for i in range(number):
        objectname =  name+str(i)
        output.append(object(name = objectname))
        print(f'Created {objectname}')

remco = human("Remco")
print(remco.name)
print(remco.physiology)