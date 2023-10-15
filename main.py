import sympy as sp
import numpy as np

x = sp.Symbol("x")

img = sp.plotting.plot("x**3","x",(x,-2,2),legend=True)
img.save("graph.png")