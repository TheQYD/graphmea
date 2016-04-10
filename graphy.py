#!/usr/bin/python

import sys
import numpy
import argparse
import matplotlib.pyplot as plot

def drawgraph():
  xmax = len(graph_values) - 1
  ymax = round(max(graph_values) * 1.05)
  
  plot.title(graph_title)
  plot.axis([0, xmax, 0, ymax])
  plot.savefig('dumb.png')
  plot.show() 

def linegraph(graph_values):
  x = range(0, len(graph_values))
  y = graph_values

  plot.plot(x, y, 'r', lw=2)

def bargraph(graph_values):
  bar_positions = range(len(graph_values))
  p1 = plot.bar(bar_positions, graph_values, 0.5, color='r')

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('graph', action="store", type=str)
  parser.add_argument('--title', '-t', action="store", type=str)
  parser.add_argument('--values', '-v', action="store", type=list)
  
  args = parser.parse_args()
  graph_values = args.values
  graph_values = [int(number) for number in graph_values if number is not ',']
  graph_type = args.graph
  graph_title = args.title
  
  if graph_type == 'bar':
    bargraph(graph_values)
  elif graph_type == 'line':
    linegraph(graph_values)
  else:
    print "Please put an appropriate argument."

  drawgraph()
