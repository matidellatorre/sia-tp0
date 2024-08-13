import json
import sys
import csv

from src.catching import attempt_catch
from src.pokemon import PokemonFactory, StatusEffect
from src.plots import *
import numpy as np

FILENAME_EJ1 = "results/ej1.csv"
FILENAME_EJ1A = 'results/ej1a.csv'
FILENAME_EJ2A = 'results/ej2a.csv'
FILENAME_EJ2B = 'results/ej2b.csv'
FILENAME_EJ2C = 'results/ej2c.csv'
FILENAME_EJ2D = 'ej2d.csv'


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

def get_pokemon_by_status_effect(factory, config, status_effect):
    match status_effect:
        case 'NONE':
            return factory.create(config["pokemon"], 100, StatusEffect.NONE, 1)
        case 'FREEZE':
            return factory.create(config["pokemon"], 100, StatusEffect.FREEZE, 1)
        case 'POISON':
            return factory.create(config["pokemon"], 100, StatusEffect.POISON, 1)
        case 'BURN':
            return factory.create(config["pokemon"], 100, StatusEffect.BURN, 1)
        case 'PARALYSIS':
            return factory.create(config["pokemon"], 100, StatusEffect.PARALYSIS, 1)
        case 'SLEEP':
            return factory.create(config["pokemon"], 100, StatusEffect.SLEEP, 1)
        case _:
            raise Exception(f'Unknown status effect {status_effect}')


def ej2a():

    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(FILENAME_EJ2A, mode="w", newline="") as output:
        config = json.load(f)
        writer = csv.writer(output)
        writer.writerow(["ball", "NONE", "SLEEP", "PARALYSIS", "BURN", "POISON", "FREEZE"])

        for ball in config["pokeball"]:
            probs = []
            for status_effect in config["status_effects"]:
                pokemon = get_pokemon_by_status_effect(factory, config, status_effect)
                catched, prob = attempt_catch(pokemon, ball)
                probs.append(prob)
            writer.writerow([ball, *probs])       


def ej2b():
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(FILENAME_EJ2B, mode='w', newline='') as output:
        config = json.load(f)
        writer = csv.writer(output)
        balls = config["pokeballs"]
        catch_rate_names = list(map(lambda x : 'catch_rate_'+x, balls))
        writer.writerow(['hp', *catch_rate_names ])
        
        for hp in range(100, 0, -1):
            pokemon = factory.create(config["pokemon"], 100, StatusEffect.NONE, hp/100)
            catched_rates_list = []
            for ball in balls:
                accumulated = 0
                for i in range(100):
                    catched, _prob = attempt_catch(pokemon, ball)
                    if catched:
                        accumulated += 1
                catched_rates_list.append(accumulated/100)
            writer.writerow([hp, *catched_rates_list])


def ej2c():
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(FILENAME_EJ2C, mode='w', newline='') as output:
        config = json.load(f)
        writer = csv.writer(output)
        balls = config["pokeballs"]
        catch_rate_names = list(map(lambda x : 'catch_rate_'+x, balls))
        writer.writerow(['lvl', *catch_rate_names ])
        
        for lvl in range(100, 0, -1):
            pokemon = factory.create(config["pokemon"], lvl, StatusEffect.NONE, 1)
            catched_rates_list = []
            for ball in balls:
                accumulated = 0
                for i in range(100):
                    catched, _prob = attempt_catch(pokemon, ball)
                    if catched:
                        accumulated += 1
                catched_rates_list.append(accumulated/100)
            writer.writerow([lvl, *catched_rates_list])


def ej2d():
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(f"{sys.argv[1]}".split("/")[1].split(".")[0] + ".csv" , mode='w', newline='') as output:
        config = json.load(f)
        writer = csv.writer(output)
        writer.writerow(['Status Effect', 'HP Percentage', 'Pokeball Prob', 'Ultraball Prob', 'Heavyball Prob', 'Fastball Prob'])
        for pokemon in config:
            probs = []
            for ball in pokemon["pokeball"]:
                match pokemon["status_effect"]:
                    case 'NONE':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.NONE, pokemon["hp_percentage"])
                    case 'FREEZE':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.FREEZE, pokemon["hp_percentage"])
                    case 'POISON':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.POISON, pokemon["hp_percentage"])
                    case 'BURN':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.BURN, pokemon["hp_percentage"])
                    case 'PARALYSIS':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.PARALYSIS, pokemon["hp_percentage"])
                    case 'SLEEP':
                        current_pokemon = factory.create(pokemon["pokemon"], 100, StatusEffect.SLEEP, pokemon["hp_percentage"])
                    case _:
                        raise Exception(f'Unknown status effect {pokemon.status_effect}')
                catched, prob = attempt_catch(current_pokemon, ball)
                probs.append(prob)
            writer.writerow([pokemon["status_effect"], pokemon["hp_percentage"], *probs])


def ej2e():
    factory = PokemonFactory("pokemon.json")
    with open(f"{sys.argv[1]}", "r") as f, open(f"{sys.argv[1]}".split("/")[1].split(".")[0] + ".csv", mode='w', newline='') as output:
        config = json.load(f)
        writer = csv.writer(output)
        writer.writerow(['Level', 'Status Effect', 'HP Percentage', 'Pokeball Prob', 'Ultraball Prob', 'Heavyball Prob', 'Fastball Prob'])
        for pokemon in config:
            probs = []
            for ball in pokemon["pokeball"]:
                print(pokemon["level"])
                match pokemon["status_effect"]:
                    case 'NONE':
                        current_pokemon = factory.create(pokemon["pokemon"], pokemon["level"], StatusEffect.NONE, pokemon["hp_percentage"])
                    case 'FREEZE':
                        current_pokemon = factory.create(pokemon["pokemon"], pokemon["level"], StatusEffect.FREEZE, pokemon["hp_percentage"])
                    case 'POISON':
                        current_pokemon = factory.create(pokemon["pokemon"], pokemon["level"], StatusEffect.POISON, pokemon["hp_percentage"])
                    case 'BURN':
                        current_pokemon = factory.create(pokemon["pokemon"], pokemon["level"], StatusEffect.BURN, pokemon["hp_percentage"])
                    case 'PARALYSIS':
                        current_pokemon = factory.create(pokemon["pokemon"], pokemon["level"], StatusEffect.PARALYSIS, pokemon["hp_percentage"])
                    case 'SLEEP':
                        current_pokemon = factory.create(pokemon["pokemon"], pokemon["level"], StatusEffect.SLEEP, pokemon["hp_percentage"])
                    case _:
                        raise Exception(f'Unknown status effect {pokemon.status_effect}')
                catched, prob = attempt_catch(current_pokemon, ball)
                probs.append(prob)
            writer.writerow([pokemon["level"], pokemon["status_effect"], pokemon["hp_percentage"], *probs])


if __name__ == "__main__":
    # ej1(1000)
    # plot_ej1a(FILENAME_EJ1)
    # plot_ej1b(FILENAME_EJ1)
    #plot_ej1b(FILENAME_EJ1)

    #ej2a()
    # plot_ej2a(FILENAME_EJ1A)
    # plot_ej2b(FILENAME_EJ2D)

    # ej2b()
    # plot_ej2b(FILENAME_EJ2B)
    # ej2c()
    # plot_ej2c(FILENAME_EJ2C)

    # ej2d()
    # plot_ej2d(f"{sys.argv[1]}".split("/")[1].split(".")[0] + ".csv")

    ej2e()
    plot_ej2e(f"{sys.argv[1]}".split("/")[1].split(".")[0] + ".csv")