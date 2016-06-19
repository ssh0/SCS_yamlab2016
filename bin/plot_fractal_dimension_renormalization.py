#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from Tkinter import *
import numpy as np
from create_percolation_cluster import Percolation
import matplotlib.pyplot as plt


def is_percolated(lattice, L):
    left = set(lattice[0])
    right = set(lattice[L - 1])
    top = set([lattice[t][0] for t in range(L)])
    bottom = set([lattice[t][L - 1] for t in range(L)])
    ptag = (left.intersection(right)
                    | top.intersection(bottom)) - set([0])
    if len(ptag) != 0:
        return True
    else:
        return False


def renormalize(per, b=2):
    if per.L % b != 0:
        raise ValueError("lattice cannot be divided by scale factor b")

    lattice = per.lattice
    rlattice = np.zeros([per.L / b, per.L / b], dtype=np.bool)
    for i in range(per.L / b):
        ic = b * i
        for j in range(per.L / b):
            jc = b * j
            if is_percolated(lattice[ic:ic+b, jc:jc+b], b):
                rlattice[i, j] = True

    lattice = lattice[np.nonzero(lattice)]
    if len(lattice) != 0:
        M = np.amax(np.bincount(lattice.flatten()))
    else:
        M = 0

    per.L = per.L / b
    per.lattice = rlattice
    per.set_labels()
    rlattice = per.lattice

    rlattice = rlattice[np.nonzero(rlattice)]
    if len(rlattice) != 0:
        rM = np.amax(np.bincount(rlattice.flatten()))
    else:
        rM = 0
    return M, rM


def calc_fractal_dimension(per, b, trial):
    M2, rM2 = [], []
    L = per.L
    create_cluster = per.create_cluster
    set_labels = per.set_labels
    for t in range(trial):
        create_cluster()
        set_labels()
        M, rM = renormalize(per, b)
        per.L = L
        M2.append(M ** 2)
        rM2.append(rM ** 2)

    ave_M2 = np.average(M2)
    ave_rM2 = np.average(rM2)
    D = np.log(ave_M2 / ave_rM2) / (2 * np.log(b))
    print 'D = %f' % D
