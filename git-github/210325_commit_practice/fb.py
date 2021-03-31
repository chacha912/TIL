def do_fizzbuzz(num):
    result = [
        'fizzbuzz' if i%15==0 else
        'fizz' if i%3==0 else
        'buzz' if i%5==0 else
        i for i in range(1,num+1)
    ]
    print(result)
if __name__=='__main__':
    user_num = int(input('Type the number: '))
    do_fizzbuzz(user_num)