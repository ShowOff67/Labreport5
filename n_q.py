import random

N = 8 
POPULATION_SIZE = 100
MUTATION_CHANCE = 0.1
MAX_GENERATIONS = 1000


def make_random_board():
    board = list(range(N))
    random.shuffle(board)  
    return board


def calculate_fitness(board):
    attacks = 0
    for i in range(N):
        for j in range(i + 1, N):
            if abs(board[i] - board[j]) == abs(i - j):  
                attacks += 1
    return attacks


def mutate(board):
    new_board = board.copy()
    i, j = random.sample(range(N), 2)
    new_board[i], new_board[j] = new_board[j], new_board[i]
    return new_board


def crossover(parent1, parent2):
    point = random.randint(1, N - 2)
    child = parent1[:point] + parent2[point:]
    return child


def evolve():
    population = [make_random_board() for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        population.sort(key=calculate_fitness)
        best = population[0]
        if calculate_fitness(best) == 0:
            print(f"Solution found in generation {generation}")
            return best

        num_parents = POPULATION_SIZE // 5
        parents = population[:num_parents]

        new_population = []
        while len(new_population) < POPULATION_SIZE:
            p1 = random.choice(parents)
            p2 = random.choice(parents)
            child = crossover(p1, p2)

            if random.random() < MUTATION_CHANCE:
                child = mutate(child)

            new_population.append(child)

        population = new_population

    population.sort(key=calculate_fitness)
    return population[0]


if __name__ == "__main__":
    solution = evolve()
   
    print("\nChessboard:")
    for row in range(N):
        line = ""
        for col in range(N):
            if solution[row] == col:
                line += " Q "
            else:
                line += " . "
        print(line)