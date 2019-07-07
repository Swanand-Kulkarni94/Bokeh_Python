#Bokeh Python

"""
Link
https://bokeh.pydata.org/en/latest/docs/gallery/hex_tile.html
"""

#Libraries
import numpy as np 

from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import linear_cmap
from bokeh.util.hex import hexbin

n = 50000 #Fifty Thousand points
x = np.random.standard_normal(n)
y = np.random.standard_normal(n)

bins = hexbin(x, y, 0.1)

p = figure(title = "Manual HexBin Tile for 50k points", tools = "wheel_zoom, pan, reset",
			match_aspect = True, background_fill_color = '#440154')
p.grid.visible = False

p.hex_tile(q = 'q', r = 'r', size = 0.1, line_color = None, source = bins,
			fill_color = linear_cmap('counts', 'Viridis256', 0, max(bins.counts)))

output_file("HexBinTile.html")

show(p)