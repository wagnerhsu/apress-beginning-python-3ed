try:
    x = int(input('Enter a number: '))
    y = int(input('Enter another number: '))
    print(x / y)
except (ZeroDivisionError, ValueError) as e:
    print('Invalid input:', e)
except:
    print('Something went wrong')
finally:
    print('This always executes')