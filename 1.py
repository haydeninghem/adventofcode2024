import os


folder_name = "P"
file_name = "1_p.txt"
file_path = os.path.join(folder_name, file_name)

left_list = []
right_list = []
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split('   ')
        if len(parts) == 2:  
            left_list.append(int(parts[0]))
            right_list.append(int(parts[1]))
            
left_list.sort()
right_list.sort()
total = 0
for i in range(0,1000):
    total += abs(left_list[i] - right_list[i])
print(total)
