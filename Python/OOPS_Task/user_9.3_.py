# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored 
# in a user profile. Make a method called describe_user() that prints a summary 
# of the user’s information. Make another method called greet_user() that prints 
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods for each user

class User:
    def __init__(self):
        self.first_name=input('Enter your firstname : ')
        self.last_name=input('Enter your lastname : ')
        self.email=input('Enter your Email : ')
        self.empid=int(input('Enter your Employee ID : '))
        self.phoneno=int(input('Enter your Phone Number : '))
        self.address=input('Enter your Address : ')
    def describe_user(self):
        print(f'User Details : \nFirst_name: {self.first_name} \nLast_Name: {self.last_name} \nEmail: {self.email} \nEmployee ID : {self.empid} \nPhone: {self.phoneno} \nAddress: {self.address}')
    def greet_user(self):
        print(f'Hi {self.first_name}{self.last_name} We Welcome you to the Changepond Technologies')

User1=User()
User1.describe_user()
User1.greet_user()
User2=User()
User2.describe_user()
User2.greet_user()
User3=User()
User3.describe_user()
User3.greet_user()
User4=User()
User4.describe_user()
User4.greet_user()
        







