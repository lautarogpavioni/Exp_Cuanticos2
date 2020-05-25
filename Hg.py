import matplotlib.pyplot as plt
import pandas as pd

Hg=pd.read_csv("hg2.txt", header=0, decimal=',', delim_whitespace=True, names=["ca","cu"])

Hg.plot("ca","cu")
plt.show()
