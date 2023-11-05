while True:
    try :
        x = int(input('Please enter int '))
        y = int(input('Please enter int '))
        result = y/x
    except ValueError :
        print('you must enter integer\n')
    except ZeroDivisionError:
        print('Zero')
    else:
        print(result)

