
def staff_info():
    name = input("Enter your name: ")
    print("Hello,", name)


def requisitions_total():
    staff_info()
    
    total = 0
    while True:
        item = input("Enter item name (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        price = input("Enter item price: $")
        total = total + float(price)
    
    print("Total cost: $" + str(total))


requisitions_total()
