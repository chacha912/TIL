def solution(s):
    L = len(s)
    answer = ''

    def checkPalin(left, right):
        while left >= 0 and right < L and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if L < 2 or s == s[::-1]:
        return s

    for i in range(L-1):
        even = checkPalin(i, i+1)
        odd = checkPalin(i, i+2)
        answer = max(answer, even, odd, key=len)
    
    return answer 

s = "babad"
print(solution(s))