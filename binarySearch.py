def main(n,q):
    final = binarySearch(n,q)
    print(final)

def binarySearch(nums,target):
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1 # if number is not found.

nums = [1,4,5,7,8,9,12,34,65]
target = 9
main(nums, target)


