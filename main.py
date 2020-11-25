'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions
import Astar
import IterativeDeepeningDFS as IDS
import UCS
import IterativeDeepeningAstar as IDAstar
from problem import ProblemSearch


def find_ucs_rout(source, target, size, graph):
    problem = ProblemSearch(source, target, size, graph)
    solution, cost = UCS.find_ucs_route(problem, )
    save_output(True, solution, problem.num_of_nodes, cost)


def save_output(success, path_string=None, opened_nodes=None, cost=None):
    output = ''
    if success is False:
        output = "no path"
    else:
        output = f'''{path_string} {cost} {opened_nodes}'''
    with open('output.txt', mode='w+', encoding='utf-8') as f:
        f.write(output)


def find_astar_route(source, target, size, graph):
    # import Algo
    # 'call function to find path, and return list of indices'
    problem = ProblemSearch(source, target, size, graph)
    solution, cost = Astar.find_astar_route(problem, )
    if solution:
        save_output(True, solution, problem.num_of_nodes, cost)
    else:
        save_output(False, solution, problem.num_of_nodes, cost)


def find_idastar_route(source, target, size, graph):
    problem = ProblemSearch(source, target, size, graph)
    solution, cost = IDAstar.find_idastar_route(problem)
    if solution:
        save_output(True, solution, problem.num_of_nodes, cost)
    else:
        save_output(False, solution, problem.num_of_nodes, cost)


def find_ids_route(source, target, size, graph):
    problem = ProblemSearch(source, target, size, graph)
    solver = IDS.IterativeDeepeningDFS(problem)
    solution, cost = solver()
    if solution:
        save_output(True, solution, problem.num_of_nodes, cost)
    else:
        save_output(False, solution, problem.num_of_nodes, cost)


def dispatch(file):
    start = tuple(map(int, file[1].split(',')))
    goal = tuple(map(int, file[2].split(',')))
    size = int(file[3])
    graph = [list(map(int, row.split(','))) for row in file[4:]]

    if file[0] == 'UCS':
        find_ucs_rout(start, goal, size, graph)
    elif file[0] == 'ASTAR':
        find_astar_route(start, goal, size, graph)
    elif file[0] == 'IDASTAR':
        find_idastar_route(start, goal, size, graph)
    elif file[0] == 'IDS':
        find_ids_route(start, goal, size, graph)


if __name__ == '__main__':
    with open("input.txt", "r") as reader:
        file = [line for line in reader.read().splitlines() if line]
    dispatch(file)
