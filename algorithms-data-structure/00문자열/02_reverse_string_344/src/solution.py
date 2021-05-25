def solution(strArr):
    answer = []
    L = len(strArr)
    for i in range(L):
        answer.append(strArr[L-i-1])
    return answer

print(solution(['h','e','l','l','o']))
print(solution(['H','a','n','n','a','h']))