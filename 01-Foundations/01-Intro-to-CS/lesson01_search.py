# مقارنة بين البحث الخطي والبحث الثنائي على مليون عنصر
numbers = list(range(1, 1000001)) # قائمة مرتبة من 1 لمليون
target = 999999 


# 1. البحث الخطي (Linear Search)
linear_steps = 0 
for num in numbers:
    linear_steps += 1
    if num == target:
        break

# 2. البحث الثنائي (Binary Search)
low = 0 
high = len(numbers)-1 
binary_steps = 0

while low <= high:
    binary_steps += 1
    mid = (low + high) // 2
    if numbers[mid]==target:
        break
    elif numbers[mid] < target:
        low = mid + 1
    else:
        high = mid -1

print(f"Linear Search steps: {linear_steps}")
print(f"Binary Search steps: {binary_steps}")