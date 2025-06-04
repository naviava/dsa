from random import randint
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
    largest = 0
    
    for i in range(1, len(arr)):
      if arr[i] > arr[largest]:
        largest = i
    
    if largest == 0:
      left = []
      right = arr[1:]
    elif largest == len(arr) - 1:
      left = arr[:len(arr) - 1]
      right = []
    else:
      left = arr[0:largest]
      right = arr[largest + 1:]
    
    print(f"Left -> {left}")
    print(f"Right -> {right}")
    
    for i in range(1, len(left)):
      if left[i] < left[i-1]:
        return False
      
    for i in range(1, len(right)):
      if right[i] < right[i-1] or (left and right[i] > arr[largest]):
        return False
    
    return True
    
p = Problems()
nums: List[int] = [randint(1,99) for _ in range(5)]
# p.sorted_rotate(nums)
print(p.sorted_rotate([6,7,7,5]))