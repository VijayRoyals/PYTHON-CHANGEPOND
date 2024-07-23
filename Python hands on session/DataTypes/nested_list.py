nested_list = ['Vijay','Kumar',[25,25],[True,False]] 

print(nested_list[0]) 
print(nested_list[1]) 
print(nested_list[2][0]) 
print(nested_list[3][0]) 







nested_list = (['Vijay', 'Kumar'], [25, 25], (True, False))


first_list = nested_list[0]
second_list = nested_list[1]
tuple_element = nested_list[2]


first_name = nested_list[0][0]      
second_integer = nested_list[1][1]   
second_boolean = nested_list[2][1]   

print("First list:", first_list)
print("Second list:", second_list)
print("Tuple element:", tuple_element)
print("First name:", first_name)
print("Second integer:", second_integer)
print("Second boolean:", second_boolean)
