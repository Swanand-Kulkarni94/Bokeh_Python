#Bokeh Python

#NOT WORKING

"""
Link
https://bokeh.pydata.org/en/latest/docs/gallery/categorical_scatter_jitter.html
"""

from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.sampledata.commits import data 
from bokeh.transform import jitter 

output_file("CategoricalScatterJitter.html")

DAYS = ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']

source = ColumnDataSource

p = figure(plot_width = 800, plot_height = 300, y_range = DAYS, x_axis_type = 'datetime',
	title = "Commits by Time of Day")

p.circle(x = 'time', y = jitter('day', width = 0.6, range = p.y_range),
	source = source, aplha = 0.3)

p.xaxis[0].formatter.days = ['%Hh']
p.x_range.range_padding = 0
p.ygrid.grid_line_color = None

show(p)