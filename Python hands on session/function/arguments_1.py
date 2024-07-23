def main(): 
    # #postional Argument 
    Output_1 = Area(10,12) 
    print('Area of Circle:', Output_1) 
    # first aargument is positional and second is default 
    Output_1 = Area(10) 
    print('Area of Circle:', Output_1) 
    
    
    #Keyword argument 
    Output_2 = Area(PI=3,Radius=12) 
    print('Area of Circle:', Output_2) 
    #Keyword argument and second is default 
    Output_2 =Area(Radius-12) 
    print('Area of circle:', Output_2) 
if __main__ =="__main__": 
    main() 
    
    
    
    
    
    
    
    