#def Addition():
#    print('Inside Addition')  #no parameter no arguments no return
#Addition()


#def Addition(value_01,value_02):
#    print('Inside Addition')
#    print('Argument 1:',value_01) 
#    print('Argument 2:',value_02)
#    print(f'{value_01} and {value_02} adition is:',value_01+value_02)
#Addition(12,13)


def Addition(value_01,value_02):
    
    print('Inside Addition')
    print('Argument 1:',value_01) 
    print('Argument 2:',value_02)
    Add = value_01+value_02
    Sub = value_02-value_01
    return Add,Sub
Result1,Result2 = Addition(12,13)
print('Addition : ',Result1)
print('Subtraction : ',Result2)