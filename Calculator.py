while True:
    try:
        a = float(input('Enter 1st Number:'))
        f = float(input('Enter 2nd Number:'))
        b = input('Enter Symbol To Do Calculations-')
        from Refrence_File import Calculator as A
        if b == '+':
            print(A.add(a,f))
        elif b == '-':
            print(A.sub(a,f))
        elif b == '/':
            print(A.div(a,f))
        elif b == '*':
            print(A.mul(a,f))
    except Exception as msg:
        print('Error -',msg)
        break
