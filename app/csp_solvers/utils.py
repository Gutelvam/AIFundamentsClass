from enum import Enum
from data_parsing import ProjectData


class SolverType(Enum):
    PYTHON_CONSTRAINT = 1
    OR_TOOLS = 2


def process_solution(solution, pData: ProjectData):
    has_preced = set()

    for job in pData.precedence_relations:
        for pId in job.successors:
            has_preced.add(f"job_{pId}")

    min_offset = min(solution[key] for key in solution if key not in has_preced)

    for key in solution:
        solution[key] -= min_offset

    solution = dict(sorted(solution.items(), key=lambda x: int(x[0].split("_")[1])))
    return solution
