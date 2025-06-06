from datetime import datetime
import math
from random import randint, shuffle
from typing import List

class Problems:
  # Returns the largest element in an array.
  def largest_element(self, arr: List[int]):
    print(f"Original -> {arr}")
    if len(arr) == 0:
      return 0
    
    largest: int = arr[0]
    for num in arr:
      if num > largest:
        largest = num
    
    print(f"Largest: {largest}")
    return largest
  
  def second_largest_element(self, arr: List[int]):
    print(f"Original -> {arr}")
    if len(arr) == 0:
      return 0
    
    largest: int = arr[0]
    second = float('-inf')
    
    for num in arr:
      print(second)
      if num > largest:
        largest = num
      elif num < largest and num > second:
        second = num
    
    print(f"Second largest: {second}")
    return second

  def second_smallest_element(self, arr: List[int]):
    print(f"Original -> {arr}")
    if len(arr) == 0:
        return 0
      
    smallest: int = arr[0]
    second = float('inf')
      
    for num in arr:
      print(second)
      if num < smallest:
        smallest = num
      elif num > smallest and num < second:
        second = num
      
    print(f"Second smallest: {second}")
    return second

  def sorted_rotate(self, arr: List[int]):
    print(f"Original -> {arr}")
    count = 0
    n = len(arr)
    
    for i in range(n):
      if arr[i] > arr[(i+1) % n]:
        count += 1
      if count > 1:
        return False
    
    return True
      
  def remove_duplicates(self, arr: List[int]):
    print(f"Original -> {arr}")
    
    if not arr:
      return 0
    
    write = 1
    
    for read in range(1, len(arr)):
      if arr[read] != arr[read - 1]:
        arr[write] = arr[read]
        write += 1
    
    return write
  
  def rotate_array_right(self, arr: List[int], k: int):
    print(f"Original -> {arr}")
    n = len(arr)
    k = k % n
    r = n - k

    temp = arr[0:r]
    print(f"Temp -> {temp}")
    
    arr[0:r] = []
    arr.extend(temp)
    
    print(f"Final -> {arr}")

  def rotate_array_left(self, arr: List[int], k: int):
    print(f"Original -> {arr}")
    n = len(arr)
    k = k % n

    temp = arr[0:k]
    print(f"Temp -> {temp}")
    
    arr[0:k] = []
    arr.extend(temp)
    
    print(f"Final -> {arr}")

  def move_zero_to_end(self, nums: List[int]):
    print(f"Original -> {nums}")
    pos = 0
    
    for i in range(len(nums)):
      if nums[i] != 0:
        nums[i], nums[pos] =  nums[pos], nums[i]
        pos += 1
    
    return nums

  def linear_search(self, nums: List[int], target: int):
    print(f"Original -> {nums}")
    
    for i, num in enumerate(nums):
      if num == target:
        return i
    return -1

  def array_union(self, a: List[int], b: List[int]):
    print(f"A -> {a}")
    print(f"B -> {b}")
        
    i = 0
    j = 0
    union: List[int | float] = []
    
    while i < len(a) and j < len(b):
      x = a[i]
      y = b[j]
      n = len(union)
      
      if x <= y:
        if n == 0 or x != union[-1]:
          union.append(x)
        i += 1
      else:
        if n == 0 or y != union[-1]:
          union.append(y)
        j += 1
      
    while i < len(a):
      if len(union) == 0 or a[i] != union[-1]:
          union.append(a[i])
      i += 1
    
    while j < len(b):
      if len(union) == 0 or b[j] != union[-1]:
          union.append(b[j])
      j += 1
    
    return union

  def array_intersection(self, a: List[int], b: List[int]):
    print(f"A -> {a}")
    print(f"B -> {b}")
    
    i = 0
    j = 0
    n1 = len(a)
    n2 = len(b)
    res: List[int] = []
    
    while i < n1 and j < n2:
      x = a[i]
      y = b[j]
      n = len(res)
      
      if x < y:
        i += 1
      elif y < x:
        j += 1
      else:
        if n == 0 or x != res[-1]:
          res.append(x)
        i += 1
        j += 1
    
    return res
  
  def missing_number(self, nums: List[int]):
    print(f"Original -> {nums}")
    
    n = len(nums)
    sum = int((n*(n+1)) / 2)
    
    # OR
    # sum: int = 0
    # for i in range(1, n+1):
    #   sum += i
    for num in nums:
      sum -= num
    
    return sum

  def max_consecutive_ones(self, nums: List[int]):
    print(f"Original -> {nums}")
    max = 0
    chain = 0
    
    if len(nums) == 0:
      return 0
    if len(nums) == 1:
      return nums[0]
    
    for num in nums:
      if num == 1:
        chain += 1
        if chain > max:
          max = chain
      
      else:
        chain = 0
      
    return max

  def single_number(self, nums: List[int]):
    print(f"Original -> {nums}")
    
    res = nums[0]
    if len(nums) == 1:
      return res
    for i in range(1, len(nums)):
      res = res ^ nums[i]
    
    return res

  # End of class.

# Inputs
p = Problems()
nums1: List[int] = [randint(0,1) for _ in range(1)]
nums2: List[int] = sorted([randint(1,10) for _ in range(7)])

n = 9
nums: List[int] = [i for i in range(n+1)]
nums.pop(randint(0,n))
shuffle(nums)

start = datetime.now()
print(p.single_number([2,2,1]))
print(p.single_number([4,1,2,1,2]))
print(p.single_number([1]))
end = datetime.now()

diff = (end - start).total_seconds() * 1000 * 1000

print()
print(f"Finished in {diff:.0f}ms.")