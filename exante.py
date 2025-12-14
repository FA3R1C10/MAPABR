#%%
from bcb import sgs, Expectativas as ep
import pandas as pd
import numpy as np
import datetime as dt
#%%
# 1) Selic meta atual (série 432)
selic = sgs.get(432, "2020-01-01", dt.datetime.today())
selic_atual = float(selic.iloc[-1, 0])
