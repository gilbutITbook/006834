import time
import random

num_of_times = 5
game_time = 25
num_of_range = 100
start_time = time.time()

for i in range(num_of_times):
    a = random.randint(1, num_of_range)
    b = random.randint(1, num_of_range)
    c = a + b
    ans = input(str(a) + '+' + str(b) + '=> ')

    if ans != c:
        print 'Sorry, wrong answer. (*x*)'
        print 'The answer is ' + str(c)
        break

    elif time.time() - start_time > game_time:
        print 'Time out! (><)'
        break

    else:
        print 'Bingo!! (^^)b'

else:
    print 'Complete!'

print('end of program')
