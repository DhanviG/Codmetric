def add(a, b):
  return a + b
  
def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

y="yes"
while y=="yes":
  print("\nSimple Calculator")
  print("Choose an operation:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (*)")
  print("4. Division (/)")
  
  choice = input("Enter your choice (1,2,3,4): ")
  try:
      num1=float(input("Enter first number: "))
      num2=float(input("Enter second number: "))
      if choice == '1':
          result = add(num1, num2)
          operator = '+'
      elif choice == '2':
          result = subtract(num1, num2)
          operator = '-'
      elif choice == '3':
          result = multiply(num1, num2)
          operator = '*'
      elif choice == '4':
          if num2 == 0:
              raise ZeroDivisionError
          result = divide(num1, num2)
          operator = '/'
      else:
          print("Invalid choice. Please select 1, 2, 3 or 4.")
          continue
      print(f"\nResult: {num1} {operator} {num2} = {result}")
      y=input("Want to continue? Type yes: ").lower()
      
  except ValueError:
      print("Invalid input! Please enter numbers only.")
      
  except ZeroDivisionError:
      print("Warning!! Division by zero is not allowed!")
