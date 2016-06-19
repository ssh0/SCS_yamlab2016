#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto


import matplotlib.pyplot as plt
import numpy as np


def calc_percolation_density_forL(per, L, trial, ps):
    """Calculate percolation density for given L.
    """
    per.L = L
    create_cluster = per.create_cluster
    set_labels = per.set_labels
    P = []

    for p in ps:
        per.p = p
        sum_of_cluster_size = 0
        for t in range(trial):
            create_cluster()
            set_labels()
            # 最大クラスターのサイズを用いるバージョン(Feder, 1988)
            l = per.lattice
            l = l[np.nonzero(l)]
            if len(l) != 0:
                sum_of_cluster_size += np.amax(np.bincount(l.flatten()))

            # パーコレートクラスターのサイズのみ勘定に入れるバージョン
            # if per.is_percolate():
            #     cluster_size = 0
            #     for ptag in list(per.ptag):
            #         where = np.where(per.lattice == ptag)
            #         size = float(len(where[0]))
            #         if size > cluster_size:
            #             cluster_size = size
            #     sum_of_cluster_size += cluster_size
        P.append(float(sum_of_cluster_size) / (trial * L ** 2))
    return P

def plot_percolation_density(per, L_list, trial, p_start, p_stop, p_num=50):
    """Plot percolation density for given p and L.

    --- Arguments ---
    per     (class): Instance variant of Percolation class
    L_list   (list): List of system size L
    trial     (int): A number of trials for calculating percolation probability
    p_start (float): The starting value of p
    p_stop  (float): The end value of p
    p_num     (int): Number of sample to generate a p-sequences
    """
    fig = plt.figure("Percolation density (trial={})".format(trial))
    ax = fig.add_subplot(111)
    ps = np.linspace(p_start, p_stop, p_num)
    for L in L_list:
        P = calc_percolation_density_forL(per, L, trial, ps)
        ax.plot(ps, P, '-o', label='L = {}'.format(L))
    ax.set_title("Percolation density (trial={})".format(trial))
    ax.set_xlabel(r'Occupation probability $p$', fontsize=16)
    ax.set_ylabel(r'Percolation density $P_{\infty}$', fontsize=16)
    ax.set_xlim(p_start, p_stop)
    ax.set_ylim(0., 1.)
    fig.tight_layout()
    plt.legend(loc='best')
    plt.show()
