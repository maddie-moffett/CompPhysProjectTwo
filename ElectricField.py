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

def PartD():
    w = PartC()
    overrexpoints = []
    rexpoints = []
    xs = []
    for n in range(50, 450, 50):
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

if __name__ == "__main__":
    PartD()