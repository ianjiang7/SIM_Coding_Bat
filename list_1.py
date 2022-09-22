#Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  return False


#first_last6([1, 2, 6])
#first_last6([6, 1, 2, 3])
#first_last6([13, 6, 1, 2, 3])

#Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[-1]:
    return True
  return False

#same_first_last([1, 2, 3])
#same_first_last([1, 2, 3, 1])
#same_first_last([1, 2, 1])

#Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
  return [3,1,4]

#make_pi()

#Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

#common_end([1, 2, 3], [7, 3])
#common_end([1, 2, 3], [7, 3, 2])
#common_end([1, 2, 3], [1, 3])

#Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
  sum = 0
  for i in nums:
	sum+= 1
  return sum

#sum3([1, 2, 3])
#sum3([5, 11, 2])
#sum3([7, 0, 0])

#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}
def rotate_left3(nums):
  x = nums.pop(0)
  nums.append(x)
  return nums

#rotate_left3([1, 2, 3])
#rotate_left3([5, 11, 9])
#rotate_left3([7, 0, 0])

#Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

#reverse3([1, 2, 3])
#reverse3([5, 11, 9])
#reverse3([7, 0, 0])

#Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0],nums[0]]
  else:
    return [nums[2], nums[2],nums[2]]

#max_end3([1, 2, 3])
#max_end3([11, 5, 9])
#max_end3([2, 11, 3])

#Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]

#sum2([1, 2, 3])
#sum2([1, 1])
#sum2([1, 1, 1, 1])

#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
  return [a[1], b[1]]

#middle_way([1, 2, 3], [4, 5, 6])
#middle_way([7, 7, 7], [3, 8, 0])
#middle_way([5, 2, 9], [1, 4, 5])

#Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
  return [nums[0], nums[-1]]

#make_ends([1, 2, 3])
#make_ends([1, 2, 3, 4])
#make_ends([7, 4, 6, 2])

#Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False

#has23([2, 5])
#has23([4, 3])
#has23([4, 5])
