# Exemple d'exécution de l'algorithme génétique

# Import functions from main.py
from main import *
import matplotlib.pyplot as plt
import numpy as np

# Define constants
length = 10
min = 0
max = 100
count = 100
target = 100
number_of_gen = 300

# Creating the population and mesuring its initial fitness
pop = population(count, length, min, max)
fitness_history = [grade(pop, target)]

# Iterating over generations
for gen in range(number_of_gen):
    pop = evolve(pop, target, min, max)
    fitness_history.append(grade(pop, target))

# Visualize the evolution of the population
Y = fitness_history
X = [i for i in range(len(Y))]
plt.title("Evolution of the population through generations")
plt.xlabel("Gen.")
plt.ylabel("Average fitness")
plt.plot(X, Y, "k-x")
plt.show()