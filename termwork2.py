termwork = {}  # Assuming you have this dictionary defined somewhere in your code

while True:
    op = int(input("\nMenu:\n1. Enter Heads\n2. Display Records\n3. Calculate Total and Average Marks\n4. Exit\n"))

    if op == 4:
        break
    elif op == 1:
        hd = 1
        hnm = input("\nEnter name of head here: ")

        for i in range(hd):
            ent = int(input("\nEnter no. of entries here: "))
            print("\n")
            hmk = []
            termwork[hnm] = hmk
            for i in range(ent):
                m = int(input("Enter mark here (max 10): "))
                if m > 10:
                    print("Invalid input. Maximum marks allowed is 10.")
                    m = 10  # Set the mark to the maximum allowed value
                termwork[hnm].append(m)

    elif op == 2:
        for i in termwork:
            print("Head:", i)
            print("Marks:", termwork[i])
    elif op == 3:
        total_marks = 0
        total_entries = 0

        for head, marks in termwork.items():
            head_total = sum(marks)
            head_average = head_total / len(marks) if len(marks) > 0 else 0  # Avoid division by zero
            total_marks += head_total
            total_entries += len(marks)

            print("Head:", head)
            print("Total Marks:", head_total)
            print("Average Marks:", head_average)
            print("Marks:", marks)
            print("\n")

        overall_average = total_marks / total_entries if total_entries > 0 else 0  # Avoid division by zero
        print("Overall Total Marks:", total_marks)
        print("Overall Average Marks:", overall_average)

    else:
        print("Invalid Choice!")
