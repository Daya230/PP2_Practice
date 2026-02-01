a = list(map(int, input().split()))
nums = list(map(int, input().split()))
nums[a[1]-1:a[2]] = nums[a[1]-1:a[2]][::-1]
print(*nums)