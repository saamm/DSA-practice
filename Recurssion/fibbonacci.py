def fib(num):
    if num == 0 or num == 1:
        return num
    else:
        #print(num,'******')
        return fib(num-1) + fib(num-2)

print(fib(6))