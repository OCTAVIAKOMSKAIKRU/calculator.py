def caculate():
  num1 = float(input("Enter number: "))
  num2 = float(input("Enter a second number: "))
  select_operator= input(("-", "+", "/", "*"))

  if "-" in select_operator:
    print(num1-num2)
  elif "+" in select_operator:
    print(num1+num2)
  elif "/" in select_operator:
    print(num1/num2)
  elif "*" in select_operator:
    print(num1*num2)
  else:
    print("invalid")

caculate()