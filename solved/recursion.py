# i = 1 on first pass.
from typing import List


def n_times_asc(i: int, n: int):
  if (i > n): return
  
  print(n-i+1)
  n_times_asc(i+1, n)

# i = n on first pass.
def n_times_desc(i: int, n: int):
  if (i < 1): return
  
  print(i)
  n_times_desc(i-1, n)
  
# i = n on first pass.
def basket_asc(i: int, n: int):
  if i < 1: return
  basket_asc(i-1, n)
  print(i)

# i = 1 on first pass.
def basket_desc(i: int, n: int):
  if i > n: return
  basket_desc(i+1, n)
  print(i)

# sum = 0 on first pass.
def parameterized_recursion(i: int, sum: int):
  if i < 1:
    print(sum)
    return
  parameterized_recursion(i-1, sum + i)
  
def functional_recursion(n: int):
  if n == 0:
    return 0
  return n + functional_recursion(n-1)

def factorial(n: int):
  if n == 0:
    return 1
  return n * factorial(n-1)

def reverse_array_pointer(a: list):
  min = 0
  max = len(a) - 1
  
  while max > min:
    temp = a[min]
    a[min] = a[max]
    a[max] = temp
    
    min += 1
    max -= 1
  
  return a

# i = 0 on first pass
def rev_array_recursion(i: int, a: list):
  n = len(a)
  if i > n/2: return
  a[i], a[n-i-1] = a[n-i-1], a[i]
  rev_array_recursion(i+1, a)
  return a
  
# i = 0 on first pass.
def palindrome(i: int, word: str):
  n = len(word)
  
  if i > n/2:
    return True
  if word[i] != word[n-i-1]:
    return False
  
  return palindrome(i+1, word)

# n is user choice. i = 0, arr = [] on first pass.
def fibonacci_array(n: int, i: int, arr: List[int]):
  if i >= n:
    return arr
  
  if i <= 1:
    arr.append(i)
  else:
    arr.append(arr[i-1] + arr[i-2])
  
  return fibonacci_array(n, i+1, arr)

def fibo_value(n: int):
  if n <= 1:
    return n
  
  return fibo_value(n-1) + fibo_value(n-2)

print(fibo_value(0))