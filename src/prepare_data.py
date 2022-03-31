
"""
Eelke-171027-090003 - 1.1 (PR) - box1 (Dv1B and Dv2B) L=cas
Eelke-171027-090003 - 1.2 (PR) - box2 (Dv3B and Dv4B) R=cas
Eelke-171027-102614 - 1.3 (PR) - box1 (Dv1B and Dv2B) R=cas
Eelke-171027-102614 - 1.4 (PR) - box2 (Dv3B and Dv4B) L=cas
Eelke-171027-094359 - 1.5 (NR) - box1 (Dv1B and Dv2B) L=cas
Eelke-171027-094359 - 1.6 (NR) - box2 (Dv3B and Dv4B) R=cas
Eelke-171027-111329 - 1.7 (NR) - box1 (Dv1B and Dv2B) R=cas
Eelke-171027-111329 - 1.8 (NR) (no signal)

"""
# %%

import numpy as np
import matplotlib.pyplot as plt

import tdt

import trompy as tp

%matplotlib inline

tank = "..\\data\\Eelke-171027-090003"

data = tdt.read_block(tank)
# %%



blue = data.streams.Dv1B.data
uv = data.streams.Dv1B.data

fs = data.streams.Dv1B.fs

processed_signal = tp.processdata(blue, uv, method="lerner", fs=fs, normalize=True)

f, ax = plt.subplots()
ax.plot(processed_signal)

cas_sipper = data.epocs.LT1_.onset
cas_licks = data.epocs.LL1_.onset

malt_sipper = data.epocs.RT1_.onset
malt_licks = data.epocs.RL1_.onset


# %%
