#creating a list:
#creating same data type 
course =['Python', 'Java', 'C'] #String 
#we can create string data type also 
rollno = [123,124,125] #integer datatype 

#creating mixed type 
mixed_type = ['Vijay', 63053,True,25.5] 
print('Heterogenus:' ,mixed_type) 
print('Length:',len(mixed_type))
print('Access value of vijay:',mixed_type[0]) 
print('Access value of 63053',mixed_type[1])
print('Access value of  True',mixed_type[2]) 
print('Access the value of 25.5',mixed_type[3])




courses = ['Python', 'Java', 'C']  
roll_numbers = [123, 124, 125]  


mixed_type = ['Vijay', 63053, True, 25.5]  


print('Mixed Type List:', mixed_type)
print('Length of the list:', len(mixed_type))


print('Access value at index -1 :', mixed_type[-1])
print('Access value at index -2 :', mixed_type[-2])
print('Access value at index -3 :', mixed_type[-3])
print('Access value at index -4 :', mixed_type[-4])




mixed_type = ['Vijay', 63053, True, 25.5, 'John', 12345, False]

slice1 = mixed_type[-3:]  
slice2 = mixed_type[-5:-2] 

print('Slice 1:', slice1)
print('Slice 2:', slice2)

#


fruits = ['Mango', 'Banana', 'Grapes', 'Watermelon']

fruits[1] = 'Kiwi'
print('After replacing Banana with Kiwi:', fruits)

del fruits[3]
print('After removing Watermelon:', fruits)

sliced_fruits = fruits[:2]
print('Sliced to get Mango and banana:', sliced_fruits)
