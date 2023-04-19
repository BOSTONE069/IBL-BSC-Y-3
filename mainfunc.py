def main():
  """
  The function prompts the user for their name and then calls the "hello" function with the user's
  name as an argument, as well as calling the "hello" function without any arguments.
  """
  name = input("What is your name?")
  hello (name)
  hello()



def hello(z="WORLD"):
  """
  The function "hello" prints a greeting message with a default argument of "WORLD".

  :param z: The parameter `z` is a string parameter with a default value of "WORLD". If no argument is
  passed to the function when it is called, the value of `z` will be "WORLD". If an argument is
  passed, the value of `z` will be replaced with the, defaults to WORLD (optional)
  """
  print("hello,", z)


main()