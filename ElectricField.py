from Relaxation import Relaxation
from OverRelaxation import OverRelaxation
import pylab

def PartC(drawit = False):
    ws = []                         # empty list for the w values
    its = []                        # empty list for the number of iterations per w
    wmin = 1                        # minimum w val
    wmax = 2                        # maximum w value
    w1 = wmax - (wmax - wmin)/1.618 # first w val to test
    w2 = wmin + (wmax - wmin)/1.618 # second w val to test

    while (wmax - wmin) > 0.001:                      # while they are too far apart
        smallnum = OverRelaxation(w1, drawit = False) # first num of iterations from w1
        bignum = OverRelaxation(w2, drawit = False)   # second num of iterations from w2

        ws.append(w1)                                 # save the w1 val
        ws.append(w2)                                 # save the w2 val
        its.append(smallnum)                          # save the num iterations 1 val
        its.append(bignum)                            # save the num iterations 2 val

        if smallnum < bignum:                         # if in the left section, move wmax down
            wmax = w2
        elif smallnum >= bignum:                      # if in the right section, move wmin up
            wmin = w1

        w1 = wmax - (wmax - wmin)/1.618               # update w1
        w2 = wmin + (wmax - wmin)/1.618               # update w2

    w = (wmin + wmax) / 2            # after while loop, average the two w vals for the optimal

    if drawit:                                             # if drawing
        pylab.plot(ws, its, "x")                           # plot the ws and their its
        pylab.xlabel("Weight Value")                       # xs are the weight for overrelaxation
        pylab.ylabel("Number of Iterations")               # ys are the number of iterations
        pylab.title("Number of Iterations per Value of W") # Title of the plot
        pylab.show()                                       # show the plot

    return w                         # return the averaged optimal w

def PartD(w = None):
    if w is None:
        w = PartC()
    overrexpoints = []
    rexpoints = []
    xs = []
    for n in [50, 100, 200, 400]:
        overrexpoints.append(OverRelaxation(w, N = n, drawit = False))
        rexpoints.append(Relaxation(N = n, drawit = False))
        xs.append(n)
    pylab.plot(xs, overrexpoints, label = "SOR Method")
    pylab.plot(xs, rexpoints, label = "Basic Jacobi Convergence")
    pylab.title("Number of Iterations per Number of Grid Points")
    pylab.ylabel("Number of Iterations")
    pylab.xlabel("Number of Grid Points")
    pylab.legend()
    pylab.show()

def ElectricField(boxvals, d, s = 1):
    efieldXdir = []
    efieldYdir = []
    efieldXpos = []
    efieldYpos = []
    for m in range(0, len(boxvals), s):
        for n in range(0, len(boxvals[m]), s):
            if m == 0:
                mdiff = (boxvals[m][n] - boxvals[m+1][n]) / (d)
            elif m == len(boxvals) - 1:
                mdiff = (boxvals[m-1][n] - boxvals[m][n]) / (d)
            else:
                mdiff = (boxvals[m-1][n] - boxvals[m+1][n]) / (d*2)
            if n == 0:
                ndiff = (boxvals[m][n] - boxvals[m][n+1]) / (d)
            elif n == len(boxvals[m]) - 1:
                ndiff = (boxvals[m][n-1] - boxvals[m][n]) / (d)
            else:
                ndiff = (boxvals[m][n-1] - boxvals[m][n+1]) / (d*2)
            efieldYdir.append(mdiff)
            efieldXdir.append(ndiff)
            efieldYpos.append(m)
            efieldXpos.append(n)
    return efieldXpos, efieldYpos, efieldXdir, efieldYdir

def PartE():
    N = 100
    s = 2
    d = N / 100
    for disss in range(3, 13, 2):
        tableVals = OverRelaxation(1.88, drawit = False, giveb = True, dist = disss)
        efieldYpos, efieldXpos, efieldYdir, efieldXdir = ElectricField(tableVals, d = d, s = s)
        pylab.quiver(efieldYpos, efieldXpos, efieldYdir, efieldXdir)
        pylab.title("Electric Field with a Distance of L/" + str(disss) + " Between Plates")
        pylab.show()

        pylab.clf()