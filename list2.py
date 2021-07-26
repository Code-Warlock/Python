"""nums = [1,2,3,4,5,6,7,8]
nums2 = nums.copy()
# nums2.clear()

nums2.extend(nums)
nums2.insert(2,["Desmond","Michael"])
nums2.pop(-1)
nums2.remove(["Desmond","Michael"])
nums.reverse()
nums2.sort()
print(nums2)
"""

#
# vals = ["desmond","Desmond","Apple","apple"]
# vals.sort(reverse=True)
# print(vals)
name = input("Enter your name : ")
name.replace("D","P")
listed_name = list(name)
print(listed_name)
listed_name[0] = "P"
print(listed_name)
