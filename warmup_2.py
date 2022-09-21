#Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
  return str*n

# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'
# string_times('Hi', 1) → 'Hi'

#Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
  return str[0:3]*n

# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  return str[::2]

# string_bits('Hello') → 'Hlo'
# string_bits('Hi') → 'H'
# string_bits('Heeololeo') → 'Hello'

#Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
  s = ""
  for i in range(len(str)+1):
    s += str[:i]
  return s

# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'

#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
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

# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2

#Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
  n = 0
  for i in nums:
    if i == 9:
      n += 1
  return n

# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

#Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
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

# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

#Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
  for i in range(len(nums)):
    if nums[i:i+3] == [1,2,3]:
      return True
  return False

# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
  n = 0
  for i in range(len(a)-1):
    if a[i:i+2] == b[i:i+2]:
      n += 1
  return n

# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0