#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from SetParameter import SetParameter
from create_percolation_cluster import Percolation
from plot_percolation_probability import plot_percolation_prob


if __name__ == '__main__':
    per = Percolation()

    def _plot_percolation_prob():
        L = [int(l) for l in sp.entry['L'].get().strip().split(',')]
        trial = int(sp.entry['trial'].get())
        p_start = float(sp.entry['p_start'].get())
        p_stop = float(sp.entry['p_stop'].get())
        p_num = int(sp.entry['p_num'].get())
        plot_percolation_prob(per, L, trial, p_start, p_stop, p_num)

    sp = SetParameter()
    parameters = [{'L': "10, 100, 200"},
                  {'trial': 100},
                  {'p_start': 0.5},
                  {'p_stop': 0.7},
                  {'p_num': 20},
                  ]
    cmds = [{'Calculate percolation probability': _plot_percolation_prob},
            {'Quit': sp.quit}]
    sp.show_setting_window(parameters, cmds)
