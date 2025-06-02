import math
from typing import List

def count_digits(n: int):
    print(int(math.log10(n) + 1))

def reverse_num(n: int):
  rev_num = 0
  while n > 0:
    rev_num = (rev_num * 10) + (n % 10)
    n = int(n / 10)
  
  print(rev_num)
  return rev_num

def palindrome(n: int):
  rev_num = reverse_num(n)
  print(n == rev_num)
  
def armstrong_num(n: int):
  sum = 0;
  num = n;
  digits: List[int] = []
  
  while num > 0:
    digits.append(int(num % 10))
    num = int(num / 10)
  
  for dig in iter(digits):
    sum = sum + (dig ** len(digits))
  
  print(f"Sum -> {sum}")
  if sum == n:
    print(f"{n} is an armstrong number!")
  else:
    print(f"{n} isn't an armstrong number.")
  
def all_divisions(n: int):
  nums: List[int] = []
  for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
      nums.append(i)
      other_factor = int(n / i)
      if other_factor != i:
        nums.append(other_factor)
  
  nums.sort()
  
  print(nums)
  return nums

def prime_number(n: int):
  divs = all_divisions(n)
  print(len(divs) <= 2)



all_divisions(67)