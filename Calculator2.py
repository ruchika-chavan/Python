while(1):
        type = int(input("Menu\n1. Arithmetic\n2. Logical\n3. Bitwise\n4. Exit\n"))
        if(type == 1):
                while(1):
                        opt = int(input("Menu\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit\n"))
                        x = int(input("Enter first number here :"))
                        y = int(input("Enter second number here :"))
                        if(opt == 1):
                                print("Sum = ", x+y)
                        elif(opt == 2):
                                print("Difference = ", x-y)
                        elif(opt == 3):
                                print("Product = ", x*y)
                        elif(opt == 4):
                                if y != 0:
                                    print("Quotient =", x/y)
                                else:
                                    print("Error")
                        elif opt == 5:
                                break
                        else:
                                print("Invalid Operator")
        elif(type == 2):
                while(1):
                        opt = int(input("Menu\n1. Logical AND \n2. Logical OR\n3. Logical NOT\n4. Exit\n"))
                        x = int(input("Enter first number here :"))
                        y = int(input("Enter second number here :"))
                        z = int(input("Enter third number here :"))
                        if(opt == 1):
                                print("Result = ", x>y and x>z)
                        elif(opt == 2):
                                print("Result = ", x<y or x<z)
                        elif(opt == 3):
                                print("Result = ", not (x>y and x<z))
                        elif(op == 4):
                                break
                        else:
                                print("Invalid Operator")
        elif(type == 3):
                while(1):
                        opt = int(input("Menu\n1. Bitwise AND\n2. Bitwise OR\n3. Bitwise XOR\n4. Exit\n"))
                        x = int(input("Enter first number here :"))
                        y = int(input("Enter second number here :"))
                        if(opt == 1):
                                print("AND = ", x&y)
                        elif(opt == 2):
                                print("OR = ", x|y)
                        elif(opt == 3):
                                print("XOR = ", x^y)
                        elif(opt == 4):
                                break
                        else:
                                print("Invalid Operator")
        elif(type == 4):
                break
        else:
                print("Invalid Operator")