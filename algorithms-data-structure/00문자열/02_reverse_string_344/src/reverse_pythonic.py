def reverseString(s):
    # s.reverse()
    # s = s[::-1]
    s[:] = s[::-1]
    print(s)

reverseString(['h','e','l','l','o'])
reverseString(['H','a','n','n','a','h'])
reverseString([0,1,2,3,5,4])