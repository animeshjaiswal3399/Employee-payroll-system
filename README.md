# Employee Payroll System

**PS No.:** 49\
**Project Title:** Employee Payroll System\
**Language:** Python 3

## 1. Project Overview

The Employee Payroll System is a Python console application that
calculates the net salary of employees and managers. It uses
object-oriented programming, functions, calculations, input validation,
and file handling.

The program calculates overtime pay, manager bonuses, Provident Fund
(PF), tax deductions, and net salary. It also saves each payslip to a
file named `payroll.txt`.

## 2. Objectives

-   Calculate employee and manager salaries accurately.
-   Use Python classes and inheritance.
-   Apply overtime, bonus, PF, and tax rules.
-   Validate salary and overtime inputs.
-   Allow the user to process multiple employees.
-   Display payslips and save them to a text file.

## 3. Salary Calculation Rules

  -----------------------------------------------------------------------
  Component                           Rule
  ----------------------------------- -----------------------------------
  Overtime pay                        Overtime hours × ₹200

  Manager bonus                       10% of basic pay

  Gross salary                        Basic pay + overtime pay + bonus

  PF deduction                        12% of basic pay

  Tax deduction                       10% of gross salary if gross salary
                                      is above ₹50,000; otherwise ₹0

  Net salary                          Gross salary − PF − tax
  -----------------------------------------------------------------------

For a regular employee, the manager bonus is not added.

## 4. Classes Used

### Employee

The `Employee` class represents a regular employee. It stores employee
details such as ID, name, basic pay, and overtime hours. It calculates
gross salary and net salary and helps display the payslip.

### Manager

The `Manager` class inherits from `Employee`. It adds a bonus equal to
10% of basic pay and includes that bonus when calculating gross salary.

## 5. Main Features

-   Accepts employee or manager details.
-   Calculates overtime pay at ₹200 per hour.
-   Adds a 10% basic-pay bonus for managers.
-   Deducts PF at 12% of basic pay.
-   Applies tax only when gross salary is above ₹50,000.
-   Checks that basic pay is positive.
-   Checks that overtime hours are a non-negative number.
-   Supports processing more than one employee.
-   Displays and saves payslips in `payroll.txt`.

## 6. Sample Test Cases

### Test Case 1: Normal Input

**Input** - Employee ID: E1 - Name: Aman - Basic pay: ₹30,000 - Overtime
hours: 10

**Expected output** - Overtime pay: ₹2,000 - Gross salary: ₹32,000 - PF:
₹3,600 - Tax: ₹0 - **Net salary: ₹28,400**

### Test Case 2: Boundary / Minimum Input

**Input** - Employee ID: E2 - Name: Neha - Basic pay: ₹10,000 - Overtime
hours: 0

**Expected output** - Overtime pay: ₹0 - Gross salary: ₹10,000 - PF:
₹1,200 - Tax: ₹0 - **Net salary: ₹8,800**

### Test Case 3: Invalid Input

  --------------------------------------------------------------------------------------------
  Input                               Expected validation message
  ----------------------------------- --------------------------------------------------------
  Basic pay: `-5000`                  `Invalid basic salary. Enter a positive number.`

  Overtime hours: `abc`               `Invalid overtime hours. Enter a non-negative number.`
  --------------------------------------------------------------------------------------------

### Test Case 4: Manager Scenario

**Input** - Manager ID: M1 - Name: Riya - Basic pay: ₹60,000 - Overtime
hours: 5

**Expected output** - Overtime pay: ₹1,000 - Bonus: ₹6,000 - Gross
salary: ₹67,000 - PF: ₹7,200 - Tax: ₹6,700 - **Net salary: ₹53,100**

## 7. Requirements

-   Python 3
-   Any code editor, such as Visual Studio Code
-   A terminal or command prompt

No external Python packages are required for the features described in
the project statement.

## 8. How to Run the Project

1.  Save the Python program in a file, for example, `payroll.py`.

2.  Open the project folder in Visual Studio Code.

3.  Open the VS Code terminal.

4.  Run:

    ``` bash
    python payroll.py
    ```

5.  Enter the employee or manager details when prompted.

6.  View the calculated payslip in the console. The program should save
    payslips to `payroll.txt`.

## 9. Output File

The program stores the generated payslips in:

``` text
payroll.txt
```

The file is created when the program saves the payslips. Each payslip
should include the employee or manager details and the salary
calculation results.

## 10. Concepts Used

-   Python classes and objects
-   Inheritance
-   Functions and methods
-   Conditional statements
-   Loops
-   User input and input validation
-   Arithmetic calculations
-   File handling

## 11. Conclusion

The Employee Payroll System demonstrates how Python can be used to
automate basic payroll calculations. It applies object-oriented
programming through the `Employee` and `Manager` classes, validates user
input, calculates salary components, displays payslips, and stores
payroll records in a file.
