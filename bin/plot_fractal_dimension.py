#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto


import matplotlib.pyplot as plt
import numpy as np
# import scipy.optimize as optimize


def view_expansion(per):
    lattice = np.zeros([per.L, per.L])
    lattice[per.lattice == list(per.ptag)[0]] = 1
    M_b = []
    s = np.sum
    ave = np.average
    append = M_b.append
    for k in range(1, int(per.L) / 2):
        nonzero = np.nonzero(lattice[k:-k, k:-k])
        tmp = np.array([0])
        for i, j in zip(nonzero[0] + k, nonzero[1] + k):
            tmp = np.append(
                tmp, s(lattice[i - k:i + k + 1, j - k:j + k + 1]))
        append(ave(tmp))

    b = np.array([2. * k + 1 for k in range(1, int(per.L) / 2)])
    M_b = np.array(M_b)

    # csvファイルとして保存
    filename = 'result_fractal_dim.csv'
    res = np.array([b, M_b]).T
    np.savetxt(filename, res)
    print "File saved to '{}'.".format(filename)


    # # === これより下はscipy.optimizeを用いてフィッティングした場合の例 ===
    # def fit_func(parameter0, b, M_b):
    #     log = np.log
    #     c1 = parameter0[0]
    #     c2 = parameter0[1]
    #     residual = log(M_b) - c1 - c2 * log(b)
    #     return residual

    # parameter0 = [0.1, 2.0]
    # result = optimize.leastsq(
    #     fit_func, parameter0, args=(b[:-1], M_b[:-1]))
    # c1 = result[0][0]
    # D = result[0][1]
    # print "D = %f" % D

    # def fitted(b, c1, D):
    #     return np.exp(c1) * (b ** D)

    fig = plt.figure("Fractal Dimension")
    ax = fig.add_subplot(111)
    ax.plot(b, M_b, '-o', label="p = %f" % per.p)
    # ax.plot(b, fitted(b, c1, D), label="D = %f" % D)
    ax.set_title("Fractal Dimension")
    ax.set_xlabel(r'$b$', fontsize=16)
    ax.set_ylabel(r'$M(b)$', fontsize=16)
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_ymargin(0.05)
    fig.tight_layout()
    plt.legend(loc='best')
    plt.show()
