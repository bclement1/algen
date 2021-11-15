# Algorithme génétique - sélection empirique dans un champ de maïs

# Importation
import random
random.seed(3)
from random import randint, random
import numpy as np

# Définition des fonctions principales

def individual(min, max):
    # Un individu est un épi de maïs, caractérisé par sa position 2D et son rendement
    return randint(min, max)

def population(min, max, lx, ly):
    # La population est un champ constitué d'épis de maïs
    # lx, ly: longueur et largeur du champ, respectivement
    pop = np.array([[individual(min, max) for i in range(lx)] for j in range(ly)], dtype = int)
    return pop

def grade(pop, max, lx, ly):
    # Calcul de la performance globale du champ à une génération donnée
    total_yield = 0
    number_of_indiv = lx*ly
    for i in range(lx):
        for j in range(ly):
            ind_yield = pop[i][j]
            total_yield += ind_yield
    field_fitness = (lx*ly*max - total_yield)/(lx*ly*max)*100 # écart relatif au champ optimal (en pourcentage)
    return field_fitness

def evolve(pop, min, max, lx, ly, retain_length = 0.1, random_select = 0.2, mutate = 0.1, verbose = 0):
    """
    Cette fonction prend en entrée les paramètres :
    pop : la population au tour N
    min, max : les valeurs minimale et maximale du rendement possibles pour un épi
    lx, ly : les dimensions du champ
    retain_length : la proportion des meilleurs épis à garder d'une génération à l'autre
    random_select : la proportion d'épis à retenir d'un tour à l'autre (indépendamment de leur rendement)
    mutate : le taux de mutation (évolution aléatoire du rendement) chez la population
    eps : paramètre de croisement
    """
    # Classement des individus
    grades = []
    for i in range(lx):
        for j in range(ly):
            ind_yield = pop[i][j]
            grades.append([ind_yield, i, j]) # l'évaluation des individus se fait directement via leur rendement
    f = lambda x : x[0]
    ranking = sorted(grades, key = f, reverse = True) # classement des épis par ordre décroissant de rendement
    retain_length = int(len(grades)*retain_length)
    # On garde une proportion des meilleurs individus pour peupler la prochaine génération
    parents = ranking[:retain_length]
    if verbose == 1:
        print(len(parents), " épis ont été sélectionnés comme les plus performants.")
    # Ajout d'épi de maïs au hasard parmi les autres individus pour la diversité génétique
    for individual in ranking[retain_length:]:
        if random_select > random():
            parents.append(individual)
    if verbose == 1:
        print(len(parents), " épis ont été sélectionnés après diversité génétique.")
    # Mutation de certains parents au hasard
    for individual in parents:
        if mutate > random():
            new_yield = randint(min, max)
            individual[0] = new_yield
    # Croisement des parents pour créer la nouvelle génération
    parents_length = len(parents)
    parents_positions = [[indiv[1], indiv[2]] for indiv in parents]
    children = []
    # On itère sur les épis du champ
    for i in range(lx):
        for j in range(ly):
            if not [i, j] in parents_positions:
                # On choisit un épi père et un épi mère parmi les parents
                ind_male = randint(0, parents_length - 1)
                ind_female = randint(0, parents_length - 1)
                while ind_male == ind_female:
                    # Il faut que les épis parents soient différents
                    ind_male = randint(0, parents_length - 1)
                    ind_female = randint(0, parents_length - 1)
                # Puis on hybride les parents pour créer un enfant épi de maïs :)
                male = parents[ind_male]
                female = parents[ind_female]
                if male[0] >= female[0]:
                    child_yield = randint(female[0], male[0])
                    child = [child_yield, i, j]
                elif female[0] > male[0]:
                    child_yield = randint(male[0], female[0])
                    child = [child_yield, i, j]
                # Que l'on l'ajoute aux enfants
                children.append(child)
    # Et enfin on ajoute les hybridés aux parents de la prochaine génération
    parents.extend(children)
    # Peuplement de la population par la nouvelle génération
    for indiv in parents:
        pop[indiv[1]][indiv[2]] = indiv[0] 
    return pop
