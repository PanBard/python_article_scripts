import numpy as np
import matplotlib.pyplot as plt
import json
from types import SimpleNamespace
import datetime

with open('all_artcles.json', encoding="utf8") as file: 
    data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))

x=data[1].Graphs[0].Isotherms[1].XAxisData
y=data[1].Graphs[0].Isotherms[1].YAxisData

data_for_table=[]
for i in range(len(x)):
    data_for_table.append([x[i],y[i]])

title_text = data[0].Graphs[0].Isotherms[0].SampleName
footer_text = datetime.datetime.now()
fig_background_color = 'skyblue'
fig_border = 'steelblue'
fig_size_y = (len(x)*10)/40 #to scale figure in height bc data is not even in all isotherms
print(fig_size_y)
column_headers = ['X','Y']# Table data needs to be non-numeric text. Format the data
plt.figure(linewidth=2, tight_layout={'pad':1}, figsize=(5,fig_size_y))
the_table = plt.table(cellText=data_for_table, rowLoc='right', colLabels=column_headers, loc='center')
the_table.scale(1, 1.5)# Make the rows taller (i.e., make cell y scale larger).
ax = plt.gca()
ax.get_xaxis().set_visible(False)# Hide axes
ax.get_yaxis().set_visible(False)
plt.box(on=None)# Hide axes border
plt.suptitle(title_text)# Add title
plt.figtext(0.95, 0.001, footer_text, horizontalalignment='right', size=6, weight='light')# Add footer
plt.draw()# Without plt.draw() here, the title will center on the axes and not the figure.
fig = plt.gcf()
plt.savefig('myDemo.png', dpi=300)