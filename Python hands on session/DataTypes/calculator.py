import arithmetic

print('Choose operation')
print('1.Addition\n2.Subtration\n3.Multiplication')
select = int(input('Select 1/2/3'))

def main():
    num01 = int(input('Enter 1st num : '))
    num02 = int(input('Enter 2nd num : '))

    if(select == 1):
        Ans = arithmetic.Addition(num01,num02)
        print(f'Addition {num01} and {num02}:',Ans)
    elif(select == 2):
        Ans = arithmetic.Subtraction(num01,num02)
        print(f'Subtration {num01} and {num02}:',Ans)
    elif(select == 3):
        Ans = arithmetic.Multiplication(num01,num02)
        print(f'Mutiplication {num01} and {num02}:',Ans)
    else:
        print('choose 1/2/3')
if __name__ == '__main__':
    main()