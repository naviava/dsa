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
  def bubble_sort(arr: List[int]):
    print()
    print("==================================")
    print("BUBBLE SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")
    
    
    print()
  
  # Insertion sort.
  @staticmethod
  def insertion_sort(arr: List[int]):
    print()
    print("==================================")
    print("INSERTION SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")
    
    
    print()
  
  # Merge sort.
  @staticmethod
  def merge_sort(arr: List[int]):
    print()
    print("==================================")
    print("MERGE SORT ALGORITHM")
    print("==================================")
    print(f"Step 0 -> {arr}")
    
    
    print()
  
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

Sorting.bubble_sort(nums);