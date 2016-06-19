#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.

from Tkinter import *


class SetParameter(object):

    def show_setting_window(self, parameters, *commands_set):
        """ Show a parameter setting window.

        --- Arguments ---
        parameters  : A list of dictionaries:
                      [{'<parameter name>': <default_value>}...]
        commands_set: A list of dictionary
                      [{'<label of the button>': <function>}...]
        """
        self.root = Tk()
        self.root.title('Parameter')

        frame = []
        frame.append(Frame(self.root, padx=5, pady=5))
        frame[-1].pack(side='top')
        self.entry = {}
        for i, parameter in enumerate(parameters):
            param_name = parameter.items()[0][0]
            if i == 0:
                first_param = param_name
            label = Label(frame[-1], text=param_name + ' = ')
            label.grid(row=i, column=0, sticky=E)
            self.entry[param_name] = Entry(frame[-1], width=10)
            self.entry[param_name].grid(row=i, column=1)
            self.entry[param_name].delete(0, END)
            self.entry[param_name].insert(0, parameter.items()[0][1])
        self.entry[first_param].focus_set()

        for commands in commands_set:
            frame.append(Frame(self.root, padx=5, pady=5))
            frame[-1].pack(side='top')
            self.button = []
            for i, command in enumerate(commands):
                self.button.append(Button(frame[-1],
                                          text=command.items()[0][0],
                                          command=command.items()[0][1]
                                          )
                                   )
                self.button[i].grid(row=0, column=i)

        self.root.mainloop()

    def quit(self):
        self.root.destroy()
