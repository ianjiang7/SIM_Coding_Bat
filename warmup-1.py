def sleep_in(weekday, vacation):
  return (not weekday) or (vacation)
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

def sum_double(a, b):
  sum = a + b
  if a == b:
    return sum * 2
  else:
    return sum
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

def diff21(n):
  diff = abs(n - 21)
  if n > 21:
    return diff * 2
  else:
    return diff
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0  

def parrot_trouble(talking, hour):
  return (talking) and ((hour < 7) or (hour > 20))
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

def makes10(a, b):
  sum = a + b
  return (sum == 10) or (a == 10) or (b == 10)
# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True

def makes10(a, b):
  sum = a + b
  return (sum == 10) or (a == 10) or (b == 10)
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)
# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

def not_string(str):
  if str[0:3] == "not":
    return str
  else:
    return "not " + str
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'
  
def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'

def front_back(str):
  if len(str) == 1 or len(str) == 0: #return string if it is one or less chars
    return str
  if len(str) == 2:  #switch letters if string is 2 chars 
    return str[::-1]
  else:
    return str[-1] + str[1:len(str)-1] + str[0] #swap first and last chars
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

def front3(str):
  return str[0:3]*3
# front3('Java') → 'JavJavJav'
# front3('Chocolate') → 'ChoChoCho'
# front3('abc') → 'abcabcabc'
