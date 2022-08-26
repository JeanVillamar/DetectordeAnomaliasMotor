from pathlib import Path
from scipy.io import wavfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, IPython.display as ipd
import librosa, librosa.display



# leer los archivos y guardarlos
kick_signals = [
    librosa.load(p)[0] for p in Path().glob('conFalla.38fulubt.s1')
]
snare_signals = [
    librosa.load(p)[0] for p in Path().glob('SinFalla.38ftfhv.s2')
]

#print(kick_signals[0].dtype)
#ipd.Audio('conFalla.38fulubt.s1')
len(kick_signals)

plt.figure(figsize=(15, 6))
for i, x in enumerate(kick_signals):
    plt.subplot(2, 5, i+1)
    librosa.display.waveplot(x[:10000])
    plt.ylim(-1, 1)
    plt.tight_layout()