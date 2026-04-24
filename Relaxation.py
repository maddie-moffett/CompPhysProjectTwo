import copy
import pylab

def calcpoint(allvals, x, y, a):

    leni = len(allvals) - 1
    
    if (x == 0) or (y == 0) or (x == leni) or (y == leni):                # walls have 0 potential
        return 0
    elif (( y >= leni//4) and (y <= 3*leni//4)) and (x == (leni // 3)):   # left plate is neg 1 voltage
        return -1
    elif (( y >= leni//4) and (y <= 3*leni//4)) and (x == (2*leni // 3)): # right plate is pos 1 voltage
        return 1
    else:                                                                             # calc and return intermediary points
        return (1/4) * (allvals[y][x + 1] + allvals[y][x - 1] + allvals[y + 1][x] + allvals[y - 1][x])

def ItThrough(boxvals, target, a):
    bvals = copy.deepcopy(boxvals) # make a copy of the matrix
    noxvals = []                   # empty array for new matrix
    delta = 1                      # starting differenc enot super important bc change almost immediately

    n = 0                          # track number of iterations

    while delta > target:          # while loop until reach target accuracy

        delta = 0                  # reset delta

        for i in range(len(bvals)):                    # for loop iterate through rows
            noxvals.append([])                         # add new row to new matrix
            for j in range(len(bvals[i])):             # iterate through columns
                newent = calcpoint(bvals, j, i, a)     # calculate value at this location
                noxvals[i].append(newent)              # add it to the correct row
                delta = max(delta, abs(bvals[i][j] - newent)) # update delta as needed
        
        bvals = copy.deepcopy(noxvals)                 # make new matrix main matrix
        noxvals = []                                   # reset the new matrix
        n += 1                                         # increment number of iterations
    return bvals, n                                    # return the new matrix

def draw(bvals):
    pylab.imshow(bvals) # make the density plot
    pylab.gray()        # black to white scale
    pylab.show()        # show it

def Relaxation(N = 100, target = 10**(-6), slen = 1, guessV = 0, drawit = True):

    a = slen / N                     # length of each segment

    boxvals = []                     # empty array for the 
    for m in range(N):               # add rows
        boxvals.append([])
        for n in range(N):           # add columns
            boxvals[m].append(guessV)   
 
    tableVals, n = ItThrough(boxvals, target, a)
    if drawit:
        draw(tableVals)
    return n

if __name__ == "__main__":
    Relaxation()