import numpy as np
import mne
import pickle
from pathlib import Path

# sample_data_raw_file=('imagery)
data=mne.io.read_raw_persyst('./imageryruns/imageryS001R03.dat')

# with open('./imageryruns/imageryS001R03.dat', 'rb',0) as f:
#     y = pickle.load(f, encoding='latin1')

# path = Path('./imageryruns/imageryS001R03.dat')
# content = path.read_bytes()
# data = pickle.loads(content, encoding='ISO-8859-1')

# data = pickle.load(open('./imageryruns/imageryS001R03.dat', "rb"))
print(data)