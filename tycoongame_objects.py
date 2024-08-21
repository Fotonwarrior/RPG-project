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
        self.staff = {} 
        self.staffnumber = 0
        self.finances = finances()
    def create_job(self,name, paybracket):
        n = len(self.staff.keys())+1
        self.staff[name] = [job(name, n, self, paybracket),{}]
    def hire_employee(self, person, functionname, parttimepercentage):
        employeeobject = employee(person,self,self.staff[functionname][0],parttimepercentage)
        self.staff[functionname][1][employeeobject.person.id] =employeeobject
        self.finances.expenses['personel_expenses'] += employeeobject.monthly_salary
    def fire_employee(self,functionname, personid):
        self.finances.expenses['personel_expenses'] -= self.staff[functionname][1][personid].monthly_salary  
        del self.staff[functionname][1][personid]    

class finances:
    def __init__(self):
        self.income = {'sales': 0}
        self.expenses = {'cogs' : 0 , 'personel_expenses' : 0}
    def get_net_earnings(self):
        return sum(self.income.values()) - sum(self.expenses.values())

        
class employee:
     def __init__(self,person,company,function,partimepercentage):
        self.person = person
        self.company = company
        self.function = function
        self.partimepercentage = partimepercentage
        self.monthly_salary = paybrackets[person.years_of_experience][function.paybracket] *self.partimepercentage/100

class job:  
     def __init__(self,name,id,company,paybracket):
        self.name = name
        self.id = id
        self.company = company
        self.paybracket = paybracket

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





Meander = company('Meander', 1, "healthcare", 'N/A')
Meander.create_job('bi',65)
Remco = person("remco", 1,1)
Meander.hire_employee(Remco,'bi',100)

print(Meander.finances.get_net_earnings())