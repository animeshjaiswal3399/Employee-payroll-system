
# Employee Payroll System

# Fixed values
OVERTIME_RATE = 200
PF_RATE = 0.12
TAX_RATE = 0.10
MANAGER_BONUS = 0.10

FILE_NAME = "payroll.txt"


# Employee Class
class Employee:

    def __init__(self, emp_id, name, basic, overtime_hours):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.overtime_hours = overtime_hours

    # Calculate overtime amount
    def calculate_overtime(self):
        return self.overtime_hours * OVERTIME_RATE

    # Calculate bonus
    def calculate_bonus(self):
        return 0

    # Calculate gross salary
    def calculate_gross(self):
        return (
            self.basic
            + self.calculate_overtime()
            + self.calculate_bonus()
        )

    # Calculate net salary
    def calculate_net(self):
        gross = self.calculate_gross()

        pf = self.basic * PF_RATE

        if gross > 50000:
            tax = gross * TAX_RATE
        else:
            tax = 0

        net = gross - pf - tax

        return gross, pf, tax, net

    # Print and save payslip
    def print_payslip(self):

        gross, pf, tax, net = self.calculate_net()

        payslip = f"""
------------------------------------
          EMPLOYEE PAYSLIP
------------------------------------
Employee ID     : {self.emp_id}
Employee Name   : {self.name}
Basic Salary    : Rs. {self.basic:.2f}
Overtime Hours  : {self.overtime_hours}
Overtime Amount : Rs. {self.calculate_overtime():.2f}
Bonus           : Rs. {self.calculate_bonus():.2f}
Gross Salary    : Rs. {gross:.2f}
PF Deduction    : Rs. {pf:.2f}
Tax Deduction   : Rs. {tax:.2f}
Net Salary      : Rs. {net:.2f}
------------------------------------
"""

        print(payslip)

        # Save payslip in file
        with open(FILE_NAME, "a") as file:
            file.write(payslip)


# Manager Class (Inheritance)
class Manager(Employee):

    def calculate_bonus(self):
        return self.basic * MANAGER_BONUS


# Function to take valid input
def get_positive_salary():

    while True:
        try:
            basic = float(input("Enter basic salary: "))

            if basic <= 0:
                print("Invalid basic salary. Enter a positive number.")
            else:
                return basic

        except ValueError:
            print("Invalid basic salary. Enter a positive number.")


def get_overtime():

    while True:
        try:
            hours = float(input("Enter overtime hours: "))

            if hours < 0:
                print("Invalid overtime hours. Enter a non-negative number.")
            else:
                return hours

        except ValueError:
            print("Invalid overtime hours. Enter a non-negative number.")


# Main Program
def main():

    print("================================")
    print("      EMPLOYEE PAYROLL SYSTEM")
    print("================================")

    while True:

        print("\n1. Employee")
        print("2. Manager")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")

            basic = get_positive_salary()
            hours = get_overtime()

            emp = Employee(emp_id, name, basic, hours)

            emp.print_payslip()

        elif choice == "2":

            emp_id = input("Enter Manager ID: ")
            name = input("Enter Manager Name: ")

            basic = get_positive_salary()
            hours = get_overtime()

            manager = Manager(emp_id, name, basic, hours)

            manager.print_payslip()

        elif choice == "3":

            print("Thank you for using Employee Payroll System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()
