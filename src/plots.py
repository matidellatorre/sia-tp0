import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_ej1a(filename):
    df = pd.read_csv(filename)
    fig, ax = plt.subplots()
    pokemons = df['Pokemon']
    balls = {
        'Pokeball Probability': df['Pokeball Prob'],
        'Heavyball Probability': df['Heavyball Prob'],
        'Fastball Probability': df['Fastball Prob'],
        'Ultraball Probability': df['Ultraball Prob'],
    }
    x = np.arange(len(pokemons))
    width = 1
    multiplier = 0
    for label, data in balls.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, data, width, label=label)
        ax.bar_label(rects, padding=4)
        multiplier += 1

    plt.show()