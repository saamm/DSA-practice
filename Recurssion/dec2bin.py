def dec2bin(dec, result):
    if dec == 0:
        return result
    print(dec)
    #print(type(dec%2))
    result = str(dec%2) + str(result)
    return dec2bin(dec//2, result)

num = input("Enter your number: ")
print(dec2bin(int(num), 0))