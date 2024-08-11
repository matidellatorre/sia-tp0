import json
import sys
import csv

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
from src.plots import *

FILENAME_EJ2D = 'ej2d.csv'
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


def ej2d():
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(FILENAME_EJ2D, mode='w', newline='') as output:
        config = json.load(f)
        writer = csv.writer(output)
        writer.writerow(['Status Effect', 'Pokeball Prob', 'Ultraball Prob', 'Heavyball Prob', 'Fastball Prob'])
        for pokemon in config:
            current_pokemon = None
            for ball in pokemon["pokeball"]:
                probs = []
                match pokemon.status_effect:
                    case 'NONE':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.NONE, 1)
                    case 'FREEZE':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.FREEZE, 1)
                    case 'POISON':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.POISON, 1)
                    case 'BURN':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.BURN, 1)
                    case 'PARALYSIS':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.PARALYSIS, 1)
                    case 'SLEEP':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.SLEEP, 1)
                    case _:
                        raise Exception(f'Unknown status effect {pokemon.status_effect}')
                catched, prob = attempt_catch(current_pokemon, ball)
                probs.append(prob)

            writer.writerow([pokemon["status_effect"], *probs])


if __name__ == "__main__":
    # ej1(1000)
    # plot_ej1a(FILENAME_EJ1)
    plot_ej1b(FILENAME_EJ1)
