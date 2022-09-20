
def string_times(str, n):
  return str*n

def front_times(str, n):
  return str[0:3]*n

def string_bits(str):
  return str[::2]

def string_splosion(str):
  s = ""
  for i in range(len(str)+1):
    s += str[:i]
  return s

def last2(str):
  last = str[-2:]
  n = 0
  if str == "":
    return 0
  for i in range(len(str)):
    s = str[i:i+2]
    if last == s:
      n += 1
  return n - 1

def array_count9(nums):
  n = 0
  for i in nums:
    if i == 9:
      n += 1
  return n

def array_front9(nums):
  n = 0
  if len(nums) < 4:
    n = len(nums)
  else:
    n = 4
  for i in range(n):
    if nums[i] == 9:
      return True;
  return False

def array123(nums):
  for i in range(len(nums)):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False

def string_match(a, b):
  n = 0
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
      n += 1
  return n
