#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from SetParameter import SetParameter
from create_percolation_cluster import Percolation
from plot_fractal_dimension_renormalization import calc_fractal_dimension


if __name__ == '__main__':
    per = Percolation()

    def calc_fractal_dimension_renormalization():
        per.L = int(sp.entry['L'].get())
        per.p = float(sp.entry['p'].get())
        b = int(sp.entry['b'].get())
        trial = int(sp.entry['trial'].get())
        calc_fractal_dimension(per, b, trial)

    sp = SetParameter()
    parameters = [{'L': 200},
                  {'p': 0.5927},
                  {'b': 2},
                  {'trial': 100},
                  ]
    cmds = [{'Calculate the fractal dimension by the method of renormalization'
             : calc_fractal_dimension_renormalization},
            {'Quit': sp.quit}
            ]
    sp.show_setting_window(parameters, cmds)
