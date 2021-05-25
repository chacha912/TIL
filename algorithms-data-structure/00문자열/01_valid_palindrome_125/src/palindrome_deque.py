import collections

def isPalindrome(s: str) -> bool:

    # 자료형 데크로 선언
    strs = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False


