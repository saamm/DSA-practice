def totalSum(num):
    if num == 0:
        return num
    return num + totalSum(num-1)

num = input("Enter your num: ")
print(totalSum(int(num)))