import pandas as pd

paybrackets = pd.read_excel('Salarisschalen.xlsx', sheet_name='Tabel 2', index_col= 'periodiek')
paybrackets = eval(paybrackets.to_json(orient = "index").replace('"', '').replace('null', 'None'))


class person:
    def __init__(self,name,id, years_of_experience):
        self.name = name
        self.id = id
        self.years_of_experience = years_of_experience

class company:
    def __init__(self,name,id,owner):
        self.name = name
        self.id = id
        self.owner = owner
        self.finances = finances()
        self.human_resources = human_resources()

    def create_job(self, name, paybracket):
        n = len(self.human_resources.staff.keys())+1
        self.human_resources.staff[name] = [job(name, n, self, paybracket),{}]

    def hire_employee(self, person, functionname, parttimepercentage):
        employeeobject = employee(person,self,self.human_resources.staff[functionname][0],parttimepercentage)
        self.human_resources.staff[functionname][1][employeeobject.person.id] =employeeobject
        self.finances.expenses['personel_expenses'] += employeeobject.monthly_salary

    def fire_employee(self,functionname, personid):
        self.finances.expenses['personel_expenses'] -= self.human_resources.staff[functionname][1][personid].monthly_salary  
        del self.human_resources.staff[functionname][1][personid]    

class finances:
    def __init__(self):
        self.income = {'sales': 0}
        self.expenses = {'cogs' : 0 , 'personel_expenses' : 0}

    def get_net_earnings(self):
        return sum(self.income.values()) - sum(self.expenses.values())
    
class human_resources:
    def __init__(self):
        self.staff = {} 
        self.staffnumber = 0    
        
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

if __name__ == '__main__':
    Meander = company('Meander', 1, 'N/A')
    Meander.create_job('bi',60)
    Remco = person("remco", 1,1)
    Meander.hire_employee(Remco,'bi',100)

    print(Meander.finances.get_net_earnings())