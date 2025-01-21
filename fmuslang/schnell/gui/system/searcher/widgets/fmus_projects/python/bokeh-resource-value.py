

from bokeh.models import ColumnDataSource, LabelSet
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6
from bokeh.models import NumeralTickFormatter

# Data for countries and resource values
countries = ["Russia", "United States", "Saudi Arabia", "Canada", "Iran", "China", "Brazil", "Australia", "Iraq", "Venezuela"]
resource_values = [75, 45, 34.4, 33.2, 27.3, 23, 21.8, 19.9, 15.9, 14.3]

# Create a ColumnDataSource
source = ColumnDataSource(data=dict(countries=countries, resource_values=resource_values))

# Define the output file
output_file("resource_values_bar_chart.html")

# Create a figure object
p = figure(x_range=countries, height=400, width=800, title="Natural Resource Values by Country (in Trillion USD)",
           toolbar_location=None, tools="")

# Create the bar chart
bars = p.vbar(x='countries', top='resource_values', width=0.5, source=source,
              line_color='white', fill_color=factor_cmap('countries', palette=Spectral6, factors=countries))

# Add value labels on top of each bar
labels = LabelSet(x='countries', y='resource_values', text='resource_values',
                  text_font_size='8pt', level='glyph', x_offset=-12, y_offset=0, source=source,) #render_mode='canvas')
				  
#labels = LabelSet(x='countries', y='resource_values', text='resource_values',
#                  level='glyph', x_offset=-15, y_offset=0, source=source, render_mode='canvas')

p.add_layout(labels)

# Format y-axis tick labels as billions
p.yaxis[0].formatter = NumeralTickFormatter(format="$0.0T")

# Rotate x-axis labels
p.xaxis.major_label_orientation = 1.2

# Show the bar chart
show(p)

