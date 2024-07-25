#using list comprehension creating a  list of  square numbers 
#new_list = [expression for member in iterable] 
#new_list = [expression for member in iterable if(optional)] 

new_list = [i for i in range(1, 11)] 
print('List Compreshsion', new_list) 

new_list = [i for i in range(1,11) if(i%2==0)] 
print('List Comprehsion:', new_list) 

#Task: Take example of your name and filter out vowels from the name
name = "vijay kumar"
vowels = ['a', 'e', 'i', 'o', 'u'] 

filtered_name = [letter for letter in name if letter.lower() not in vowels]

print("Original Name:", name)
print("Name without vowels:", ''.join(filtered_name))
