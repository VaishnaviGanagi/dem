try:
  a=int(input("Enter first number:"))
  b=int(input("Enter second number:"))
  print(f"Add:{a+b}")
  print(f"sub:{a-b}")
except ValueError:
  print("enter valid integer")
