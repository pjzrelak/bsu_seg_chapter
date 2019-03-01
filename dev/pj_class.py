# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

class SinePlot:
        

    def __init__(self, x, f):
        self.x = x
        self.freq = f
        self.fx = np.sin(2 * np.pi * self.x * self.freq)
        self.table = pd.DataFrame(self.fx, self.x)

    def __repr__(self):
        
        return repr([self.table])
    


x = np.linspace(0, 100, num=50)
x = x * np.pi

test = SinePlot(x, 5)
print(test)

plt.plot(test.x, test.fx)