# FUNCIÓN 1. de creación de una población con alelos al azar

import dalziel as dz



with open ('abc.txt') as datos:
    suma= 0
    numero_personas = 0
    i = 0
    for line in datos:
        if i > 0:
            line = line.split(',')
            edad = int(line[1])
            nota = float(line[2])
            if edad >= 18:
                suma += nota
                numero_personas += 1
    i += 1
    print(suma/numero_personas)

cities = "BalTiMOre"
cities = ["BalTiMOre", "COLUMBUS", "miami") # de ser necesario debe primero uniformizar los nombres ingresados

a = dz.avgcity(cities)

years = 1920
years = [1920, 1930, 1948]

b = dz.avgyear(cities, year)

weeks = 12
weeks = [1, 6]
weeks = range(12:24)
c = dz.avgbiweek(cities, biweeks)

import scipy # for random numbers
def build_population(N, p):
    """The population consists of N individuals.Each individual has two chromosomes, containing
    allele "A" or "a", with probability p or 1-p, respectively.The population is a list of tuples.
    """
    population = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        population.append((allele1, allele2))
    return population

# FUNCIÓN 2. Cáculo de la infecciones promedio por año, la desviación estándar y número de registros
def compute_frequencies(population):
    """ Count the genotypes.Returns a dictionary of genotypic frequencies."""
    AA = population.count(("A", "A"))
    Aa = population.count(("A", "a"))
    aA = population.count(("a", "A"))
    aa = population.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})

# FUNCIÓN 3. Cálculo de la infecciones promedio por semana, la desviación estándar y número de registros

def reproduce_population(population):
    """ Create new generation through reproduction. For each of N new offspring:
    - choose the parents at random, 
    - the offspring receives a chromosome from each of the parents.
    """
    new_generation = []
    N = len(population)
    for i in range(N):
        # random integer between 0 and N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # which chromosome comes from mom
        chr_mom = scipy.random.randint(2)
        offspring = (population[mom][chr_mom], population[dad][1 - chr_mom])
        new_generation.append(offspring)
    return(new_generation)