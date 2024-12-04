import os 
xmas_len = len('XMAS')
XMAS = 'XMAS'


def horz(i,j):
    str = ''
    for k,x in zip(range(j,j + xmas_len,1),range(0,xmas_len)):
        try:
            if md[i][k] == XMAS[x] and k > -1:
                str +=md[i][k]
            else:
                return 0
        except:
            return 0       
    return 1

def bkwd(i,j):
    str = ''
    for k,x in zip(range(j, j - xmas_len, -1),range(0,xmas_len)):
        try:
            if md[i][k] == XMAS[x] and k > -1:
                str +=md[i][k]
            else:
                return 0
        except:
            return 0     
 
    return 1



def up(i,j):
    str = ''
    for k,x in zip(range(i, i - xmas_len, -1),range(0,xmas_len)):
        try:
            if md[k][j] == XMAS[x] and k > -1:
                str +=md[k][j]
            else:
                return 0
        except:
            return 0     

    return 1
   
def down(i,j):
    str = ''
    for k,x in zip(range(i, i + xmas_len, 1),range(0,xmas_len)):
        try:
            if md[k][j] == XMAS[x] and k > -1:
                str +=md[k][j]
            else:
                return 0
        except:
            return 0     

    return 1



def rightupdiag(i,j):
    str = ''
    for k,z,x in zip(range(i, i - xmas_len, -1),range(j, j + xmas_len, 1),range(0,xmas_len)):
        try:
            if md[k][z] == XMAS[x] and z > -1 and k > -1:
                str +=md[k][z]
            else:
                return 0
        except:
            return 0     
    print(md[i],i,j)
    return 1

def leftupdiag(i,j):
    str = ''
    for k,z,x in zip(range(i, i - xmas_len, -1),range(j, j - xmas_len, -1),range(0,xmas_len)):
        try:
            if md[k][z] == XMAS[x] and z > -1 and k > -1:
                #print(k,z)
                str +=md[k][z]
            else:
                return 0
        except:
            return 0     
    print(md[i],i,j)
    return 1


def leftdowndiag(i,j):
    str = ''
    for k,z,x in zip(range(i, i + xmas_len, 1),range(j, j - xmas_len, -1),range(0,xmas_len)):
        try:
            if md[k][z] == XMAS[x] and z > -1 and k > -1:
                str +=md[k][z]
            else:
                return 0
        except:
            return 0     

    return 1

def rightdowndiag(i,j):
    str = ''
    for k,z,x in zip(range(i, i + xmas_len, 1),range(j, j + xmas_len, 1),range(0,xmas_len)):
        try:
            if md[k][z] == XMAS[x] and z > -1 and k > -1:
                str +=md[k][z]
            else:
                return 0
        except:
            return 0     
 
    return 1

folder_name = "P"
file_name = "4_p.txt"
file_path = os.path.join(folder_name, file_name)
res = 0 
md = []
with open(file_path, 'r') as file:
    for line in file:
        md.append(line.strip())



for i,line in enumerate(md): 
    for j,c in enumerate(line):
        if c == 'X':
            
            res+=horz(i,j)
            res+=bkwd(i,j)

            res+=up(i,j)
            res+=down(i,j)

            res+=rightupdiag(i,j)
            res+=leftupdiag(i,j)

            res+=leftdowndiag(i,j)
            res+=rightdowndiag(i,j)

print(res)
