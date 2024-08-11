import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot_ej1a(filename):
    df = pd.read_csv(filename)
    pokemons = df['Pokemon']
    balls = {
        'Pokeball': df['Pokeball Prob'],
        'Heavyball': df['Heavyball Prob'],
        'Fastball': df['Fastball Prob'],
        'Ultraball': df['Ultraball Prob'],
    }

    x = np.arange(len(pokemons))
    width = 0.2
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in balls.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=4)
        multiplier += 1

    ax.set_ylabel('Probabilidad de captura')
    ax.set_xticks(x + 1.5 * width, pokemons.map(lambda x: x.capitalize()))
    ax.legend(loc='upper left', ncols=4)
    ax.set_ylim(0, 1)
    ax.set_yticks(np.arange(0, 1.1, 0.1)) 

    plt.show()