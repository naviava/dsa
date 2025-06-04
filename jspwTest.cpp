from random import randint
from typing import List

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

  def insertion_sort_recursive(self, arr: List[int], start: int = 1):
    print(f"Step 0 -> {arr}")

    for i in range(1, len(arr)):
      if start <= 0: return arr
      
      if arr[start] < arr[start-1]:
        arr[start], arr[start-1] = arr[start-1], arr[start]
        self.insertion_sort_recursive(arr, start - 1)
          
      print(f"STEP {i} -> {arr}")
    
    print(arr)
    return arr
  
  # Merge sort.
  def merge_sort(self, arr: List[int]):
    print()
    print("==================================")
    print("MERGE SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")
  
  # Quick sort.
  @staticmethod
  def quick_sort(arr: List[int]):
    print()
    print("==================================")
    print("QUICK SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")
    
    
    print()
    
nums: List[int] = [randint(1, 99) for _ in range(5)]

s = Sorting()
s.insertion_sort_recursive(nums);