# FUNCIÓN 1. de creación de una población con alelos al azar

asdfghjk

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
