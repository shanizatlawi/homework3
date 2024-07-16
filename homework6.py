id_input1 = input("Enter first user's id:")
first_name1 = input("Enter first user's first name")
last_name1 = input("Enter first user's last name:")
height1 = float(input("Enter first user's heigt (in meters):"))
birth_year1 = int(input("Enter first user's birth year:"))

id_input2 = input("Enter second user's id:")
first_name2 = input("Enter second user's first name")
last_name2 = input("Enter second user's last name:")
height2 = float(input("Enter second user's heigt (in meters):"))
birth_year2 = int(input("Enter second user's birth year:"))

print(f"{id_input1:<5} {last_name1[:10]:<10} {first_name1[:10]:<10} {height1:.2f} {birth_year1:<15}")
print(f"{id_input2:<5} {last_name2[:10]:<10} {first_name2[:10]:<10} {height2:.2f} {birth_year2:<15}")