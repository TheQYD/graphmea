#!/usr/bin/python

import argparse
import matplotlib.pyplot as plot
import matplotlib.ticker as ticker
import matplotlib.patches as patches
import random
import uuid
import matplotlib.colors as colors

COLORS = colors.cnames.keys()

def RenderGraph(**args_dict):
  """Draws a graph.

  Args:
    kwargs: a dict of arguments used to render a graph.

  Returns:
    None

  RenderGraph() takes arguements parsed by argparse and uses them to build a
  graph using matplotlib.
  """
  
  # Grab the values passed from the command line.
  graph_data = args_dict.get('graph_data', [])
  graph_type = args_dict.get('graph_type')
  graph_output = args_dict.get('graph_output', 'mygraph-1')
  graph_title = args_dict.get('graph_title')
  random_colors = args_dict.get('random_colors')
  xlabel = args_dict.get('xlabel')
  ylabel = args_dict.get('ylabel')
  filename = args_dict.get('filename')

  # Check for random colors

  if random_colors is True:
    random.shuffle(COLORS)
  if filename is None:
    filename = str(uuid.uuid4()) + '.png'

  # Call the function based on the first argument.
  eval(graph_type.capitalize())(graph_data, args_dict)
 
  # Find the axes maximums.
  graph_max = max([max(i) for i in graph_data])
  graph_len = max([len(i) for i in graph_data])
  #xmax = args_dict.get('xmax', graph_len - 1)
  #ymax = args_dict.get('ymax', round(graph_max * 1.05))

  # Plot the graph.
  #plot.axis([0, xmax, 0, ymax])
  plot.xlabel(xlabel)
  plot.ylabel(ylabel)
  plot.title(graph_title[0])
  plot.savefig(filename)
  plot.show() 

def Linegraph(graph_data, args_dict):
  graph_color = args_dict.get('graph_color', 'b')

  for gd in graph_data:
    lg_color = COLORS[graph_data.index(gd)] 
    x = range(0, len(gd))
    y = gd
    plot.plot(x, y, lg_color, lw=2)

def Bargraph(graph_data, args_dict):
  width = .7/len(graph_data)
  xticks = args_dict.get('xticks')
  yticks = args_dict.get('yticks')
  graph_len = max([len(i) for i in graph_data])
  bar_pos = range(graph_len)
  tick_pos = [i + width/graph_len for i in bar_pos]
  
  RenderLegend(args_dict)

  for gd in graph_data: 
    bg_color = COLORS[graph_data.index(gd)]
    
    plot.bar(bar_pos, gd, width, color=bg_color, align='center')
    bar_pos = [i + width for i in bar_pos]

  if xticks is not None:
    plot.xticks(tick_pos, xticks, rotation=45)
    #plot.yticks(range(len(gd)), gd)

def RenderLegend(args_dict):
  keys = args_dict.get('keys')
  line_list = []
  line_name = []

  for key in keys:
    line = patches.Patch(
        [],
        [],
        color = COLORS[keys.index(key)],
        label = keys[keys.index(key)]
    )
    line_list.append(line)
    line_name.append(key)
  
  plot.legend(line_list, line_name)

if __name__ == '__main__': 
  parser = argparse.ArgumentParser()
  parser.add_argument('type', action='store', type=str) 
  parser.add_argument('--data', '-d', action="append", type=str)
  parser.add_argument('--title', '-t', action='append', type=str)
  parser.add_argument('--filename', '-f', action='append', type=str)
  parser.add_argument('--output', '-o', action="store", type=str) 
  parser.add_argument('--color', '-c', action="store", type=str) 
  parser.add_argument('--style', '-s', action="store", type=str) 
  parser.add_argument('--xmax', '-X', action="store", type=int) 
  parser.add_argument('--ymax', '-Y', action="store", type=int) 
  parser.add_argument('--xlabel', '-x', action="store", type=str) 
  parser.add_argument('--ylabel', '-y', action="store", type=str)
  parser.add_argument('--xticks', action="store", type=str) 
  parser.add_argument('--yticks', action="store", type=str) 
  parser.add_argument('--keys', '-k', action="store", type=str) 
  parser.add_argument('--size', '-s', action="store", type=str) 

  args = parser.parse_args()
  graph_data = [map(int, i.split(',')) for i in args.data]

  if args.xticks is not None:
    args.xticks = args.xticks.split(',')
  if args.yticks is not None:
    args.yticks = args.yticks.split(',')
  if args.keys is not None:
    args.keys = args.keys.split(',')
  if args.color is not None:
    args.color = [i.split(',') for i in args.color] 
  if args.style is not None:
    args.style = [i.split(',') for i in args.style] 

  RenderGraph(
    graph_type=args.type,
    graph_data=graph_data,
    graph_title=args.title,
    graph_output=args.output,
    graph_style=args.style,
    xmax=args.xmax,
    ymax=args.ymax,
    xlabel=args.xlabel,
    ylabel=args.ylabel,
    xticks=args.xticks,
    keys=args.keys,
    graph_color=args.color,
    filename=args.filename,
    size=args.size
  )
