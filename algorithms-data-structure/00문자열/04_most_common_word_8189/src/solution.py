import collections
import re

def solution(paragraph, banned):

    counts = collections.defaultdict(int)
    words = re.sub('[^a-zA-Z]', ' ', paragraph).lower().split()
    banned = set(banned)

    for word in words:
        if word not in banned:
            counts[word] += 1

    return max(counts, key=counts.get)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(solution(paragraph, banned))
