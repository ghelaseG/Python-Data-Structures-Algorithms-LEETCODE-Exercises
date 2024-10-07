"""
Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, and emp_department and methods like calculate_emp_salary, emp_assign_department, and print_employee_details.
Sample Employee Data:
"ADAMS", "E7876", 50000, "ACCOUNTING"
"JONES", "E7499", 45000, "RESEARCH"
"MARTIN", "E7900", 50000, "SALES"
"SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary. Overtime is calculated as following formula:
overtime = hours_worked - 50
Overtime amount = (overtime * (salary / 50))
"""

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.name = emp_name
        self.id = emp_id
        self.salary = emp_salary
        self.department = emp_department
    
    def assign_department(self, emp_department):
        self.department = emp_department
    
    def calculate_emp_salary(self, salary, hours_worked):
        overtime = 0
        if hours_worked > 50:
            overtime = hours_worked - 50
        self.salary = self.salary + (overtime * (self.salary / 50))
    
    def print_employee_details(self):
        print('\nName:', self.name)
        print('ID:', self.id)
        print('Salary:', self.salary)
        print('Department:', self.department)
        print('..------------------------..')


employee1 = Employee('Adams', 'A1234', 50000, 'Accounting')
employee2 = Employee('Kala', 'K1234', 55000, 'Sales')
employee3 = Employee('George', 'G1234', 10000, 'Data Consultant')

print('Original Employee Details:')
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()

print("\nChanging the departments of some of the employees")
employee1.assign_department('Operator')
employee3.assign_department('Driver')

print("\nCalculate the overtime of the employees who are eligible:")
employee3.calculate_emp_salary(40000, 72)
employee2.calculate_emp_salary(45000, 60)

print("Updated employee details:")
employee1.print_employee_details()
employee2.print_employee_details()
employee3.print_employee_details()