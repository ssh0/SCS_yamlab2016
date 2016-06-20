#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto


import matplotlib.pyplot as plt
import numpy as np


def plot_percolation_freq(per, L_list, trial, p_start, p_stop, p_num=50):
    """Plot percolation frequency for given p and L.

    --- Arguments ---
    per     (class): Instance variant of Percolation class
    L_list   (list): List of system size L
    trial     (int): A number of trials for calculating percolation probability
    p_start (float): The starting value of p
    p_stop  (float): The end value of p
    p_num     (int): Number of sample to generate a p-sequences
    """
    fig = plt.figure("Percolation frequency (trial={})".format(trial))
    ax = fig.add_subplot(111)
    for L in L_list:
        P = []
        ps = np.linspace(p_start, p_stop, p_num)
        for p in ps:
            per.p = p
            percolate = 0
            for t in range(trial):
                per.create_cluster()
                per.set_labels()
                if per.is_percolate():
                    percolate += 1
            P.append(float(percolate) / trial)
        ax.plot(ps, P, '-o', label='L = {}'.format(L))
    ax.set_title("Percolation frequency (trial={})".format(trial))
    ax.set_xlabel(r'Occupation probability $p$', fontsize=16)
    ax.set_ylabel(r'Percolation frequency $P$', fontsize=16)
    ax.set_xlim(p_start, p_stop)
    ax.set_ylim(0., 1.)
    fig.tight_layout()
    plt.legend(loc='best')
    plt.show()
