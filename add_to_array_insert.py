my_list = [1, 2, 3, 4, 5]
print(f'Current Numbers List {my_list}')
number = int(input("Please enter a number to be added:\n"))
index = int(input(f'Enter the index between 0 and {len(my_list) - 1} to add the given number:\n'))
my_list.insert(index, number)
print(f'Updated List {my_list}')
