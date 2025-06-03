from random import randint
from typing import Dict, List, Tuple

def count_numbers(n: int):
  nums: List[int] = []
  map: Dict[int, int] = {}
  
  for _ in range(n):
    nums.append(randint(0,9))
    
  for num in iter(nums):
    map[num] = map.get(num, 0) + 1
  
  print(nums)
  return map

def count_chars(word: str):
  map: Dict[str, int] = {}
   
  for char in word:
    map[char] = map.get(char, 0) + 1
  
  return map

"""
Given an array of n integers, find the most frequent element in it,
i.e., the element that occurs the maximum number of times. 
If there are multiple elements that appear a maximum number of times,
find the smallest of them.
"""
def most_frequent(arr: List[int]):
    hmap: Dict[int, int] = {}
    
    for num in arr:
      hmap[num] = hmap.get(num, 0) + 1
    
    max_count: int = 0
    min_num: int = 0
    
    for num, count in hmap.items():
      if count > max_count or (count == max_count and num < min_num):
        max_count = count
        min_num = num

    print(f"{min_num} appears the most. {max_count} times!")
    return min_num
    
    
print(most_frequent([1,1,2,2,3,3,4,4,4,5,5,5]))