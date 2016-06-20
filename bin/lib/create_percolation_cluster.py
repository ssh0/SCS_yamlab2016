#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

import matplotlib.pyplot as plt
import numpy as np


class Percolation(object):

    def __init__(self, L=61, p=0.5):
        """Initialise Percolation class.

        --- Arguments ---
        L (int)  : Lattice size (L x L)
        p (float): Probability of site occupation
        """
        self.L = L
        self.p = p

    def create_cluster(self):
        """Create the cluster with occupation probability p.
        """
        self.lattice = np.zeros([self.L, self.L], dtype=bool)
        rn = np.random.random([self.L, self.L])
        self.lattice[rn < self.p] = True

    def set_labels(self):
        """Label the same number for points with connected (= cluster).
        """
        label = np.zeros([self.L + 2, self.L + 2], dtype=int)
        n = 1
        for i, j in np.array(np.where(self.lattice)).T:
            tags = list(set([label[i][j + 1], label[i + 1][j]]) - set([0]))
            if len(tags) == 0:
                label[i + 1, j + 1] = n
                n += 1
            else:
                label[i + 1, j + 1] = min(tags)

        for i, j in reversed(np.array(np.where(label > 0)).T):
            nn = set([label[i + 1, j], label[i, j + 1],
                      label[i, j]]) - set([0])
            min_tag = min(list(nn))
            for tag in nn - set([min_tag]):
                label[label == tag] = min_tag

        self.lattice = label[1:-1, 1:-1]
        left = set(self.lattice[0])
        right = set(self.lattice[self.L - 1])
        top = set([self.lattice[t][0] for t in range(self.L)])
        bottom = set([self.lattice[t][self.L - 1] for t in range(self.L)])
        self.ptag = (left.intersection(right)
                     | top.intersection(bottom)) - set([0])

    def is_percolate(self):
        """Return true if the cluster is percolated.
        """
        if len(self.ptag) != 0:
            return True
        else:
            return False

    def draw_canvas(self):
        """Draw the clusters using matplotlib.pyplot.matshow.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111)
        # maxtag = np.amax(self.lattice)
        rect = np.ma.masked_equal(self.lattice, 0)
        # for i, tag in enumerate(list(self.ptag)):
        #     rect[rect == tag] = maxtag + i + 1
        # ax.matshow(rect, vmin=maxtag, cmap=plt.cm.gnuplot)
        ax.matshow(rect, cmap=plt.cm.jet)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        plt.show()
