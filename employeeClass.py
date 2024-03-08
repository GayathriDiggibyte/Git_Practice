class employee:
    def __init__(self,empid,empname,salary,address,phno):
        self.empid=empid
        self.empname=empname
        self.salary=salary
        self.address=address
        self.phno=phno
    def display(self):
        print("EMPLOYEE ID : ",self.empid)
        print("EMPLOYEE NAME : ",self.empname)
        print("EMPLOYEE SALARY : ",self.salary)
        print("EMPLOYEE ADDRESS : ",self.address)
        print("Employee Phone No : ",self.phno)
    def calculate_annual_salary(self):
        print("The annual salary of",self.empname,"is",12*self.salary)


def main():
    employees=[]
    while(True):
        a=input("Do you want to give input? yes or no : ")
        if(a=="no"):
            break
        else:
            id=input("Enter the employee id : ")
            name=input("Enter the employee name : ")
            salary=float(input("Enter the employee salary : "))
            address=input("Enter the employee address : ")
            phno=int(input("Enter the employee phone number : "))
            e=employee(id,name,salary,address,phno)
            employees.append(e)
    for x in employees:
        x.display()
        x.calculate_annual_salary()

main()



