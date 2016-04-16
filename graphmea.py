#!/usr/bin/python

import argparse
import matplotlib.pyplot as plot
import random

COLORS = ['indigo', 'gold', 'hotpink', 'firebrick', 'indianred', 'yellow',
'mistyrose', 'darkolivegreen', 'olive', 'darkseagreen', 'pink', 'tomato',
'lightcoral', 'orangered', 'navajowhite', 'lime', 'palegreen', 'greenyellow',
'burlywood', 'seashell', 'mediumspringgreen', 'fuchsia', 'papayawhip',
'blanchedalmond', 'chartreuse', 'dimgray', 'black', 'peachpuff', 'springgreen',
'aquamarine', 'white', 'orange', 'lightsalmon', 'darkslategray', 'brown',
'ivory', 'dodgerblue', 'peru', 'lawngreen', 'chocolate', 'crimson',
'forestgreen', 'slateblue', 'lightseagreen', 'cyan', 'mintcream', 'silver',
'antiquewhite', 'mediumorchid', 'skyblue', 'gray', 'darkturquoise',
'goldenrod', 'darkgreen', 'floralwhite', 'darkviolet', 'darkgray', 'moccasin',
'saddlebrown', 'darkslateblue', 'lightskyblue', 'lightpink', 'mediumvioletred',
'red', 'deeppink', 'limegreen', 'darkmagenta', 'palegoldenrod', 'plum',
'turquoise', 'lightgoldenrodyellow', 'darkgoldenrod', 'lavender', 'maroon',
'yellowgreen', 'sandybrown', 'thistle', 'violet', 'navy', 'magenta', 'tan',
'rosybrown', 'olivedrab', 'blue', 'lightblue', 'ghostwhite', 'honeydew',
'cornflowerblue', 'linen', 'darkblue', 'powderblue', 'seagreen', 'darkkhaki',
'snow', 'sienna', 'mediumblue', 'royalblue', 'lightcyan', 'green',
'mediumpurple', 'midnightblue', 'cornsilk', 'paleturquoise', 'bisque',
'slategray', 'darkcyan', 'khaki', 'wheat', 'teal', 'darkorchid', 'deepskyblue',
'salmon', 'darkred', 'steelblue', 'palevioletred', 'lightslategray',
'aliceblue', 'lightgreen', 'orchid', 'gainsboro', 'mediumseagreen',
'lightgray', 'mediumturquoise', 'lemonchiffon', 'cadetblue', 'lightyellow',
'lavenderblush', 'coral', 'purple', 'aqua', 'whitesmoke', 'mediumslateblue',
'darkorange', 'mediumaquamarine', 'darksalmon', 'beige', 'blueviolet', 'azure',
'lightsteelblue', 'oldlace']


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
  random_colors = args_dict.get('random_colors')
  # Check for random colors

  if random_colors is True:
    random.shuffle(COLORS)
  
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
  plot.savefig('asdf'+ '.png')
  plot.show() 

def Linegraph(graph_data, args_dict):
  graph_color = args_dict.get('graph_color', 'b')
  
  for gd in graph_data:
    lg_color = COLORS[graph_data.index(gd)] 
    x = range(0, len(gd))
    y = gd
    plot.plot(x, y, lg_color, lw=2)

def Bargraph(graph_data, args_dict):
  graph_color = args_dict.get('graph_color', 'b')
  width = .7/len(graph_data)
  
  for gd in graph_data: 
    xtick_label = xticks[graph_data.index(gd)]
    bg_color = COLORS[graph_data.index(gd)]
    pos = range(0, len(gd))
    plot.bar(pos, gd, width, color=bg_color, align='center')
    plot.xticks(range(len(gd)), xtick_label, rotation='vertical')
    #plot.yticks(range(len(gd)), gd)
    pos = [i + width for i in pos]

if __name__ == '__main__': 
  parser = argparse.ArgumentParser()
  parser.add_argument('type', action='store', type=str) 
  parser.add_argument('--data', '-d', action="append", type=str)
  parser.add_argument('--title', '-t', action='append', type=str)
  parser.add_argument('--output', '-o', action="store", type=str) 
  parser.add_argument('--color', '-c', action="store", type=str) 
  parser.add_argument('--style', '-s', action="store", type=str) 
  parser.add_argument('--xmax', '-X', action="store", type=int) 
  parser.add_argument('--ymax', '-Y', action="store", type=int) 
  parser.add_argument('--xlabel', '-x', action="store", type=str) 
  parser.add_argument('--ylabel', '-y', action="store", type=str)
  parser.add_argument('--xticks', action="append", type=str) 
  
  args = parser.parse_args()
  graph_type = args.type
  graph_data = [map(int, i.split(',')) for i in args.data]
  xticks = [i.split(',') for i in args.xticks]
  graph_title = args.title 
  xmax = args.xmax
  ymax = args.ymax
  xlabel = args.xlabel
  ylabel = args.ylabel
  graph_output = args.output 
  
  try:
    graph_color = [i.split(',') for i in args.color] 
    graph_style = [i.split(',') for i in args.style] 
  except:
    graph_color = 'b'
    graph_style = ''
  
  RenderGraph(
    graph_type=graph_type,
    graph_data=graph_data,
    graph_title=graph_title,
    graph_output=graph_output,
    graph_style=graph_style,
    xmax=xmax,
    ymax=ymax,
    xlabel=xlabel,
    ylabel=ylabel,
    xticks=xticks,
    graph_color=graph_color
  )
