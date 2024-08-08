# 5)Write a program which contains one class named as Numbers.
# Arithmetic class contains one instance variables as Value.
# Inside init method initialize that instance variables to the value which is accepted from user.
# There are four instance methods inside class as ChkPrime(), ChkPerfect() , SumFactors(), Factors().
# ChkPrime() method will returns true if number is prime otherwise return false
# ChkPerfect () method will returns true if number is perfect otherwise return false.
# Factors () method will display all factors of instance variable.
# SumFactors() method will return addition of all factors. Use this method in any another method
# As a helper method if required.
# After Designing the above class call all instance methods by creating multiple objects.
class Numbers:
    def __init__(self,value):
        self.value = value

    def ChkPrime(self):

        if self.value <= 1:
            print(f'{self.value} is a Composite Number')
        else:
            for i in range(2, (self.value//2)+1):
                if (self.value % i) == 0:
                    print(self.value, "is not a prime number")
                    break
            print(self.value, "is a prime number")
    def ChkPerfect(self):
        sum = 0
        for i in range(1,self.value):
            if self.value%i == 0:
                sum += i 
        if sum == self.value :
            print(f'{self.value} is Perfect Number') 
        else:
            print(f'{self.value} is not a Perfect Number') 

    def SumFactors(self):
        sum = 0
        for i in range(1,self.value+1):
            if self.value%i == 0:
                sum += i 
        print(f'Sum Factor of {self.value} : {sum}')
    def Factors(self):
        factors=[]
        for i in range(1, self.value+1):
            if int(self.value)%i==0:
                factors.append(i) 
        print(f'Factor of {self.value} : {factors}')
def main():
    obj1 = Numbers(int(input('Enter the Number : ')))
    select = int(input('Enter the Option : \n1.Check Prime\n2.Check Perfect\n3.Sum of Factors\n4.Factors\n'))

    if(select == 1):
        obj1.ChkPrime()
    elif(select == 2):
        obj1.ChkPerfect()
    elif(select == 3):
       obj1.SumFactors()
    elif(select == 4):
        obj1.Factors()
    else:
        print('choose the correct option')
        main()
if __name__ == '__main__':
    main()