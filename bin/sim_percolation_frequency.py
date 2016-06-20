#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from lib.SetParameter import SetParameter
from lib.create_percolation_cluster import Percolation
from lib.plot_percolation_frequency import plot_percolation_freq


if __name__ == '__main__':
    per = Percolation()

    def _plot_percolation_freq(widget):
        L = [int(l) for l in sp.entry['L'].get_text().strip().split(',')]
        trial = int(sp.entry['trial'].get_text())
        p_start = float(sp.entry['p_start'].get_text())
        p_stop = float(sp.entry['p_stop'].get_text())
        p_num = int(sp.entry['p_num'].get_text())
        plot_percolation_freq(per, L, trial, p_start, p_stop, p_num)

    sp = SetParameter()
    parameters = [{'L': "10, 40, 160"},
                  {'trial': 50},
                  {'p_start': 0.},
                  {'p_stop': 1.},
                  {'p_num': 20},
                  ]
    cmds = [[{'Calculate percolation frequency': _plot_percolation_freq}],
            [{'Quit': sp.quit}]
            ]
    sp.show_setting_window(parameters, *cmds)
