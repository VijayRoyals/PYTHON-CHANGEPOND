import os
import filecmp

def Comparefiles(filename_01,filename_02):
    if(not os.path.exists(filename_01)):
        print('Not Exists : ',filename_01)
    elif(not os.path.exists(filename_02)):
        print('Not Exists : ',filename_02) 
    else :
        compare = filecmp.cmp(filename_01,filename_02)
        if compare == True :
            print('Success -> The files are same ')

        else : 
            print('Failure -> Files are different')

def main():
    file_01 = input('Enter the first file name : ')
    file_02 = input('Enter the second file name : ')
    Comparefiles(file_01,file_02)


if __name__ == '__main__':
    main()
