# Importing bokeh
from bokeh.plotting import figure
from bokeh.plotting import show
from bokeh.plotting import output_file

# Interface
p = figure(plot_width=500, plot_height=500, tools='pan')

# Set titlo
p.title.text="Data Visualization"
p.title.text_color = "Gray"
p.title.text_font = "times"
p.title.text_font_style = "bold"

# Color in ticks line
p.xaxis.minor_tick_line_color = "Blue"
p.yaxis.minor_tick_line_color = "Green"

# Add the label
p.xaxis.axis_label = "Date"
p.yaxis.axis_label = "Intensity"

# Data
x = [1,2,3,4,5]
y = [6,7,8,9,10]

# Draw the line plot
p.line(x,y)

# Save the file
output_file("graph.html")

# Opens the html file
show(p)