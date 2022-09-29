import pandas as pd
import numpy as np

class analyse:

    def recentanalysis(filename):
        r = pd.read_csv(filename)
        return(r['Keyword'].tail(5).tolist())
       
    def toptenanalysis(filename):
        r = pd.read_csv(filename)
        return(r['Keyword'].value_counts()[:10].index.tolist())