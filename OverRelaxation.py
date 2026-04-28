import copy
import pylab

def calcpoint(allvals, x, y, w, dist = 3):

    leni = len(allvals) - 1                     # leni is max index
    negposi = (leni * (dist//2)) // dist        # negative plate position calculation
    posposi = (leni * ((dist//2) + 1)) // dist  # positive plate position calculation
    
    if (x == 0) or (y == 0) or (x == leni) or (y == leni):            # walls have 0 potential
        return 0
    elif (( y >= leni//4) and (y <= 3*leni//4)) and (x == negposi):   # left plate is neg 1 voltage
        return -1
    elif (( y >= leni//4) and (y <= 3*leni//4)) and (x == posposi):   # right plate is pos 1 voltage
        return 1
    else:                                                                 # calc and return intermediary points
        newguess = (1/4) * (allvals[y][x + 1] + allvals[y][x - 1] + allvals[y + 1][x] + allvals[y - 1][x])
        return allvals[y][x] + w*(newguess - allvals[y][x])

def ItThrough(boxvals, target, w, dist = 3):
    bvals = copy.deepcopy(boxvals) # make a copy of the matrix
    delta = 1                      # starting difference not super important bc change almost immediately

    n = 0                          # track number of iterations

    while delta > target:          # while loop until reach target accuracy

        delta = 0                  # reset delta at the start of each pass through

        for i in range(len(bvals)):                    # for loop iterate through rows
            for j in range(len(bvals[i])):             # iterate through columns
                newent = calcpoint(bvals, j, i, w, dist)      # calculate value at this location
                delta = max(delta, abs(bvals[i][j] - newent)) # compare and update delta as needed
                bvals[i][j] = (newent)                 # add new val to the correct row
        
        n += 1                                          # increment number of iterations
    
    return bvals, n                                     # return the new matrix

def draw(bvals):
    pylab.imshow(bvals) # make the density plot
    pylab.gray()        # black to white scale
    pylab.show()

def OverRelaxation(w, N = 100, target = 10**(-6), slen = 1, guessV = 0, drawit = True, giveb = False, dist = 3):

    boxvals = []                     # empty array for the 
    for m in range(N):               # add rows
        boxvals.append([])
        for n in range(N):           # add columns
            boxvals[m].append(guessV)   
 
    tableVals, n = ItThrough(boxvals, target, w, dist) # iterate through and calculate vals
    if drawit:            # if draw, then draw
        draw(tableVals)
    if giveb:             # if return the table vals, return that
        return tableVals
    return n              # if not return table vals, return n