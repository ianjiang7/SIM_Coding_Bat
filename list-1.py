def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  return False

def make_pi():
  return [3,1,4]

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def sum3(nums):
  sum = 0
  for i in nums:
    sum += i
  return sum

def rotate_left3(nums):
  x = nums.pop(0)
  nums.append(x)
  return nums

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0],nums[0]]
  else:
    return [nums[2], nums[2],nums[2]]

def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]

def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[-1]]

def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False


