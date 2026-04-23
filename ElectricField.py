import copy
import pylab

e0 = 1            # emissivity constant
target = 10**(-6) # target accuracy
guessV = 0        # starting guess for intermediate voltages
slen = 1          # length of side one decimeter
snum = 100        # number of divisions per side
a = slen / snum   # length of each segment

boxvals = []                        # empty array for the 
for m in range(snum):               # add rows
    boxvals.append([])
    for n in range(snum):           # add columns
        boxvals[m].append(guessV)    


def calcpoint(allvals, x, y, w):
    p = 0 # no charge densities here
    
    if (x == 0) or (y == 0) or (x == (len(allvals[y]) - 1)) or (y == (len(allvals) - 1)): # walls have 0 potential
        return 0
    elif (( y * a >= 0.2) and (y * a <= 0.8)) and (x * a == 0.2):                         # left plate is pos 1 voltage
        return 1
    elif (( y * a >= 0.2) and (y * a <= 0.8)) and  x * a == 0.8:                          # right plate is neg 1 voltage
        return -1
    else:                                                                                 # calc and return intermediary points
        return (1/4) * (allvals[y][x + 1] + allvals[y][x - 1] + allvals[y + 1][x] + allvals[y - 1][x]) + ((w**2) / (4*e0)) * p

def Poise():
    bvals = copy.deepcopy(boxvals) # make a copy of the matrix
    noxvals = []                   # empty array for new matrix
    delta = 1                      # starting differenc enot super important bc change almost immediately


    while delta > target:           # while loop until reach target accuracy

        for i in range(len(bvals)):                  # for loop iterate through rows
            noxvals.append([])                       # add new row to new matrix
            for j in range(len(bvals[i])):           # iterate through columns
                newent = calcpoint(bvals, j, i, a)   # calculate value at this location
                noxvals[i].append(newent)            # add it to the correct row
                if (i == 0) and (j == 0):            # if at the start, overwrite delta automatically
                    delta = abs(bvals[i][j] - newent)
                else:                                # else compare and update delta as needed
                    delta = max(delta, abs(bvals[i][j] - newent))
        
        bvals = copy.deepcopy(noxvals)               # make new matrix main matrix
        noxvals = []                                 # reset the new matrix
    
    return bvals                                     # return the new matrix

def draw(bvals):
    pylab.imshow(bvals) # make the density plot
    pylab.gray()        # black to white scale
    pylab.show()        # show it

if __name__ == "__main__":
    draw(Poise())       # call!