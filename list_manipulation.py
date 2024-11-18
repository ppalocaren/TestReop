num_list = [10, 20, 33, 46, 55]
print("The number list is ", num_list)

print("The numbers divisible by 5 are ")

for num in num_list:
    if num % 5 == 0:
        print(num,end = ", ")
        