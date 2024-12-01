import os


folder_name = "P"
file_name = "1_p.txt"
file_path = os.path.join(folder_name, file_name)

left_list = []
right_list = []
with open(file_path, 'r') as file:
    for line in file:
            # Strip whitespace and split the line by spaces
        parts = line.strip().split('   ')
        # Add the parts to respective lists
        if len(parts) == 2:  # Ensure there are two parts
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))


counter = 0 
for loc_id in left_list:
    counter += loc_id * right_list.count(loc_id)
print(counter)


