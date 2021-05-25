import re

def isPalindrome(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    # re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1] # 슬라이싱

print(isPalindrome("A man, a plan, a canal: Panama")) # True
print(isPalindrome("race a car")) # False


