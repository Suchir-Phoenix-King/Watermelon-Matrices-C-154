# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 17:29:18 2022

@author: PC_RC
"""

import matplotlib
import matplotlib.pyplot as plt
data = [
        [10,10,10,10,10,10,10,10,10,7,10,10,10,10],
        [10,10,10,10,10,10,10,10,9,8,7,10,10,10],
        [10,10,10,10,10,10,10,9,9,9,8,7,10,10],
        [10,10,10,10,10,10,9,9,4,9,9,8,7,10],
        [10,10,10,10,10,9,9,9,9,9,9,8,7,10],
        [10,10,10,10,9,9,9,9,4,9,9,8,7,10],
        [10,10,10,9,9,9,9,9,9,9,9,8,7,10],
        [10,10,9,9,9,9,4,9,9,9,9,8,7,10],
        [10,9,4,9,4,9,9,9,9,9,8,7,10,10],
        [7,8,9,9,9,9,9,9,9,8,7,10,10,10],
        [10,7,8,9,9,9,9,9,8,7,10,10,10,10],
        [10,10,7,8,8,8,8,8,7,10,10,10,10,10],
        [10,10,10,7,7,7,7,7,10,10,10,10,10,10],
        
        ]
plt.imshow(data, cmap = "nipy_spectral")
plt.show()