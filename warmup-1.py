def sleep_in(weekday, vacation):
  return (not weekday) or (vacation)

def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

def sum_double(a, b):
  sum = a + b
  if a == b:
    return sum * 2
  else:
    return sum
  
def diff21(n):
  diff = abs(n - 21)
  if n > 21:
    return diff * 2
  else:
    return diff
  
def parrot_trouble(talking, hour):
  return (talking) and ((hour < 7) or (hour > 20))

def makes10(a, b):
  sum = a + b
  return (sum == 10) or (a == 10) or (b == 10)

def makes10(a, b):
  sum = a + b
  return (sum == 10) or (a == 10) or (b == 10)

def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return (a < 0 and b > 0) or (a > 0 and b < 0)

def not_string(str):
  if str[0:3] == "not":
    return str
  else:
    return "not " + str

def missing_char(str, n):
  return str[0:n] + str[n+1:len(str)]

def front_back(str):
  if len(str) == 1 or len(str) == 0: #return string if it is one or less chars
    return str
  if len(str) == 2:  #switch letters if string is 2 chars 
    return str[::-1]
  else:
    return str[-1] + str[1:len(str)-1] + str[0] #swap first and last chars

