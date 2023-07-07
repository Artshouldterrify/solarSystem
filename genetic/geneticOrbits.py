import random as rand
import solarSystem as drawingScript
import systemSim as sim
import time
import turtle


# fitness function for the genetic algorithm
def fitness(individual, solar_system_inst):
    solar_suns = (sim.sun(solar_syst, mass=10_000, position=(-400, 0), velocity=(0, 2.5)),
                  sim.sun(solar_syst, mass=10_000, position=(400, 0), velocity=(0, -2.5)))
    solar_planet = sim.planet(solar_system_inst, individual[0], (individual[1], individual[2]), (individual[3],
                                                                                                 individual[4]))
    time_alive = solar_system_inst.simulate()
    solar_system_inst.remove_body(solar_planet)
    solar_system_inst.remove_body(solar_suns[0])
    solar_system_inst.remove_body(solar_suns[1])
    return time_alive


# tournament
def tournament(tournament_set, solar_system_inst):
    best_cand = tournament_set[0]
    best_fitness = fitness(tournament_set[0], solar_system_inst)
    for candidate in tournament_set:
        fit = fitness(candidate, solar_system_inst)
        if fit > best_fitness:
            best_cand = candidate
            best_fitness = fit
    return best_cand


# selection: tournament selection with parameter k
def selection(k, population, solar_system_inst):
    tournament_pop = list()
    for i in range(k):
        index = rand.randint(0, len(population) - 1)
        tournament_pop.append(population[index])
    best_in = tournament(tournament_pop, solar_system_inst)
    return best_in


# creation of new generation
def crossover(crossover_p, parent_1, parent_2):
    num = rand.randint(0, 100)
    c_1, c_2 = parent_1.copy(), parent_2.copy()
    if num <= (crossover_p * 100):
        for i in range(1, len(c_1)):
            Y = (rand.randint(0, 100) - 50) / 100
            c_1[i] = parent_1[i] + Y * parent_2[i]
            c_2[i] = parent_2[i] + Y * parent_1[i]
    return c_1, c_2


# mutation: randomly pick a position and change
def mutation(individual, mutation_p):
    num = rand.randint(0, 100)
    if num <= (mutation_p * 100):
        pos = rand.randint(0, len(individual) - 1)
        Y = rand.randint(1, 30) - 15
        individual[pos] += individual[pos] * Y / 100
    return individual


# genetic algorithm main function
def genetic(epochs, cross_rate, mut_rate, pop_size, solar_system_inst):
    # generate initial population
    population = list()
    for i in range(pop_size):
        new_individual = list()
        new_individual.append(rand.randint(1, 50))
        new_individual.append(rand.randint(0, 1800) - 900)
        new_individual.append(rand.randint(0, 1800) - 900)
        new_individual.append(rand.randint(0, 20) - 10)
        new_individual.append(rand.randint(0, 20) - 10)
        population.append(new_individual)
    best_individual, best_score = population[0], 0
    for i in range(pop_size):
        if fitness(population[i], solar_system_inst) > best_score:
            best_score = fitness(population[i], solar_system_inst)
            best_individual = population[i]
    print("The best individual in generation 0 is: ", best_individual)
    print("Score: ", best_score)
    # run generations
    for epoch in range(epochs):
        selected_parents = list()
        for i in range(pop_size):
            new_parent = selection(4, population, solar_system_inst)
            selected_parents.append(new_parent)
        new_generation = list()
        for i in range(0, pop_size, 2):
            p_1, p_2 = selected_parents[i], selected_parents[i + 1]
            child_1, child_2 = crossover(cross_rate, p_1, p_2)
            mutation(child_1, mut_rate)
            mutation(child_2, mut_rate)
            new_generation.append(child_1)
            new_generation.append(child_2)
        population = new_generation
        population.append(best_individual)
        population.append(best_individual)
        best_individual, best_score = population[0], 0
        for i in range(pop_size):
            if fitness(population[i], solar_system_inst) > best_score:
                best_score = fitness(population[i], solar_system_inst)
                best_individual = population[i]
        print("The best individual in generation ", epoch + 1, "is: ", best_individual)
        print("Score: ", best_score)
    return best_score, best_individual


# main
solar_syst = sim.solar_system()
score, run = genetic(10, 0.9, 0.1, 30, solar_syst)
print(score, run)
solar_sys_draw = drawingScript.solarSystem(1600, 900)
draw_suns = (drawingScript.sun(solar_sys_draw, mass=10_000, position=(-400, 0), velocity=(0, 2.5)),
             drawingScript.sun(solar_sys_draw, mass=10_000, position=(400, 0), velocity=(0, -2.5)))
draw_planets = (drawingScript.planet(solar_sys_draw, mass=run[0], position=(run[1], run[2]), velocity=(run[3], run[4])))
tick = 0
while tick < 2_000:
    tick += 1
    time.sleep(0.01)
    solar_sys_draw.interactions()
    solar_sys_draw.update_bodies()
turtle.done()
