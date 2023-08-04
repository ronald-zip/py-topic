# Solve problem Frizz Buzz
# Imprimir en pantalla la palabra Frizz cuando un numero sea multiplo de 3, Buzz cuando sea multiplo de 5 y FrizzBuzz cuando sea multiplo de 15

def FrizBuzz():
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

FrizBuzz()