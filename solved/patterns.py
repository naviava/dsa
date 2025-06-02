def pattern01(n: int):
  for _ in range(n):
    for _ in range(n):
      print("*", end=" ")
    print()
    
def pattern02(n: int):
  for i in range(n):
    for _ in range(i+1):
      print("*", end=" ")
    print()
    
def pattern06(n: int):
  for i in range(n):
    for j in range(n-i):
      print(j + 1, end=" ")
    print()
    
def pattern07(n: int):
  for i in range(n):
    # Spaces
    for _ in range(n-i-1):
      print(" ", end=" ")
    
    # Stars
    for _ in range((2*i)+1):
      print("*", end=" ")
    
    # Spaces
    for _ in range(n-i-1):
      print(" ", end=" ")
    
    print()

def pattern08(n: int):
  for i in range(n):
    # Spaces
    for _ in range(i):
      print(" ", end=" ")
    
    # Stars
    for _ in range((2*(n-i))-1):
      print("*", end=" ")
    
    # Spaces
    for _ in range(i):
      print(" ", end=" ")
    
    print()
    
def pattern09(n: int):
  pattern07(n)
  pattern08(n)

def pattern10(n: int):
  for i in range((2*n)-1):
    if i<n:
      for _ in range(i+1):
        print("*", end=" ")
      print()
      
    else:
      for _ in range((2*n)-i-1):
        print("*", end=" ")
      print()
      
def pattern11(n: int):
  for i in range(n):
    for j in range(i+1):
      if i%2 == j%2:
        print("1", end=" ")
      else:
        print("0", end=" ")
    print()
    
def pattern12(n: int):
  spaces = 2*(n-1)
  for i in range(n):
    # Number
    for j in range(i+1):
      if j+1 > 9:
        print("X", end=" ")
      else:
        print(j+1, end=" ")
    
    # Spaces
    for _ in range(spaces):
      print(" ", end=" ")
    
    # Number
    for j in range(i+1, 0, -1):
      # print(i-j+1, end=" ")
      if j > 9:
        print("X", end=" ")
      else:
        print(j, end=" ")
    
    spaces -= 2
    print()
    
def pattern13(n: int):
  num = 1
  for i in range(n):
    for _ in range(i+1):
      print(num, end=" ")
      num += 1
    
    print()
    
def pattern14(n: int):
  for i in range(n):
    char = "A"
    for _ in range(i+1):
      print(char, end=" ")
      char = chr(ord(char) + 1)
    print()

def pattern15(n: int):
  for i in range(n):
    char = "A"
    for _ in range(n-i):
      print(char, end=" ")
      char = chr(ord(char) + 1)
    print()

def pattern16(n: int):
  char = "A"
  
  for i in range(n):
    for _ in range(i+1):
      print(char, end=" ")
    
    char = chr(ord(char) + 1)
    print()

def pattern17(n: int):
  for i in range(n):
    char = "A"
    # Spaces
    for _ in range(n-i-1):
      print(" ", end=" ")
    
    # Character
    for j in range((2*i)+1):
      print(char, end=" ")
      if (j < i):
        char = chr(ord(char) + 1)
      else:
        char = chr(ord(char) - 1)
        
    
    # Spaces
    for _ in range(n-i-1):
      print(" ", end=" ")

    print()

def pattern18(n: int):
  if n > 26:
    n = 26
  for i in range(n):
    char = chr(ord("A") + n-i-1)
    
    for _ in range(i+1):
      print(char, end=" ")
      char = chr(ord(char) + 1)
    
    print()

def pattern19(n: int):
  # Symmetry top half
  for i in range(n):
    # Stars
    for _ in range(n-i):
      print("*", end=" ")
    
    # Spaces
    for _ in range(2*i):
      print(" ", end=" ")    
    
    # Stars
    for _ in range(n-i):
      print("*", end=" ")

    print();
  
  # Symmetry bottom half
  for i in range(n):
    # Stars
    for _ in range(i+1):
      print("*", end=" ")
      
    # Spaces
    for _ in range(2*(n-i-1)):
      print(" ", end=" ")    
    
    # Stars
    for _ in range(i+1):
      print("*", end=" ")
    
    print()

def pattern20(n: int):
  for i in range(2*n):
    # Top half
    if i < n:
      # Stars
      for _ in range(i+1):
        print("*", end=" ")
        
      # Spaces
      for _ in range(2*(n-i-1)):
        print(" ", end=" ")
      
      # Stars
      for _ in range(i+1):
        print("*", end=" ")
      
      print()
    
    else:
      # Stars
      for _ in range((2*n)-i-1):
        print("*", end=" ")
      
      # Spaces
      for _ in range(2*(i-n+1)):
        print(" ", end=" ")
      
      # Stars
      for _ in range((2*n)-i-1):
        print("*", end=" ")
      
      print()

def pattern21(n: int):
  for i in range(n):
    for j in range(n):
      if (i in (0, n-1)) or (j in (0, n-1)):
        print("*", end=" ")
      else:
        print(" ", end=" ")
    
    print()

def pattern22(n: int):
  total = (2*n) - 1
  for i in range(total):
    for j in range(total):
      top = i
      left = j
      right = 2*(n-1) - j
      bottom = 2*(n-1) - i
      print(n - min(top, left, bottom, right), end=" ")      

    print()
    
pattern22(9)

"""
    0 1 2 3 4 5 6 
    
0:  4 4 4 4 4 4 4         
1:  4 3 3 3 3 3 4         if (j <= i) num - 1
2:  4 3 2 2 2 3 4         else num + 1
3:  4 3 2 1 2 3 4         min = n - i
4:  4 3 2 2 2 3 4
5:  4 3 3 3 3 3 4
6:  4 4 4 4 4 4 4

n = 4

"""
