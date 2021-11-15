# Exemple d'exécution de l'algorithme génétique

# Import functions from main.py
from main import *
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Constantes
min = 1
max = 10
lx = 100
ly = 100
number_of_gen = 30

def show_fitness_history(min, max, lx, ly, number_of_gen, retain_length = 0.1, random_select = 0.1, mutate = 0.2):
    # Création du champ
    pop = population(min, max, lx, ly)
    gr = grade(pop, max, lx, ly)
    fitness_history = [grade(pop, max, lx, ly)]

    # Itération sur les générations
    for gen in range(number_of_gen):
        pop = evolve(pop, min, max, lx, ly, retain_length = retain_length, random_select = random_select, mutate = mutate)
        fitness_history.append(grade(pop, max, lx, ly))

    Y = fitness_history
    X = [i for i in range(len(Y))]
    plt.title(
    "Evolution of the population through generations. retain length = {} ; random select = {} ; mutation = {}"
    .format(retain_length, random_select, mutate)
    )
    plt.xlabel("Gen.")
    plt.ylabel("Average fitness")
    plt.plot(X, Y, "k-x")
    plt.show()

# show_fitness_history(min, max, lx, ly, number_of_gen)

def build_pop(min, max, lx, ly, number_of_gen, retain_length = 0.1, random_select = 0.1, mutate = 0.2):
    tab = np.zeros(shape = (number_of_gen, lx, ly)) # là où on stocke les générations
    # Création du champ
    pop = population(min, max, lx, ly)

    # Itération sur les générations
    for gen in range(number_of_gen):
        tab[gen] = pop
        pop = evolve(pop, min, max, lx, ly, retain_length = retain_length, random_select = random_select, mutate = mutate)
    return tab

def return_pop(gen):
    ax.cla()
    sns.heatmap(tab[gen],
                ax = ax,
                cbar = True,
                cmap = "Greens",
                cbar_ax = cbar_ax,
                vmin = tab.min(),
                vmax = tab.max())

'''
tab = build_pop(min, max, lx, ly, number_of_gen, retain_length = 0.2, random_select = 0.05, mutate = 0.05)
grid_kws = {'width_ratios': (0.9, 0.05), 'wspace': 0.2}
fig, (ax, cbar_ax) = plt.subplots(1, 2, gridspec_kw = grid_kws, figsize = (12, 8))
anim = FuncAnimation(fig = fig, func = return_pop, frames = number_of_gen, interval = 10000)
plt.show()
'''
show_fitness_history(min, max, lx, ly, number_of_gen)