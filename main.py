import json
import sys
import csv

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
from src.plots import plot_ej1a

FILENAME_EJ1A = 'ej1a.csv'

def ej1a():
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(FILENAME_EJ1A, mode='w', newline='') as output:
        config = json.load(f)
        writer = csv.writer(output)
        writer.writerow(['Pokemon', 'Pokeball Prob', 'Ultraball Prob', 'Heavyball Prob', 'Fastball Prob'])
        for pokemon in config:
            probs = []
            for ball in pokemon["pokeball"]:
                accumulated = 0
                for i in range(100):
                    current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.NONE, 1)
                    catched, _prob = attempt_catch(current_pokemon, ball)
                    if catched:
                        accumulated += 1
                probs.append(accumulated/100)

            writer.writerow([pokemon["pokemon"], *probs])


if __name__ == "__main__":
    ej1a()
    plot_ej1a(FILENAME_EJ1A)