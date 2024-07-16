pizza_num: int = int(input("please enter a number of pizza slices:"));
if pizza_num % 4 == 0:
    print(f"Each friend received {pizza_num // 4} slice of pizza, and no more slices remained.");
else:
    print(f"Each friend received {pizza_num // 4} slice of pizza, and {pizza_num % 4} more slices remained.");


##############################################3
pizza_num: int = int(input("please enter a number of pizza slices:"));
friends_num: int = int(input("please enter a number of friends:"));
if pizza_num % friends_num == 0:
    print(f"Each friend received {pizza_num // friends_num} slice of pizza, and no more slices remained.");
else:
    slices_remain: int = pizza_num % friends_num;
    print(f"Each friend received {pizza_num // friends_num} slice of pizza, and {slices_remain} more slices remained.");
