#1.2 Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements


def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False


# Input from the user
year = int(input("Enter a year: "))

if is_leap_year(year):
  print(f"{year} is a leap year.")
else:
  print(f"{year} is not a leap year.")
