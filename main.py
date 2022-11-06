import random
def merge(line):
    new_line =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4) :
        index=0
        for j in range(4) :
            if line[i][j] != 0 :
                new_line[i][index] = line[i][j]
                index += 1
        for j in range(3) :
            if new_line[i][j] == new_line[i][j+1] :
                new_line[i][j] = new_line[i][j]*2
                new_line[i][j+1] = 0
        for j in range(3) :
            if new_line[i][j] == 0 and new_line[i][j+1] != 0 :
                new_line[i][j] = new_line[i][j+1]
                new_line[i][j+1] = 0
    line=new_line
    return line