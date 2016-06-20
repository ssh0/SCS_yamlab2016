#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from SetParameter import SetParameter
from create_percolation_cluster import Percolation
from plot_fractal_dimension_renormalization import is_percolated, renormalize


if __name__ == '__main__':
    per = Percolation()

    def create_cluster(widget):
        p = float(sp.entry['p'].get_text())
        L = int(sp.entry['L'].get_text())
        per.p, per.L = p, L
        per.create_cluster()
        per.set_labels()
        per.draw_canvas()

    def renormalization(widget):
        b = int(sp.entry['b'].get_text())
        lattice, rlattice = renormalize(per, b)
        per.draw_canvas()

    sp = SetParameter()
    parameters = [{'L': 256},
                  {'p': 0.5927},
                  {'b': 2}
                  ]
    cmds = [[{'Run': create_cluster},
             {'Renormalize the cluster': renormalization}],
            [{'Quit': sp.quit}]
            ]
    sp.show_setting_window(parameters, *cmds)
