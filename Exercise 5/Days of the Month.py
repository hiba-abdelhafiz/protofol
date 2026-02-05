months = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

month_num = int(input("Enter month number (1-12): "))

if 1 <= month_num <= 12:
    if month_num == 2:
        leap = input("Is it a leap year? (yes/no): ")
        if leap.lower() == "yes":
            print("February has 29 days")
        else:
            print("February has 28 days")
    else:
        print("Number of days:", months[month_num])
else:
    print("Invalid month number!")
