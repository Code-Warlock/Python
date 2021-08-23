try:
    array = []
    length = int(input("Enter the length of the array"))
    if length > 0:
        for each in range(1,length+1):
                item = input("Enter the item")
                array.append(item)
    print(array )
except ValueError:
    print("Please enter an Integer Value!")