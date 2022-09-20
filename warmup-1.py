#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
  return (not weekday) or (vacation)


#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
  return a_smile == b_smile

#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
  sum = a + b
  if a == b:
    return sum * 2
  else:
    return sum

  
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
  diff = abs(n - 21)
  if n > 21:
    return diff * 2
  else:
    return diff
  
  
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
  return (talking) and ((hour < 7) or (hour > 20))

#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
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

def front3(str):
  return str[0:3]*3
