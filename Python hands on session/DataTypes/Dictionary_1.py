Watch_details= {
    'Titan':8000, 
    'Fastract':5000, 
    'Omega':9000
 } 
print('length of the dictionary: ', len(Watch_details)) 
print('Type:', type(Watch_details)) 

print('Using key',Watch_details['Titan'])
print('-'*50) 
Watch_details ={
    'Titan'   
}




# Example of a nested dictionary
nested_dict = {
    'person1': {
        'name': 'VIJAY KUMAR',
        'age': 22,
        'city': 'tirupathi'
    },
    'person2': {
        'name': 'sateesh chowdary',
        'age': 25,
        'city': 'chittoor'
    },
    'person3': {
        'name': 'raghul',
        'age': 35,
        'city': 'Madurai',
        'children': {
            'child1': {
                'name': 'vijay',
                'age': 5
            },
            'child2': {
                'name': 'kumar',
                'age': 8
            }
        }
    }
}


print(nested_dict['person1']['name'])  
print(nested_dict['person3']['children']['child2']['name'])  


nested_dict['person2']['age'] = 26
print(nested_dict['person2']['age'])  


nested_dict['person1']['job'] = 'Engineer'
print(nested_dict['person1']) 


for person, details in nested_dict.items():
    print(f"Person: {person}")
    for key, value in details.items():
        print(f"{key}: {value}")
    print()
    
    
    
# Accessing 'VIJAY KUMAR'
name_person1 = nested_dict['person1']['name']
print("Access:", name_person1) 

# Accessing 'tirupathi'
city_person1 = nested_dict['person1']['city']
print("Access:", city_person1)  # Output: Access: tirupathi





  