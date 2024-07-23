menu_card = ['Mushroom','Dal','paneer'] 
print('Available Items in menu card:', menu_card) 
#append()--> Adds an element at the end of the list 
menu_card.append('Mushroomcurry') 
print('After using append method:', menu_card) 
#Dal Tadka','Briyanni'
#extend() --> Add the elements of a list(or iterable ) 
#to the end of list  
menu_card.extend(['Dal Tadka', 'Briyani']) 
print('Using Extend method:',menu_card)

menu_card.extend('Dal Tadka') 
print(menu_card)


#insert --> Adds an element at the specified position 
menu_card.insert(1,'vegBiryani') 
print('Using Insert method:',menu_card)

#remove() method -> will remove specified value 
menu_card.remove('Dal Tadka') 
print('using Remove Method:',menu_card)

#pop() method -> remove element of specified position of the element 
menu_card.pop(2) 
print('Using pop method:',menu_card)