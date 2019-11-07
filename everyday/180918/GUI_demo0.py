# 初探
from tkinter import *

Label(text="I'm in the first window!").pack()
second = Toplevel()
Label(second, text="I'm in the second window!").pack()

# 布局
Label(text="I'm in the first window!").pack()
second = Toplevel()
Label(second, text="I'm in the second window!").pack()

for i in range(10): Button(text=i).pack()

# help(Pack.config)
# Help on method pack_configure in module tkinter:
#
# pack_configure(self, cnf={}, **kw)
#     Pack a widget in the parent widget. Use as options:
#     after=widget - pack it after you have packed widget
#     anchor=NSEW (or subset) - position widget according to
#                               given direction
#     before=widget - pack it before you will pack widget
#     expand=bool - expand widget if parent size grows
#     fill=NONE or X or Y or BOTH - fill widget if widget grows
#     in=master - use master to contain this widget
#     in_=master - see 'in' option description
#     ipadx=amount - add internal padding in x direction
#     ipady=amount - add internal padding in y direction
#     padx=amount - add padding in x direction
#     pady=amount - add padding in y direction
#     side=TOP or BOTTOM or LEFT or RIGHT -  where to add this widget.

# help(Grid.configure)
# Help on method grid_configure in module tkinter:
#
# grid_configure(self, cnf={}, **kw)
#     Position a widget in the parent widget in a grid. Use as options:
#     column=number - use cell identified with given column (starting with 0)
#     columnspan=number - this widget will span several columns
#     in=master - use master to contain this widget
#     in_=master - see 'in' option description
#     ipadx=amount - add internal padding in x direction
#     ipady=amount - add internal padding in y direction
#     padx=amount - add padding in x direction
#     pady=amount - add padding in y direction
#     row=number - use cell identified with given row (starting with 0)
#     rowspan=number - this widget will span several rows
#     sticky=NSEW - if cell is larger on which sides will this
#                   widget stick to the cell boundary

help(Place.config)
# Help on method place_configure in module tkinter:
#
# place_configure(self, cnf={}, **kw)
#     Place a widget in the parent widget. Use as options:
#     in=master - master relative to which the widget is placed
#     in_=master - see 'in' option description
#     x=amount - locate anchor of this widget at position x of master
#     y=amount - locate anchor of this widget at position y of master
#     relx=amount - locate anchor of this widget between 0.0 and 1.0
#                   relative to width of master (1.0 is right edge)
#     rely=amount - locate anchor of this widget between 0.0 and 1.0
#                   relative to height of master (1.0 is bottom edge)
#     anchor=NSEW (or subset) - position anchor according to given direction
#     width=amount - width of this widget in pixel
#     height=amount - height of this widget in pixel
#     relwidth=amount - width of this widget between 0.0 and 1.0
#                       relative to width of master (1.0 is the same width
#                       as the master)
#     relheight=amount - height of this widget between 0.0 and 1.0
#                        relative to height of master (1.0 is the same
#                        height as the master)
#     bordermode="inside" or "outside" - whether to take border width of
#                                        master widget into account