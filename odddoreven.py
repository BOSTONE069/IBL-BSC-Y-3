def main():
  """
  The function takes an input value and determines if it is even or odd.
  """
  x = int(input("What is the value of x? "))
  if mod(x):
    print("Even")
  else:
    print("Odd")


def mod(n):
  """
  The function checks if a given number is even or odd.

  :param n: The input parameter for the function mod, which is a number that we want to check if it is
  even or odd
  :return: The function `mod(n)` returns `True` if the input `n` is even (i.e., divisible by 2) and
  `False` otherwise.
  """
  return n % 2 == 0

main()