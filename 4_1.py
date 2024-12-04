import os 

folder_name = "P"
file_name = "4_p.txt"
file_path = os.path.join(folder_name, file_name)
res = 0 
md = []
with open(file_path, 'r') as file:
    for line in file:
        md.append(line.strip())

def check_mas(i,j):
    rows = len(md)
    cols = len(md[0]) if rows > 0 else 0
    try:
        if (
        0 <= i - 1 < rows and 0 <= i + 1 < rows and
        0 <= j - 1 < cols and 0 <= j + 1 < cols
        ):
            if md[i-1][j-1] == 'M' and md[i-1][j+1] == 'M' and md[i+1][j-1] == 'S' and md[i+1][j+1] == 'S':
                return 1 
            if md[i-1][j-1] == 'S' and md[i-1][j+1] == 'S' and md[i+1][j-1] == 'M' and md[i+1][j+1] == 'M':
                return 1 
            
            if md[i-1][j-1] == 'M' and md[i-1][j+1] == 'S' and md[i+1][j-1] == 'M' and md[i+1][j+1] == 'S':
                return 1
            
            if md[i-1][j-1] == 'S' and md[i-1][j+1] == 'M' and md[i+1][j-1] == 'S' and md[i+1][j+1] == 'M':
                return 1  
    except:
        return 0
    return 0


for i,line in enumerate(md): 
    for j,c in enumerate(line):
        if c == 'A':
            res+=check_mas(i,j)

            
print(res)
