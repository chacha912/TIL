import collections

def solution(paragraph, banned):
    # 1). replace the punctuations with spaces,
    #     and put all letters in lower case
    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

    # 2). split the string into words
    words = normalized_str.split()

    word_count = collections.defaultdict(int)
    banned_words = set(banned)

    # 3). count the appearance of each word, excluding the banned words
    for word in words:
        if word not in banned_words:
            word_count[word] += 1

    # 4). return the word with the highest frequency
    return max(word_count.items(), key=lambda x: x[1])[0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(solution(paragraph, banned))