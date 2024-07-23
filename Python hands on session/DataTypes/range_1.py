for i in range(5):
    print(i)
for i in range(5,13): # Start = 5,stop = 12 ,13 will be exculded
    print(i)
for i in range(5,int(13/2),2): 
    print(i)


#Iterate over a string using for loop
name = "vijay"
for i in range(len(name)): 
    print(name[i])