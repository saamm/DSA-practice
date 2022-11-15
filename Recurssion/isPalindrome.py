def check_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        else:
            return check_palindrome(s[1:-1])

var = input("Enter a value : ")
if check_palindrome(var):
    print("the input is a palindrome")
else:
    print("the input is not a palindrome")
