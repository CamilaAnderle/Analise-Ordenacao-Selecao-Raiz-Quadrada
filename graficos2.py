# -*- coding: utf-8 -*-
"""graficos2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LRBrUzsNdt_d6EADBnzzJoFy7n6PAg6N
"""

import matplotlib.pyplot as plt
import numpy as np
import math

#Heap
qbb = np.array(['10⁴','10⁵','10⁶', '10⁷', '10⁸'])
tbb = np.array([math.log(x) for x in [0.062, 0.26, 4.59, 215.67, 9418.78]])

plt.plot(qbb, tbb,  label='Heap')


#BUBBLE

qbs = np.array(['10⁴','10⁵','10⁶', '10⁷', '10⁸'])
tbs = np.array([ math.log(x) for x in [ 0.048, 0.29, 6.46, 329.09, 11959.82]])

plt.plot( qbs, tbs, label = 'Bubblesort')

plt.title('Heap vs Bubblesort')
plt.ylabel('Tempo em escala logartimica(segundos)', fontsize = 12)
plt.xlabel('Tamanho da Sequência(n)', fontsize = 12)
plt.legend()


plt.show()