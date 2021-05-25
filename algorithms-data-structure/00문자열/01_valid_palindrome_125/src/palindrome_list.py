def isPalindrome(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum(): # 문자, 숫자만을 대상으로 
            strs.append(char.lower()) 

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False


