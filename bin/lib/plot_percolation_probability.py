#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto


import matplotlib.pyplot as plt
import numpy as np


def calc_percolation_strength_forL(per, L, trial, ps):
    """Calculate percolation strength for given L.
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
            l = per.lattice
            l = l[np.nonzero(l)]
            if len(l) != 0:
                sum_of_cluster_size += np.amax(np.bincount(l.flatten()))
        P.append(float(sum_of_cluster_size) / (trial * L ** 2))
    return P


def plot_percolation_probability(per, L_list, trial, p_start, p_stop, p_num=50):
    """Plot percolation density for given p and L.

    --- Arguments ---
    per     (class): Instance variant of Percolation class
    L_list   (list): List of system size L
    trial     (int): A number of trials for calculating percolation probability
    p_start (float): The starting value of p
    p_stop  (float): The end value of p
    p_num     (int): Number of sample to generate a p-sequences
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ps = np.linspace(p_start, p_stop, p_num)
    for L in L_list:
        P = calc_percolation_strength_forL(per, L, trial, ps)
        ax.plot(ps, P, '-o', label='L = %d' % L)
    ax.set_title("Percolation probability (trial=%d)" % trial)
    ax.set_xlabel('Occupation probability p', fontsize=16)
    ax.set_ylabel('Percolation strength P_{N}', fontsize=16)
    ax.set_xlim(p_start, p_stop)
    ax.set_ylim(0., 1.)
    plt.legend(loc='best')
    plt.show()
