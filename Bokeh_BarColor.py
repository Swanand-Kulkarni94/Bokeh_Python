#Bokeh Python

"""Link
https://bokeh.pydata.org/en/latest/docs/gallery/bar_colormapped.html
"""

#Libraries
import numpy as np 

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

output_file("BarColorMap.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

source = ColumnDataSource(data = dict(fruits = fruits, counts = counts))
#What happens in this line over here ?

p = figure(x_range = fruits, plot_height = 350, toolbar_location = None, title = "Fruit Counts")
p.vbar(x = 'fruits', top = 'counts', width = 0.9, source = source, legend = "fruits",
	  line_color = 'white', fill_color = factor_cmap('fruits', palette = Spectral6, factors = fruits))

p.xgrid.grid_line_color = None
p.y_range.start = 0
p.y_range.end = 9
p.legend.orientation = 'horizontal'
p.legend.location = 'top_center'

show(p)