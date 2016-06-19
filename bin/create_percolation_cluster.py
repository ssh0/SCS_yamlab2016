#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from Tkinter import Tk, Frame, Label, Entry, Button, END, YES, Toplevel, Canvas
import numpy as np
import sys
from SetParameter import SetParameter


class Percolation(object):

    def __init__(self, L=61, p=0.5):
        """Initialise Percolation class.

        --- Arguments ---
        L (int)  : Lattice size (L x L)
        p (float): Probability of site occupation
        """
        self.sub = None
        self.L = L
        self.p = p

    def create_cluster(self):
        """Create the cluster with occupation probability p.
        """
        self.lattice = np.zeros([self.L, self.L], dtype=bool)
        if self.sub is None or not self.sub.winfo_exists():
            rn = np.random.random([self.L, self.L])
            self.lattice[rn < self.p], self.lattice[rn >= self.p] = True, False

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

    def draw_canvas(self, canvas_size=640, margin=10):
        default_size = canvas_size  # default size of canvas
        r = int(default_size / (2 * self.L)) or 1
        fig_size = 2 * r * self.L + 1
        sub = Toplevel()

        sub.title('figure  ' + '(p=%s)' % str(self.p))
        self.canvas = Canvas(sub, width=fig_size + 2 * margin,
                             height=fig_size + 2 * margin)
        self.canvas.create_rectangle(margin, margin,
                                     fig_size + margin, fig_size + margin,
                                     outline='black', fill='white', width=1)
        self.canvas.pack()

        c = self.canvas.create_rectangle
        rect = self.lattice

        for m, n in np.array(np.nonzero(rect)).T:
            if rect[m][n] in self.ptag:
                c(2 * m * r + margin + 1, 2 * n * r + margin + 1,
                  2 * (m + 1) * r + margin, 2 * (n + 1) * r + margin,
                  outline='blue', fill='blue')
            else:
                c(2 * m * r + margin + 1, 2 * n * r + margin + 1,
                  2 * (m + 1) * r + margin, 2 * (n + 1) * r + margin,
                  outline='black', fill='black')
