student_name = input('Enter Your Name:') 
student_id = int(input('Enter Your id Card Number')) 
#print(f'Student Name {student_name.title()} Student id:{student_id}') 

#print(f'Student Name {student_name.upper()} Student id:{student_id}') 

#format method 
print('Student Name:{} \nStudent id: {}'.format(student_name,student_id)) 
print('Student Name: {} \nStudent id: {}'.format(student_id,student_name))
author_names = ('k k rowling', 'rachel aaron', 'verna aadrma')

for author_name in author_names:
    print(f"Author: {author_name.title()}")


for i in range(5):
    print(i)