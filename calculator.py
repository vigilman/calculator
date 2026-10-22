# SCCM4910 lab project - a four-operation calculator
def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def mutiply(a,b):
	return a * b

def divide(a,b):
	return a / b

def main():
	while True:
		a = float(input("First number: "))
		op = input("Operator (+ - * /): ")
		b = float(input("Second number: "))
		if op == "+":
			print("Result:", add(a,b))
		elif op == "-":
			print("Result:", subtract(a,b))
		elif op == "*":
                        print("Result:", mutiply(a,b))
		elif op == "/":
                        print("Result:", divide(a,b))
		else:
			print("Unknown operator:", op)

if __name__ == "__main__":
	main()
