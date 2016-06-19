#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from SetParameter import SetParameter
from create_percolation_cluster import Percolation
from plot_percolation_density import plot_percolation_density


if __name__ == '__main__':
    per = Percolation()

    def plot_pc_density():
        L = [int(l) for l in sp.entry['L'].get().strip().split(',')]
        trial = int(sp.entry['trial'].get())
        p_start = float(sp.entry['p_start'].get())
        p_stop = float(sp.entry['p_stop'].get())
        p_num = int(sp.entry['p_num'].get())
        plot_percolation_density(per, L, trial, p_start, p_stop, p_num)

    sp = SetParameter()
    parameters = [{'L': "10, 40, 160"},
                  {'trial': 100},
                  {'p_start': 0.},
                  {'p_stop': 1.},
                  {'p_num': 20},
                  ]
    cmds = [{'Calculate percolation density': plot_pc_density},
            {'Quit': sp.quit}
            ]
    sp.show_setting_window(parameters, cmds)
