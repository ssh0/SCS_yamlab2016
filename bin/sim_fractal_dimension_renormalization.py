#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from lib.SetParameter import SetParameter
from lib.create_percolation_cluster import Percolation
from lib.plot_fractal_dimension_renormalization import calc_fractal_dimension


if __name__ == '__main__':
    per = Percolation()

    def calc_fractal_dimension_renormalization(widget):
        per.L = int(sp.entry['L'].get_text())
        per.p = float(sp.entry['p'].get_text())
        trial = int(sp.entry['trial'].get_text())
        calc_fractal_dimension(per, trial)

    sp = SetParameter()
    parameters = [{'L': 128},
                  {'p': 0.5927},
                  {'trial': 10},
                  ]
    cmds = [{'Calculate the fractal dimension by the method of renormalization'
             : calc_fractal_dimension_renormalization},
            {'Quit': sp.quit}
            ]
    sp.show_setting_window(parameters, cmds)
