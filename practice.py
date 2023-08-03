# Frizz Buzz

x = range(101)

for num in x:
    if num%3 == 0 and num%5 == 0:
        val = 'FrizzBuzz'
    elif num%3 == 0:
        val = 'Frizz'
    elif num%5 == 0:
        val = 'Buzz'
    else:
        val = 'None'
    print(f'{num} {val}')