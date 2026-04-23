import Relaxation
import OverRelaxation
from math import inf

def PartC():
    mini = inf
    minnum = 0
    for w in range(1.0, 1.6, 0.1):
        nmin = OverRelaxation.OverRelaxation(w)
        if nmin <= mini:
            mini = nmin
            minnum = w
    return minnum