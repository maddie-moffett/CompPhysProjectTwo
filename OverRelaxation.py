import copy
import pylab

def calcpoint(allvals, x, y, e0, a, w):

    leni = len(allvals) - 1
    
    if (x == 0) or (y == 0) or (x == (len(allvals[y]) - 1)) or (y == leni):           # walls have 0 potential
        return 0
    elif (( y * a >= leni//4) and (y * a <= 3*leni//4)) and (x * a == (leni // 3)):   # left plate is neg 1 voltage
        return -1
    elif (( y * a >= leni//4) and (y * a <= 3*leni//4)) and (x * a == (2*leni // 3)): # right plate is pos 1 voltage
        return 1
    else:                                                                             # calc and return intermediary points
        return ((1+w)/4) * (allvals[y][x + 1] + allvals[y][x - 1] + allvals[y + 1][x] + allvals[y - 1][x]) - w*allvals[y][x]

def ItThrough(boxvals, target, e0, a, w):
    bvals = copy.deepcopy(boxvals) # make a copy of the matrix
    delta = 1                      # starting differenc enot super important bc change almost immediately


    while delta > target:          # while loop until reach target accuracy

        for i in range(len(bvals)):                    # for loop iterate through rows
            for j in range(len(bvals[i])):             # iterate through columns
                newent = calcpoint(bvals, j, i, e0, a) # calculate value at this location
                bvals[i][j] = (newent)                 # add it to the correct row
                if (i == 0) and (j == 0):              # if at the start, overwrite delta automatically
                    delta = abs(bvals[i][j] - newent)
                else:                                  # else compare and update delta as needed
                    delta = max(delta, abs(bvals[i][j] - newent))
    
    return bvals                                       # return the new matrix

def draw(bvals):
    pylab.imshow(bvals) # make the density plot
    pylab.gray()        # black to white scale
    pylab.show()        # show it

def OverRelaxation(w, N = 100, target = 10**(-6), e0 = 1, slen = 1, guessV = 0, draw = True):

    a = slen / N                     # length of each segment

    boxvals = []                     # empty array for the 
    for m in range(N):               # add rows
        boxvals.append([])
        for n in range(N):           # add columns
            boxvals[m].append(guessV)   
 
    tableVals = ItThrough(boxvals, target, e0, a, w)
    draw(tableVals)