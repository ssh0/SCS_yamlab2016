#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto

import pygtk
pygtk.require('2.0')
import gtk


class SetParameter(object):

    def show_setting_window(self, parameters, *commands_set):
        """ Show a parameter setting window.

        --- Arguments ---
        parameters  : A list of dictionaries:
                      [{'<parameter name>': <default_value>}...]
        commands_set: A list of dictionary
                      [{'<label of the button>': <function>}...]
        """
        self.root = gtk.Window()
        self.root.tooltips = gtk.Tooltips()
        self.root.set_title('Parameter')
        self.root.connect('destroy_event', self.quit)
        self.root.connect('delete_event', self.quit)

        self.entry = {}
        vbox = gtk.VBox(spacing=3)
        for i, parameter in enumerate(parameters):
            hbox = gtk.HBox(spacing=5)
            param_name = str(parameter.items()[0][0])
            label = gtk.Label()
            label.set_text(param_name + ' = ')
            entry = gtk.Entry()
            entry.set_text(str(parameter.items()[0][1]))
            self.entry[param_name] = entry
            hbox.add(label)
            hbox.add(entry)
            vbox.add(hbox)

        for commands in commands_set:
            hbox = gtk.HBox(spacing=5)
            for i, command in enumerate(commands):
                button = gtk.Button()
                button.set_label(command.items()[0][0])
                button.connect('clicked', command.items()[0][1])
                hbox.add(button)
            vbox.add(hbox)

        self.root.add(vbox)
        self.root.show_all()
        gtk.main()

    def quit(self, widget, data=None):
        gtk.main_quit()
