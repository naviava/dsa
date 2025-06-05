from random import randint
from typing import List, Set

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

p = Problems()
nums: List[int] = [randint(1,99) for _ in range(5)]
# p.sorted_rotate(nums)
print(p.linear_search([2, -4, 4, 0, 10], 0))
