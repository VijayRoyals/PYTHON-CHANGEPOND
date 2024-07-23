#While loop is used to execute a block of statements repeatedly until the given condition is true or satisfy 
#when the condition becomes false , the line immediately after the loopin the given program is executed 
#Syntax: 
#While(expression): 
    #loop body 
    
    
    
count = 0 
while(count<6):
    print(count)
    count +=1
        
        
ice_cream = ['Vanilla', 'choco-chips', 'strawberry', 'blackcurrent', 'dark Chocolate', 'pista']
index = 0
while index < len(ice_cream):
    result= ice_cream[index]
    print(result)
    index += 1



student_names = ("vijayroyals", "SateeshChowdary", "pawankalyan", "ramcharan", "chiranjeevi")


i = 0


length = len(student_names)

while i < length:
    print(student_names[i])
    i += 1  
