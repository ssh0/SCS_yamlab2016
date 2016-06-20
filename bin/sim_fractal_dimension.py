#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from SetParameter import SetParameter
from create_percolation_cluster import Percolation
from plot_fractal_dimension import view_expansion


if __name__ == '__main__':
    per = Percolation()

    def calc_fractal_dimension(widget):
        per.p = float(sp.entry['p'].get_text())
        per.L = int(sp.entry['L'].get_text())
        per.create_cluster()
        per.set_labels()
        if per.is_percolate():
            view_expansion(per)
        else:
            print "Created cluster is not percolated. Try again."

    sp = SetParameter()
    parameters = [{'L': 61},
                  {'p': 0.5927}
                  ]
    cmds = [[{'Calculate the fractal dimension': calc_fractal_dimension}],
            [{'Quit': sp.quit}]
            ]
    sp.show_setting_window(parameters, *cmds)
