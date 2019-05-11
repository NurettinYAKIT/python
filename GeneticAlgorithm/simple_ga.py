from fuzzywuzzy import fuzz
import random
import string


class Agent:
    def __init__(self, length):
        self.string = ''.join(random.choice(string.ascii_letters)
                              for _ in range(length))
        self.fitness = -1

    def __str__(self):
        return 'String: ' + str(self.string) + 'Fitness: ' + str(self.fitness)


in_str = None
in_str_length = None
population = 20
generations = 1000


def genetic_algorithm():
    agents = init_agents(population, in_str_length)

    for generation in range(generations):
        print('Generation ' + str(generation))
        if agents is not None:
            agents = fitness(agents)
            agents = selection(agents)
            agents = crossover(agents)
            agents = mutation(agents)

            if any(agent.fitness >= 90 for agent in agents):
                print('Threshold met!')
                exit(0)


def init_agents(population, length) -> [Agent]:
    return [Agent(length) for _ in range(population)]


def fitness(agents):
    print('fitness')
    for agent in agents:
        agent.fitness = fuzz.ratio(agent.string, in_str)
    return agents


def selection(agents):
    agents = sorted(agents, key=lambda agent: agent.fitness, reverse=True)
    print('\n'.join(map(str, agents)))
    agents = agents[:int(0.2) * len(agents)]
    return agents


def crossover(agents):
    print('crossover')
    offspring = []

    for _ in range(int((population - len(agents)) / 2)):
        parent1 = random.choice(agents)
        parent2 = random.choice(agents)
        child1 = Agent(in_str_length)
        child2 = Agent(in_str_length)
        split = random.randint(0, in_str_length)
        child1.string = parent1.string[0:split] + parent2.string[split:in_str_length]
        child2.string = parent2.string[0:split] + parent1.string[split:in_str_length]

        offspring.append(child1)
        offspring.append(child2)

    agents.extend(offspring)

    return agents


def mutation(agents):
    print('mutation')
    for agent in agents:
        for idx, param in enumerate(agent.string):
            if random.uniform(0.0, 1.0) <= 0.1:
                agent.string = agent.string[0:idx] + random.choice(string.ascii_letters) + agent.string[idx + 1:in_str_length]
    return agents


if __name__ == '__main__':
    in_str = 'Troy'
    in_str_length = len(in_str)
    genetic_algorithm()
