Employee Payroll System – Project Summary
1. Introduction
The Employee Payroll System is a Python-based project developed to calculate the salaries of employees and managers. It calculates gross salary, overtime pay, bonus, Provident Fund (PF), tax deductions, and final net salary.

The project uses Object-Oriented Programming (OOP), functions, calculations, and file handling to manage payroll information efficiently.
2. Objectives
- To calculate the salary of employees and managers.
- To calculate overtime payment and manager bonuses.
- To apply PF and tax deductions.
- To generate employee payslips.
- To validate user inputs.
- To save salary details in a file.
3. Technologies Used
- Programming Language: Python 3
- IDE: VS Code
- Concepts: Classes, Objects, Inheritance, Functions, Conditional Statements, Loops, and File Handling.
4. Project Features
1. Accepts employee ID, name, basic salary, and overtime hours.
2. Calculates overtime payment at Rs. 200 per hour.
3. Provides managers with a 10% bonus on basic salary.
4. Calculates PF at 12% of basic salary.
5. Calculates 10% tax if gross salary is above Rs. 50,000.
6. Calculates the final net salary.
7. Displays a complete salary payslip.
8. Saves payslips in payroll.txt.
9. Supports multiple employees.
10. Validates incorrect inputs.
5. Salary Calculation
The project uses the following formulas:
Component	Formula
Overtime Pay	Overtime Hours × 200
Manager Bonus	10% of Basic Salary
Gross Salary	Basic + Overtime + Bonus
PF	12% of Basic Salary
Tax	10% of Gross Salary if Gross is above Rs. 50,000
Net Salary	Gross − PF − Tax

6. Classes Used
Employee Class: Stores employee details and contains methods to calculate gross salary, net salary, and print payslips.

Manager Class: Inherits the Employee class and provides an additional 10% bonus on basic salary.
7. Test Cases
The project includes four test cases:
- Test Case 1: Normal employee salary calculation.
- Test Case 2: Minimum salary with zero overtime hours.
- Test Case 3: Invalid salary and overtime input validation.
- Test Case 4: Manager salary calculation with bonus and deductions.
8. File Handling
The project uses a file named payroll.txt to store the payslips of employees and managers. This helps maintain salary records even after the program is closed.
9. Conclusion
The Employee Payroll System is a simple Python project that automates salary calculations for employees and managers. It demonstrates important Python programming concepts such as OOP, inheritance, functions, loops, input validation, and file handling.

This project helps in understanding how programming can be used to solve real-world payroll management problems.
