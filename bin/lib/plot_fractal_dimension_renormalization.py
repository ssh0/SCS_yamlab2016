#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

import numpy as np
from create_percolation_cluster import Percolation
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def is_percolated(lattice, L):
    left = set(lattice[0])
    right = set(lattice[L - 1])
    top = set([lattice[t][0] for t in range(L)])
    bottom = set([lattice[t][L - 1] for t in range(L)])
    # 縦・横両方
    # ptag = (left.intersection(right)
    #         | top.intersection(bottom)) - set([0])
    # 縦のみ
    ptag = top.intersection(bottom) - set([0])
    if len(ptag) != 0:
        return True
    else:
        return False


def renormalize(per, b=2):
    """スケール因子bによって繰り込まれた格子を生成する関数
    """
    if per.L % b != 0:
        raise ValueError("lattice cannot be divided by scale factor b")

    lattice = per.lattice
    rlattice = np.zeros([per.L / b, per.L / b], dtype=np.bool)
    for i in range(per.L / b):
        ic = b * i
        for j in range(per.L / b):
            jc = b * j
            if is_percolated(lattice[ic:ic + b, jc:jc + b], b):
                rlattice[i, j] = True
    per.L = per.L / b
    per.lattice = rlattice
    per.set_labels()
    rlattice = per.lattice
    return lattice, rlattice

def count_largest_cluster(per, b):
    """最大クラスターサイズを取得する関数
    """
    lattice, rlattice = renormalize(per, b)
    lattice = lattice[np.nonzero(lattice)]
    if len(lattice) != 0:
        M = np.amax(np.bincount(lattice.flatten()))
    else:
        M = 0

    rlattice = rlattice[np.nonzero(rlattice)]
    if len(rlattice) != 0:
        rM = np.amax(np.bincount(rlattice.flatten()))
    else:
        rM = 0
    return M, rM

def calc_fractal_dimension(per, trial):
    """繰り込まれた格子中の最大クラスターサイズからフラクタル次元を求める関数
    """
    ave_M2, ave_rM2 = [], []
    L = per.L
    blist = [b for b in range(2, per.L) if per.L % b == 0]
    create_cluster = per.create_cluster
    set_labels = per.set_labels
    for b in blist:
        M2, rM2 = [], []
        for t in range(trial):
            create_cluster()
            set_labels()
            M, rM = count_largest_cluster(per, b)
            per.L = L
            M2.append(M ** 2)
            rM2.append(rM ** 2)
        ave_M2.append(np.average(M2))
        ave_rM2.append(np.average(rM2))

    X = np.log(np.array(blist)) * 2
    Y = np.log(np.array(ave_M2) / np.array(ave_rM2))

    # Ds = Y / X
    # D = np.average(Ds)
    # print Ds
    # print D

    # # csvファイルとして保存
    # filename = 'result_fractal_dim_renormalization.csv'
    # res = np.array([X, Y]).T
    # print "2 * log(b), log(ave_M2 / ave_rM2) = Y"
    # print res
    # np.savetxt(filename, res, delimiter=',')
    # print "Saved to '%s'." % filename

    # # === これより下はscipy.optimizeを用いてフィッティングした場合の例 ===
    def fit_func(parameter0, x, y):
        c1 = parameter0[0]
        c2 = parameter0[1]
        residual = y - c1 - c2 * x
        return residual

    parameter0 = [0., 1.5]
    result = optimize.leastsq(fit_func, parameter0, args=(X, Y))
    c1 = result[0][0]
    D = result[0][1]
    print "D = %f" % D

    def fitted(x, c1, D):
        return D * x + c1

    # 可視化
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(X, Y, '-o', label="L = %d, p = %f" % (per.L, per.p))
    ax.plot(X, fitted(X, c1, D), label="D = %f" % D)
    ax.set_title("Fractal Dimension")
    ax.set_xlabel(r'$2 \log b$', fontsize=16)
    ax.set_ylabel(r"$\log \frac{\langle M^{2} \rangle}{\langle M'^{2} \rangle}$", fontsize=16)
    ax.set_xscale('linear')
    ax.set_yscale('linear')
    plt.legend(loc='best')
    plt.show()
