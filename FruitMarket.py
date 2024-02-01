


prices = {}
stock = {}

while(1):
        op = int(input("Menu\n1. Add Fruit\n2. Buy Fruit\n3. View Inventory\n4. Update Price\n5. Update Stock\n6. Exit\n"))
        if(op == 6):
                break
        elif(op == 1):
                fnm = input("Enter name of the fruit here : ")
                fst = int(input("Enter stock of the fruit here : "))
                fpr = int(input("Enter price per kg here : "))

                prices[fnm] = fpr
                stock[fnm] = fst
                print("Fruit Added Successfully!")		
        
        elif(op == 2):
                  sell = input("Enter name of the fruit here: ")
                  
                  if sell in stock and prices:
                    qua = int(input("Enter quantity here: "))
                    if(qua<stock[sell]):
                       stock[sell] -= qua
                       print("price is ",qua*prices[sell])
                       print("Fruit sale successful!!")
                    else:
                       print("insufficient stock")
                  else:
                     print("Fruit not found in stock.")

        elif (op == 3):
                for fruit in prices:
                    print("Fruit name:", fruit)
                    print("Price:", prices[fruit])
                    if fruit in stock:
                        print("Stock:", stock[fruit])
                    else:
                        print("Stock: 0")

        elif(op == 4):
           up=input("Enter fruit name:")
           if up in prices and stock:
              new=input("Enter new price here: ")
              prices[up]=new
              print("price updated successful!!")
           else:
               print("Fruit not found in stock.")

        elif(op == 5):
           us=input("Enter fruit name:")
           if us in prices and stock:
              y=int(input("Enter new stock here: "))
              stock[us]=stock[us]+y
              print("stock updated successful!!")
           else:
                    print("Fruit not found in stock.")
            
              
        elif(op == 6):
                break
        else:
                print("Invalid Choice")
