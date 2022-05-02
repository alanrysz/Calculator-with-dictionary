#Calculator
dictionary = {}

def calculator():
  

  n1 = int(input("Write the first number: "))
  
  def add(n1,n2):
    return n1 + n2

  def subtract(n1,n2):
    return n1 - n2

  def multiply(n1,n2):
    return n1 * n2
  
  def div(n1,n2):
    return n1 / n2
  
  dictionary = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : div
  }
  
  for key in dictionary:
    print(key)

  operation_symbol = input("Write the operation do you want to show. ")
  n2 = int(input("Write the second number: "))
  calculation_function = dictionary[operation_symbol]
  answer = calculation_function(n1,n2)

  
  
  print(f"{n1} {operation_symbol} {n2} = {answer}")
  
calculator()
