from Relaxation import Relaxation
from OverRelaxation import OverRelaxation
from math import inf
import pylab

def PartC():
    mini = inf
    minnum = 0
    for w in [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]:
        nmin = OverRelaxation(w, drawit = False)
        if nmin <= mini:
            mini = nmin
            minnum = w
    return minnum

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