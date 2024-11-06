
class building:
     def __init__(self,id,address,type):
        self.id = id
        self.address = address 
        self.type = type  

class location:
     def __init__(self,building,company):
        self.building = building
        self.company = company   

class production_unit:
     def __init__(self,id,location,type,):
        self.id = id
        self.location = location 
        self.type = type   

class comodity:
     def __init__(self,type,required_job, required_production_unit, going_rate):
        self.type = type
        self.required_job = required_job
        self.required_production_unit = required_production_unit
        self.going_rate = going_rate
        
class customer:
    def __init__(self,person,company):
        self.person = person
        self.company = company

    def wants_comodity(self,comodity):
        self.wanted_comodity = comodity
