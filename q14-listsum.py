nums = list(map(int, input("Enter numbers: ").split()))
print(sum(nums))

#or

nums = list(map(int, input("Enter numbers: ").split()))

sum = 0
for n in nums:
    sum += n

print("Sum =", sum)
