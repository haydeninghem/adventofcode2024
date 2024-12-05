import os 
import itertools



def follows_rules(lines,fix=False):
    rule_len = len(lines)
    for i,rule in enumerate(lines):
        for j in range(i+1,rule_len,1):
            key = f'{lines[i]}|{lines[j]}'
            if rules.get(key) != 1 and fix is False:
                return 0

    return int(lines[rule_len // 2])



        
folder_name = "P"
file_name = "5_p.txt"
file_path = os.path.join(folder_name, file_name)
res = 0 
rules = {}
with open(file_path, 'r') as file:
    for line in file:
        if ',' in line :
            line = line.strip().split(',')
            res += follows_rules(line)
        else:
            rules[line.strip()] = 1

print(res)

