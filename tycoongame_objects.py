import pandas as pd

paybrackets = pd.read_excel('Salarisschalen.xlsx', sheet_name='Tabel 2', index_col= 'periodiek')
paybrackets = eval(paybrackets.to_json(orient = "index").replace('"', '').replace('null', 'None'))


class person:
    def __init__(self,name,id, years_of_experience):
        self.name = name
        self.id = id
        self.years_of_experience = years_of_experience

class company:
    def __init__(self,name,id,type,owner):
        self.name = name
        self.id = id
        self.type = type
        self.owner = owner
        
class employee:
     def __init__(self,person,company,function,partimepercentage):
        self.person = person
        self.company = company
        self.function = function
        self.partimepercentage = partimepercentage
        self.monthly_salary = paybrackets[person.years_of_experience][function.paybracket] *self.partimepercentage/100

class jobdescription:  
     def __init__(self,name,id,company,paybracket):
        self.name = name
        self.id = id
        self.company = company
        self.paybracket = paybracket

class building:
     def __init__(self,id,address,type,):
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





Meander = company('Meander', 1, "healthcare", 'N/A')
bi = jobdescription('bi_developer', 1, Meander, 60)
Remco = employee(person("remco", 1,1),Meander,bi,100)

print(Remco.monthly_salary)