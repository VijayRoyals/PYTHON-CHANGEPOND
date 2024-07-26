#open function -> filename ,mode (r,w,a,...)
#file_read = open('calculator.py','r')
#print(file_read.read())


import os
def CreateFile(filename):
    if(os.path.exists(filename)):
        print('File alreay exists')
    else:
        file_create = open(filename,'w')

def main():
    print('Enter filename you want to create: ')
    file_name = input()

    #CreateFile(file_name)
    #file_read = open('calculator.py','r')
    file_read = open(file_name,'r')
    print(file_read.read())
if __name__=="__main__":
    main()