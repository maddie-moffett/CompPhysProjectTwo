from Relaxation import Relaxation
from OverRelaxation import OverRelaxation
from math import inf
import pylab

def PartC(drawit = False):
    ws = []
    its = []
    wmin = 1
    wmax = 2
    w1 = wmax - (wmax - wmin)/1.618
    w2 = wmin + (wmax - wmin)/1.618

    while (wmax - wmin) > 0.001:
        smallnum = OverRelaxation(w1, drawit = False)
        bignum = OverRelaxation(w2, drawit = False)

        ws.append(w1)
        ws.append(w2)
        its.append(smallnum)
        its.append(bignum)

        if smallnum < bignum:
            wmax = w2
        elif smallnum >= bignum:
            wmin = w1

        w1 = wmax - (wmax - wmin)/1.618
        w2 = wmin + (wmax - wmin)/1.618

    w = (wmin + wmax) / 2

    if drawit:
        pylab.plot(ws, its, "x")
        pylab.xlabel("Weight Value")
        pylab.ylabel("Number of Iterations")
        pylab.title("Number of Iterations per Value of W")
        pylab.show()

    return w

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
        tableVals = OverRelaxation(1.5, drawit = False, giveb = True, dist = disss)
        efieldYpos, efieldXpos, efieldYdir, efieldXdir = ElectricField(tableVals, d = d, s = s)
        pylab.quiver(efieldYpos, efieldXpos, efieldYdir, efieldXdir)
        pylab.title("Electric Field with a Distance of L/" + str(disss) + " Between Plates")
        pylab.show()

        pylab.clf()

if __name__ == "__main__":
    print(PartC(True))