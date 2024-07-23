def count(list,num):
    count = 0
    for i in list:
        if(i == num):
            count += 1
    return count
def main():
    #dynamic input
    print('Enter the size of the list : ')
    size = int(input())
    data_input = []
    print('Enter the Value : ')
    for i in range(size):
        value = int(input())
        data_input.append(value)
    print('User List : ',data_input)
    searchnum = int(input('Enter the number to be count : '))
    print(searchnum, "is repeating ",count(data_input,searchnum),"times")
if __name__ ==  '__main__':
    main()
