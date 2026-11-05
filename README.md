# Calculator lab project
## How to run it
Run: python3 calculator.py
Opreations: + - * / (two numbers)

This project is a simple calculator that performs basic arithmetic opreation,
 including addition, subtracton, mutipilication and division.
# Calculator
A Python 3 calculator used from the Terminal, built step by step in SCCM4910.
## What it will do
Add, subtract, multiply and divide two numbers; display the result.
## How to run it
From Week 3: python3 calculator.py
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer.
use ./run.sh to runing the calculator and use ctrl c stop this calculator
## Lab 5 - Testing
This calculator uses Python 3 and pytest.
Install pytest using requirements-dev.txt.
## Run Tests
Activate the environment:
	source /opt/python-venv/sccm-4910/bin/activate
Run the quality gate:
	./check.sh
Expected result:
-5 passed
-QUALITY GATE PASSED
Check the exit status:
	echo $?
-0 = Tests passed
-1 = Tests failed
-5 = No tests collected

A non-zero status means the check did not pass.
