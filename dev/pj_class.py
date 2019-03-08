# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

class SinePlot:
        

    def __init__(self, x, f, xlabel='xlabel', ylabel='ylabel',sym='-',title='untitled', **kwargs):
        self.x = x
        self.freq = f
        self.sym = sym
        self.xtitle = xlabel
        self.ytitle = ylabel
        self.title = title
        
    def fx(self):
        self.fx = np.sin(2 * np.pi * self.x * self.freq)
        return self.fx
        
    def table(self): 
        self.table = pd.DataFrame(self.fx, self.x)
        return self.table
        
    
    def mkFig(self):
        self.fig = plt.plot(self.x, self.fx(), self.sym)
        plt.xlabel(self.xtitle)
        plt.ylabel(self.ytitle)
        plt.title(self.title)
        plt.show()
        return self.fig
    


x = np.linspace(0, 100, num=50)
x = x * np.pi

test = SinePlot(x, 5)
#test.mkFig()
