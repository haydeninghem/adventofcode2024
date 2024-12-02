import os 
def safe_report_check_pd(parts):
    for i in range(len(parts)):
        pd_list = parts[:i] + parts[i+1:]

        res = safe_report_check(pd_list)

        if res == 1:
            return 1




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
                return False
            desc = True
        
        elif (prev < part) and (desc == None or desc == False):           
            if abs(prev - part) > 3:
                return False 
            desc = False
        else:
            return False
        prev = part

    #print(parts,'Safe')
    return 1



folder_name = "P"
file_name = "2_p.txt"
file_path = os.path.join(folder_name, file_name)
safe_report_count = 0 
with open(file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(' ')
        res = safe_report_check(parts)
        print(parts,res)
        if res is False:
            res = safe_report_check_pd(parts)
        if res == 1:
            safe_report_count += res


        

print(safe_report_count)