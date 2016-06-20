#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from SetParameter import SetParameter
from create_percolation_cluster import Percolation


if __name__ == '__main__':
    per = Percolation()
    count = 1

    def create_cluster(widget):
        p = float(sp.entry['p'].get_text())
        L = int(sp.entry['L'].get_text())
        per.p, per.L = p, L
        per.create_cluster()
        per.set_labels()
        per.draw_canvas()

    sp = SetParameter()
    parameters = [{'L': 61},
                  {'p': 0.5927}
                  ]
    cmds = [{'Run': create_cluster},
            {'Quit': sp.quit}]
    sp.show_setting_window(parameters, cmds)
