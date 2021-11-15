# Algorithme génétique - somme des listes de 5-uplets

# Import libraries
from random import randint, random

# Define main functions
def individual(length, min, max):
    # Create a member of the population
    return [randint(min, max) for x in range(length)]


def population(count, length, min, max):
    # Create a number of individuals (i.e. a population).
    # count: the number of individuals in the population
    return [individual(length, min, max) for x in range(count)]


def fitness(individual, target):
    # Determine the fitness of an individual. The less the better.
    # individual: the individual to evaluate
    # target: the target number individuals are aiming at
    
    sum = 0
    for val in individual:
        sum+= val
    return abs(target - sum)


def grade(pop, target):
    # Calculate the average fitness of a population
    avg_fitness = 0
    for indiv in pop:
        avg_fitness += (fitness(indiv, target))/len(pop)
    return avg_fitness


def evolve(pop, target, min, max, retain_length = 0.2, random_select = 0.05, mutate = 0.01):
    # Start by grading all individuals
    graded = [(fitness(indiv, target), indiv) for indiv in pop]
    ranking = [graded_indiv[1] for graded_indiv in sorted(graded)]
    retain_length = int(len(graded)*retain_length)
    # Keep a proportion of the best performing individuals to form the next generation
    parents = ranking[:retain_length]
    # Randomly add other individuals to promote genetic diversity
    for individual in ranking[retain_length:]:
        if random_select > random():
            parents.append(individual)
    # Mutate some parents individuals
    for individual in parents:
        if mutate > random():
            position_to_mutate = randint(0, len(individual) - 1)
            individual[position_to_mutate] = randint(min, max)
    # Breed parents to create children
    parents_length = len(parents)
    still_to_create = len(pop) - parents_length
    children = []
    while len(children) < still_to_create:
        # Pick a male and a female within the parents population
        ind_male = randint(0, parents_length - 1)
        ind_female = randint(0, parents_length - 1)
        if ind_male != ind_female:
            male = parents[ind_male]
            female = parents[ind_female]
            half = int(len(male)/2)
            # The child is made of half its parents' genetic material
            child = male[:half] + female[half:]
            children.append(child)     
    parents.extend(children)
    return parents