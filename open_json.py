import json
from types import SimpleNamespace
import matplotlib.pyplot as plt
import numpy as np

with open('all_artcles.json', encoding="utf8") as file: 
    data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))

for article in data:
    for graph in article.Graphs:
        jpg_graph_name = graph.Isotherms[0].FileName+"_f"+graph.Isotherms[0].FigureNumber
        title_name = "PDF file: "+article.FormalNicelyPDFName.replace("... .pdf","").replace("Data ","")+"\n"+"Figure "+graph.Isotherms[0].FigureNumber 
        for isotherm in graph.Isotherms:        
            plt.scatter(isotherm.XAxisData, isotherm.YAxisData, label = isotherm.SampleName)

        plt.grid(color='black', linestyle='-', linewidth=0.1, alpha=0.8)
        plt.legend(borderaxespad=0, bbox_to_anchor=(1.04, 1))
        plt.xlabel('Relative Pressure P/Po')
        plt.ylabel('Volume adsorbed [cm3/g]')
        plt.title(title_name)
        plt.xticks(np.arange(graph.Isotherms[0].MinX, graph.Isotherms[0].MaxX + 1, 0.1))
        plt.yticks()
        plt.axis((graph.Isotherms[0].MinX, graph.Isotherms[0].MaxX, graph.Isotherms[0].MinY, graph.Isotherms[0].MaxY)) #x1,x2,y1,y2
        plt.savefig(f'graphs/{jpg_graph_name}.jpg', dpi=700 ,bbox_inches="tight")
        # plt.show()
        plt.clf()
        print(f"{isotherm.FileName} ---> Figure {isotherm.FigureNumber}        {isotherm.SampleName}      !!!SAVED!!!!")









