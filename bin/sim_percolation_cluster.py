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

    def save_to_eps():
        global count
        p = float(sp.entry['p'].get())
        filename = "figure_%d(p=%s).eps" % (count, str(p))
        d = per.canvas.postscript(file=filename)
        print "Current canvas is saved to {}".format(filename)
        count += 1

    sp = SetParameter()
    parameters = [{'L': 61},
                  {'p': 0.5927}
                  ]
    cmds = [{'Run': create_cluster},
            {'Save the canvas to eps file': save_to_eps},
            {'Quit': sp.quit}]
    sp.show_setting_window(parameters, cmds)
