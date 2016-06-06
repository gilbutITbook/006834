import time
times = 3

try:
    for i in range(times):
        for j in [' __(.)= __(.)> __(.)< ~P',\
                  '\___)  \___)  \___) ',\
                  '  ))     ))     )) ']:

            print j
            time.sleep(0.1)

except KeyboardInterrupt:
    print 'Keyboard Interrupt!!'
        
else:
    print 'complete ' + str(times) + ' times!'

finally:
    print 'end of program'
