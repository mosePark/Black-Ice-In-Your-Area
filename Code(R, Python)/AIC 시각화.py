import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Model = ["Model0","Model1","Model2","Model3","Model4","Model5","Model6", "Model7","Model8","Model9","Model10","Model11","Model12"]

AIC = [134483, 134432, 134216, 133618, 133620, 133555, 133279, 131042, 118576, 118467, 117554, 115011, 114963]

plt.plot(Model, AIC)
