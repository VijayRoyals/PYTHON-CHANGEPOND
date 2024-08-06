import datetime
today = datetime.date.today() 
year = today.year
print(year)
# try: 
#     num1 = int(input("Enter the number 1: ")) 
#     num2 = int(input("Enter the number 2: ")) 
#     result =  num1/num2 
#     print(result) 
# except ZeroDivisionError: 
#     print("Error: Denomintor cannot be zero")
# except ValueError: 
#     print("Error: Only numbers are allowed")

try:
    items = ["Bread", "Butter", "Jam", "Cheese"] 
    # items[len(items)] = "Spread" 
    num1 = int(input("enter the number 1:")) 
    assert num1%2==0
except ZeroDivisionError: 
    print("Error: Denominator cannot  be Zero") 
except ValueError: 
    print("Only numbers are allowed") 
except IndexError: 
    print("Kindly use insert or append method") 
except AssertionError: 
    print("Entered value is not matching the testcondition")
else: 
    print(num1, "is even")
finally: 
    print("program is over")


yob = int(input("Enter Your Year Of Birth: ")) 
age = year - yob 
if(age < 18): 
    raise Exception(f'The age should be above 18 years and your age is less than 19')
print(age)