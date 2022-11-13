def reverseString(s):
    s = list(map(str, s))
    def reverse(l,r):
        #print(l, r)
        if l < r:
            s[l] , s[r] = s[r] , s[l]
            reverse(l+1, r-1)
    reverse(0, len(s) - 1)
    s = "".join(map(str, s))
    return s

word = "hello"
print(reverseString(word))

def isPalindrome(s):
    print(s)
    #s = list(map(str,s))
    def checkquals(l, r):
        if l < r:
            print(l , r)
            if s[l] != s[r]:
                #print("check")
                check = "not a palindrome"
                print(check)
                return
            checkquals(l+1, r-1)
        check = "is a palindrome"
        print(check)
        return "is a palindrome"
    checkquals(0, len(s)-1)

word = "helleh"
print(isPalindrome(word))
