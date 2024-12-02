import os

def safe_report_check(parts):
    prev = None 
    desc = None 
    for part in parts:
       
        if prev is None:
            prev = part
            continue
        
        prev = int(prev)
        part = int(part)

    
        if (prev > part) and (desc == None or desc == True) :

            if abs(prev - part) > 3:
                return 0 
            desc = True
        
        elif (prev < part) and (desc == None or desc == False):
            
            if abs(prev - part) > 3:
                return 0 
            desc = False
        else:
            return 0
    
        prev = part

    print(parts,'Safe')
    return 1
       

folder_name = "P"
file_name = "2_p.txt"
file_path = os.path.join(folder_name, file_name)
safe_report_count = 0 
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        safe_report_count += safe_report_check(parts)

print(safe_report_count)
  




