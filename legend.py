#!/usr/bin/python

import matplotlib.lines as lines
import matplotlib.pyplot as plot

red_line = lines.Line2D(
        [], 
        [], 
        color='red', 
        marker='*', 
        markersize=15,
        label='Red Dashes')

plot.legend(handles=[red_line])
plot.show()
