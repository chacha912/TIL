def test():
    print('hello')

def do_fizzbuzz(num):
    for i in range(1, num+1):
        print(i)

if __name__=='__main__':
    test()
    user_num = int(input('Type the number: '))
    do_fizzbuzz(user_num)