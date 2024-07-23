#Create a Tuple 
#Homogenous 
student_id = (123,124,125,126) 
ice_cream = ('Chocolate', 'choco-chips', 'BlackCurrent') 

#Heterogenous 
mixed_type = (123, 'Hello', False, 56.78) 
#len() 
#using index ==> BlackCurrent(positive) 
#using index ==> False(Negative index) 
#using slicing ==> 'Hello', False  


print(ice_cream[2])  
print(mixed_type[-2])
sliced_elements = mixed_type[1:3]
print(sliced_elements) 




ice_cream = ('vanilla') #str 
print(ice_cream,type(ice_cream)) 
ice_cream = ('Vanilla',) #comma 
print(ice_cream,type(ice_cream))



ice_cream = ('Vanilla' ,'Choco-chips','Blueberry','Vanilla') 
count_method = ice_cream.count('Vanilla') 
print(count_method) 

indexmethod = ice_cream.index('Vanilla') 
print(indexmethod)