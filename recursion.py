# i = 1 on first pass.
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

# def rev_array_recursion(a: list):
  

print(reverse_array_pointer([1,2,"dsd",3,5,"gha",75,12,55,"sd"]))