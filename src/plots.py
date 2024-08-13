import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

DATASET_QTY = 100


def plot_ej1a(filename):
    df = pd.read_csv(filename)
    pokemons = df["pokemon"]
    balls = {
        "Pokeball": df["pokeball"],
        "Heavyball": df["heavyball"],
        "Fastball": df["fastball"],
        "Ultraball": df["ultraball"],
    }

    x = np.arange(len(pokemons))
    width = 0.2
    multiplier = 0

    _, ax = plt.subplots(layout="constrained")

    for attribute, measurement in balls.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=4)
        multiplier += 1

    ax.set_ylabel("Probabilidad de captura")
    ax.set_xticks(x + 1.5 * width, pokemons.map(lambda x: x.capitalize()))
    ax.legend(loc="upper left", ncols=4)
    ax.set_ylim(0, 1)
    ax.set_yticks(np.arange(0, 1.1, 0.1)) 

    plt.show()


def plot_ej1b(filename):
    df = pd.read_csv(filename)
    
    fig, ax = plt.subplots(nrows=2, ncols=3, layout="constrained")
    
    positions = [[0,0], [0,1], [0,2], [1,0], [1,1]]
    
    for i, row in df.iterrows():
        axis = ax[positions[i]]
        
        pokeball_probability = row["pokeball"]
        ultraball_probability = row["ultraball"]
        heavyball_probability = row["heavyball"]
        fastball_probability = row["fastball"]
        
        balls = {
            "Ultraball": ultraball_probability / pokeball_probability,
            "Heavyball": heavyball_probability / pokeball_probability,
            "Fastball": fastball_probability / pokeball_probability
        }
        
        for j, (ball, probability) in enumerate(balls.items()):
            rect = axis.bar(j + 1, probability, label=ball)
            axis.bar_label(rect, padding=2)
            axis.axhline(y=1, color='k', linestyle='--')

        
        axis.set_ylabel("Efectividad de captura comparado con Pokeball")
        axis.set_xlabel(row["pokemon"].capitalize())
        axis.legend(loc="lower left", ncols=3)
        axis.set_xticks([])
        
    fig.delaxes(ax[1, 2])
    
def plot_ej2a(filename):
    df = pd.read_csv(filename)
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(df['ball'])-1)

    width = 0.15
    
    def normalize(s):
        return s[1:].div(s[0])

    ax.bar(x - 2 * width, normalize(df['NONE']), width, label='NONE', color='gray')
    ax.bar(x - width, normalize(df["SLEEP"]), width, label='SLEEP', color='blue')
    ax.bar(x, normalize(df['PARALYSIS']), width, label='PARALYSIS', color='yellow')
    ax.bar(x + width, normalize(df['BURN']), width, label='BURN', color='red')
    ax.bar(x + 2 * width, normalize(df['POISON']), width, label='POISON', color='purple')
    ax.bar(x + 3 * width, normalize(df['FREEZE']), width, label='FREEZE', color='cyan')
    
    ax.axhline(y=1, color='k', linestyle='--')
    ax.set_xlabel('Pokéball')
    ax.set_ylabel('Probabilidad de captura (relativa a la pokeball)')
    ax.set_title('Probabilidad de captura según el estado del Pokémon y la Pokébola')
    ax.set_xticks(x)
    ax.set_xticklabels(df['ball'][1:])
    ax.legend()
    plt.show()

def plot_ej2b(filename):
    df = pd.read_csv(filename)
    catch_rate_pokeball = df['catch_rate_pokeball']
    catch_rate_ultraball = df['catch_rate_ultraball']
    catch_rate_fastball = df['catch_rate_fastball']
    catch_rate_heavyball = df['catch_rate_heavyball']

    hps = df['hp']
    
    plt.figure(figsize=(10, 6))

    plt.scatter(hps, catch_rate_pokeball, color='red', label='Pokeball')
    plt.plot(hps, catch_rate_pokeball, color='red')
    plt.scatter(hps, catch_rate_fastball, color='orange', label='Fastball')
    plt.plot(hps, catch_rate_fastball, color='orange')
    plt.scatter(hps, catch_rate_ultraball, color='blue', label='Ultraball')
    plt.plot(hps, catch_rate_ultraball, color='blue')
    plt.scatter(hps, catch_rate_heavyball, color='green',label='Heavyball')
    plt.plot(hps, catch_rate_heavyball, color='green')

    plt.title('Salud vs P. de captura')
    plt.ylabel('Probabilidad de captura')
    plt.xlabel('Salud')
    plt.legend()
    plt.show()

def plot_ej2c(filename):
    df = pd.read_csv(filename)
    catch_rate_pokeball = df['catch_rate_pokeball']
    catch_rate_ultraball = df['catch_rate_ultraball']
    catch_rate_fastball = df['catch_rate_fastball']
    catch_rate_heavyball = df['catch_rate_heavyball']

    lvls = df['lvl']
    
    plt.figure(figsize=(10, 6))

    plt.scatter(lvls, catch_rate_pokeball, color='red', marker='o', label='Pokeball')
    plt.plot(lvls, catch_rate_pokeball, color='red')
    plt.scatter(lvls, catch_rate_fastball, color='orange', marker='s', label='Fastball')
    plt.plot(lvls, catch_rate_fastball, color='orange')
    plt.scatter(lvls, catch_rate_ultraball, color='blue', marker='x', label='Ultraball')
    plt.plot(lvls, catch_rate_ultraball, color='blue')
    plt.scatter(lvls, catch_rate_heavyball, color='green', marker='+', label='Heavyball')
    plt.plot(lvls, catch_rate_heavyball, color='green')

    plt.title('Nivel vs P. de captura')
    plt.ylabel('Probabilidad de captura')
    plt.xlabel('Nivel')
    plt.legend()
    plt.show()


def plot_ej2d(filename):
    df = pd.read_csv(filename)
    status_effects = df['Status Effect']
    balls = {
        "Pokeball": df["Pokeball Prob"],
        "Heavyball": df["Heavyball Prob"],
        "Fastball": df["Fastball Prob"],
        "Ultraball": df["Ultraball Prob"],
    }

    x = np.arange(len(status_effects))
    width = 0.2
    multiplier = 0
    max_measurement = 0
    _, ax = plt.subplots(layout="constrained")

    for attribute, measurement in balls.items():
        if measurement.max() > max_measurement:
            max_measurement = measurement.max()
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=4)
        multiplier += 1

    ax.axhline(y=max_measurement, color='k', linestyle='--')
    ax.set_ylabel("Probabilidad de captura")
    ax.set_xticks(x + 1.5 * width, status_effects.map(lambda x: x.lower().capitalize()))
    ax.legend(loc="upper left", ncols=4)
    ax.set_ylim(0, 1)
    ax.set_yticks(np.arange(0, 1.1, 0.1))

    plt.show()


