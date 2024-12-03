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


mul_pattern = re.compile(r"mul\(\s*\d+\s*,\s*\d+\s*\)")
do_pattern = r"\b\w*do\(\)"
dont_pattern = r"\bdon't\(\)"

do_matches = re.finditer(do_pattern, input)
dont_matches = re.finditer(dont_pattern, input)
func_calls = re.finditer(mul_pattern, input)

stack = {}

for func_calls in func_calls:
    stack[func_calls.end()] = func_calls.group()

for dont_matches in dont_matches:
    stack[dont_matches.end()] = False 

for do_matches in do_matches:
    stack[do_matches.end()] = True 


do = True 
for key in sorted(stack.keys()):
    val = stack[key]
    print(f"{key}: {stack[key]}")

    if isinstance(val, bool):
        do = val
        continue 

    if do is True:
        res += eval(val, {"__builtins__": None}, {'mul': mul})


print(res)
