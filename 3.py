import os 
import re 

def mul(x,y):
    return x * y 

folder_name = "P"
file_name = "3_p.txt"
file_path = os.path.join(folder_name, file_name)
res = 0 
with open(file_path, 'r') as file:
    input = file.read()


pattern = re.compile(r"mul\(\s*\d+\s*,\s*\d+\s*\)")


for func_calls in re.findall(pattern, input):
    print(func_calls)
    res += eval(func_calls, {"__builtins__": None}, {'mul': mul})


print(res)