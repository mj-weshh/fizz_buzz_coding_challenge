"""
FizzBuzz challenge
Instructions:
- Print/log the numbers from 1 to 100
- For multiples of three print 'Fizz' instead of the number
- For multiples of five print 'Buzz'
- For mumbers which are multiples of both three and five print 'FizzBuzz'.
"""

def mod(number):
     if number % 3 == 0 and number % 5 == 0:
          return "FizzBuzz"
     elif number % 5 == 0 and number % 3 != 0:
          return "Buzz"
     elif number % 3 == 0 and number % 5 !=0:
          return "Fizz"
     else:
          return number


def output(list_num):
     for i in list_num:
          print(i)


def main():
     num_list = []
     for i in range(100):
          num_list.append(mod(i))
     output(num_list)


if __name__ == "__main__":
     main()