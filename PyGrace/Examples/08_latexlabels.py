import sys
sys.path.append('../../')
sys.path.append('../')

from PyGrace.grace import Grace
from PyGrace.graph import Graph
from PyGrace.drawing_objects import DrawText, DrawLine

from PyGrace.Extensions.distribution import CDFGraph, PDFGraph
from PyGrace.Extensions.latex_string import LatexString, CONVERT

# this is the step where YOU do the analysis
import example_tools
cdf, pdf = example_tools.latexlabels()
                
class Graph1(CDFGraph):
    def __init__(self, *args, **kwargs):
        CDFGraph.__init__(self, *args, **kwargs)
        self.set_view(0.15, 0.15, 0.6, 0.6)
        self.world.xmin = 0
        self.world.xmax = 10
        self.xaxis.label.text = \
            LatexString(r'\6X\4 = $\langle$ \xb\4\sj\N $\rangle$')

class Graph2(PDFGraph):
    def __init__(self, *args, **kwargs):
        PDFGraph.__init__(self, *args, **kwargs)
        self.set_view(0.75, 0.15, 1.2, 0.6)
        self.world.xmin = 0
        self.world.xmax = 10
        self.xaxis.label.text = \
            LatexString(r'\6X\4 = $\langle$ \xb\4\sj\N $\rangle$')

# make the plot
grace = Grace()

grace.add_drawing_object(DrawText, text='Currently available LaTeX characters',
                         x=0.08, y=0.92, char_size=0.8, font=6, just=4)
grace.add_drawing_object(DrawLine, start=(0.08, 0.915), end=(1.22, 0.915),
                         linewidth=1.0)

mod = (len(CONVERT) / 5) + 1
for index, (latexString, graceString) in enumerate(sorted(CONVERT.items())):
    x = 0.1 + 0.20 * (index / mod)
    y = 0.895 - 0.0225 * (index % mod)
    latexString = latexString.replace('\\', r'\\')
    grace.add_drawing_object(DrawText, text=graceString, x=x, y=y,
                             char_size=0.6, font=4, just=1)
    grace.add_drawing_object(DrawText, text=latexString, x=x+0.01, y=y,
                             char_size=0.6, font=4, just=0)

grace.add_drawing_object(DrawLine,
                         start=(0.08, 0.895-0.0225*(mod-1)-0.01),
                         end=(1.22, 0.895-0.0225*(mod-1)-0.01),
                         linewidth=1.0)

graph1 = grace.add_graph(Graph1, cdf, True)

graph2 = grace.add_graph(Graph2, pdf)

grace.write_file('08_latexlabels.agr')

