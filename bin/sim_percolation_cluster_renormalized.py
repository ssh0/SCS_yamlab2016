#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

from SetParameter import SetParameter
from create_percolation_cluster import Percolation
from plot_fractal_dimension_renormalization import is_percolated, renormalize


if __name__ == '__main__':
    per = Percolation()
    count = 1

    def create_cluster():
        p = float(sp.entry['p'].get())
        L = int(sp.entry['L'].get())
        per.p = p
        per.L = L
        per.create_cluster()
        per.set_labels()
        per.draw_canvas()

    def renormalization():
        b = int(sp.entry['b'].get())
        m2, M2 = renormalize(per, b)
        per.draw_canvas()

    def save_to_eps():
        global count
        p = float(sp.entry['p'].get())
        filename = "figure_%d(p=%s).eps" % (count, str(p))
        d = per.canvas.postscript(file=filename)
        print "Current canvas is saved to {}".format(filename)
        count += 1

    sp = SetParameter()
    parameters = [{'L': 200},
                  {'p': 0.5927},
                  {'b': 2}
                  ]
    cmds = [[{'Run': create_cluster},
             {'Renormalize the cluster': renormalization}],
            [{'Save the canvas to eps file': save_to_eps},
             {'Quit': sp.quit}]
            ]
    sp.show_setting_window(parameters, *cmds)
