# inheritance
# employee --name, id, department, gender
#salaried -- + salary, tenure
# casual -- rates,
class Employee:
    def __init__(self,names:str,id_no:str,department:str,gender:str):
        self.full_name = names
        self.identity_no = id_no
        self.department = department
        self.gender = gender

    def print_details(self):
        print(self.full_name)
        print(self.identity_no)
        print(self.department)
        print(self.gender)
        print("----------------")

class SalariedEmployee(Employee):
    def __init__(self, names: str, id_no: str, department: str, gender: str,salary:int, tenure:int):
       super().__init__(names, id_no, department, gender)
       self.tenure = tenure
       self.salary = salary

class CasualWorker(Employee):
    def __init__(self, names: str, id_no: str, department: str, gender: str, rate:float):
        super().__init__(names, id_no, department, gender)
        self.rate = rate
    def calc_wage(self, hours: float):
        return hours * self.rate

s1 = SalariedEmployee("Sarah", "22334455", "HR", "F", salary=95_000)
c1 = CasualWorker("Jack", "908656", "sales", "M",rate=356)

s1.print_details()
c1.print_details()
print(c1.calc_wage(19))
