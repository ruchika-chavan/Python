while(1):
        type = int(input("Menu\n1. Multiplication Table\n2. Factorial\n3. Fibonacci sequence\n4. Exit\n"))
        if(type == 1):
            n = int(input("Enter number here :"))
            for i in range(1, 11):
                print(n,"x",i,"=",n*i)
        elif(type == 2):
                
                while(1):
                    f = 1
                    n = int(input("Enter first number here :"))
                    if(n == 0):
                        print("Factorial = 1")
                    else:
                        for i in range(1, n+1):
                            f = f*i
                        print("Factorial =",f)
        elif(type == 3):
                n1 = 0
                n2 = 1
                num = int(input("Enter Number of Elements: "))
                print("\n", n1, n2,end="\t")

                for i in range(2, num):
                         n3 = n1 + n2
                         print(n3,end="\t")
                         n1 = n2
                         n2 = n3
                         

        elif(type == 4):
                break
        else:
                print("Invalid Operator")
