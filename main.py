'''
Parse input and run appropriate code.
Don't use this file for the actual work; only minimal code should be here.
We just parse input and call methods from other modules.
'''

# do NOT import ways. This should be done from other files
# simply import your modules and call the appropriate functions
from Algorithms import *
from SearchProblem.Problem import ProblemSearch


def save_output(success, path_string=None, opened_nodes=None, cost=None):
    output = ''
    if success is False:
        output = "no path"
    else:
        output = f'''{path_string} {cost} {opened_nodes}'''
    with open('output.txt', mode='w+', encoding='utf-8') as f:
        f.write(output)


def find_route(problem, solver_type):
    solver = solver_type(problem)
    solution, cost = solver()
    if solution:
        save_output(True, solution, problem.num_of_nodes, cost)
    else:
        save_output(False, solution, problem.num_of_nodes, cost)


def dispatch(file):
    SOLVERS = {
        "UCS": UCS.UCS,
        "ASTAR": Astar.AStar,
        "IDASTAR": IterativeDeepeningAstar.IterativeDeepeningAstar,
        "IDS": IterativeDeepeningDFS.IterativeDeepeningDFS
    }
    start = tuple(map(int, file[1].split(',')))
    goal = tuple(map(int, file[2].split(',')))
    size = int(file[3])
    graph = [list(map(int, row.split(','))) for row in file[4:]]
    problem = ProblemSearch(start, goal, size, graph)

    if file[0] not in SOLVERS:
        print(f"Error: {file[0]} is not a valid algorithm!")
    else:
        find_route(problem, SOLVERS[file[0]])


if __name__ == '__main__':
    try:
        with open("input.txt", "r") as reader:
            file = [line for line in reader.read().splitlines() if line]
        dispatch(file)
    except Exception as e:
        print(e)
