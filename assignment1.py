# main memory
d = {}

# PC incrementing after each iteration
for i in range(4):
    print('memory: ',d)
    interrupt = input("Would you like to issue an interrupt? ")

    if interrupt == 'yes':
        val = int(input('Enter a value:'))
        # updating main memory
        d[i]=val
    