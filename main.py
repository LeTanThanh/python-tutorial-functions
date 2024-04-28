if __name__ == "__main__":
  # Defining a Python function

  # def greet():
  #   """Display a greeting a users"""
  #   print("Hi")

  # greet()

  # Passing information to Python functions

  # def greet(name):
  #   print(f"Hi {name}")

  # greet("John")

  # first_name = "Jane"
  # greet(first_name)

  # Returning a value

  """
  return value
  """

  def greet(name):
    return f"Hi {name}"

  greeting = greet("John")
  print(greeting)

  # Python functions with multiple parameters

  def sum(a, b):
    return a + b

  total = sum(10, 20)
  print(total)
