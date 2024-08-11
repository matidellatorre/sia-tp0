import json
import sys
import csv

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
from src.plots import *


FILENAME_EJ1 = "results/ej1.csv"


def ej1(ball_throws=100):
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(FILENAME_EJ1, mode="w", newline="") as output:
        config = json.load(f)
        writer = csv.writer(output)
        writer.writerow(["pokemon", "pokeball", "ultraball", "heavyball", "fastball"])
        for pokemon in config:
            probs = []
            for ball in pokemon["pokeball"]:
                accumulated = 0
                for _ in range(ball_throws):
                    current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.NONE, 1)
                    catched, _ = attempt_catch(current_pokemon, ball)
                    if catched:
                        accumulated += 1
                probs.append(accumulated / ball_throws)

            writer.writerow([pokemon["pokemon"], *probs])


if __name__ == "__main__":
    # ej1(1000)
    # plot_ej1a(FILENAME_EJ1)
    plot_ej1b(FILENAME_EJ1)
