num = 1

while num != 0:

    num = int ( input ("\nDime un factorial a calcular\n"))
    print("\nFactorial de",num)
    print("\n 0 ! = 1")
    print("\n 1 ! = 1")
    
    for i in range(2,num+1):
        
        print("\n",i,"! =",i,flush=True,end=" ")    
        
        for j in range(i-1,1,-1):
            
            print("*",j,flush=True,end=" ")
        
        print("* 1")