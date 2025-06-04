from random import randint
from typing import List, Optional

class Sorting:
  # Selection sort.
  @staticmethod
  def selection_sort(arr: List[int]):
    print()
    print("==================================")
    print("SELECTION SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")
    
    for i in range(len(arr) - 1):
      min: int = i
      
      for j in range(i+1, len(arr)):
        if j == len(arr):
          return
        if arr[j] < arr[min]:
          min = j
      
      arr[i], arr[min] = arr[min], arr[i]
      print(f"Step {i+1} -> {arr}: {arr[i]} moved to I{i}, {arr[min]} moved to I{min}.")
    
    print()
    
  # Bubble sort.
  @staticmethod
  def bubble_sort(arr: List[int], start: int, end: int):
    print()
    print("==================================")
    print("BUBBLE SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")
    
    while start < end:
      hasSwapped = False
      for i in range(end - 1):
        if arr[i] > arr[i+1]:
          arr[i], arr[i+1] = arr[i+1], arr[i]
          hasSwapped = True
        
      print(f"Step {len(arr) - end + 1} -> {arr}")
      
      if hasSwapped:
        end -= 1
      else:
        end = 0
  
  def bubble_sort_recursive(self, arr: List[int], start: int, end: int):
    if start >= end:
      return arr
    
    hasSwapped = False
    print(f"Step {len(arr) - end} -> {arr}")
    for i in range(end - 1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        hasSwapped = True

    if hasSwapped:
      self.bubble_sort_recursive(arr, 0, end - 1)
        
    return arr
  
  # Insertion sort.
  @staticmethod
  def insertion_sort(arr: List[int]):
    print()
    print("==================================")
    print("INSERTION SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")

    for i in range(1, len(arr)):
      start = i
      while start > 0:
        if arr[start] < arr[start-1]:
          arr[start], arr[start-1] = arr[start-1], arr[start]
          start -= 1
        else:
          start = 0
          
      print(f"STEP {i} -> {arr}")
    
    return arr

  def insertion_sort_recursive(self, arr: List[int], n: Optional[int] = None):
    if n is None:
        n = len(arr)
        print(f"Step 0 -> {arr}")

    # Base case
    if n <= 1:
        return arr

    # Sort first n-1 elements
    self.insertion_sort_recursive(arr, n - 1)

    # Insert last element at its correct position
    last = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        arr[j] = last
        j -= 1

    print(f"Step {n-1} -> {arr}")
    return arr
  
    
  """
  merge() accepts two sorted arrays as input.
  Merges them and returns a sorted array.
  """
  def merge(self, a1: List[int], a2: List[int]):
      left = 0
      right = 0
      result: List[int] = []
      print(f"Merging {a1}, {a2}")
      
      while left < len(a1) and right < len(a2):
        if a1[left] < a2[right]:
          result.append(a1[left])
          left += 1
        else:
          result.append(a2[right])
          right += 1
      
      while left < len(a1):
        result.append(a1[left])
        left += 1
      
      while right < len(a2):
        result.append(a2[right])
        right += 1
      
      print(result)
      print()
      return result
  
  # Merge sort.
  def merge_sort(self, arr: List[int]):
    print(f"Split -> {arr}")
    
    mid = int(len(arr) / 2)
    left = self.merge_sort(arr[0:mid])
    right = self.merge_sort(arr[mid:])
    
    return self.merge(left, right)
  
  # Pivot function for quick sort.
  def pivot(self, arr: List[int], start: int, end: int):
    if start >= end:
      return start
    
    print(f"{arr}")
    shift: int = start
    
    for i in range(start + 1, end):
      if arr[i] < arr[start]:
        shift += 1
        arr[i], arr[shift] = arr[shift], arr[i]
    
    arr[start], arr[shift] = arr[shift], arr[start]
    print(f"Pivot = {shift}")
    return shift
  
  # Quick sort.
  def quick_sort(self, arr: List[int], start: int, end: int):
    if (start >= end - 1):
      return arr
    
    pivot_pt = self.pivot(arr, start, end)
    self.quick_sort(arr, start, pivot_pt)
    self.quick_sort(arr, pivot_pt + 1, end)
    
    return arr
        
nums: List[int] = [randint(1, 99) for _ in range(10)]

s = Sorting()
# print(s.quick_sort(nums));
print(s.quick_sort(nums, 0, len(nums)));