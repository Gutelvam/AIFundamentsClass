from enum import Enum
from data_parsing import ProjectData


class SolverType(Enum):
    """
    Enum representing available solver types.

    Attributes:
        PYTHON_CONSTRAINT (int): Solver type using Python's constraint library.
        OR_TOOLS (int): Solver type using Google's OR-Tools.
    """

    PYTHON_CONSTRAINT = 1
    OR_TOOLS = 2


def process_solution(solution, pData: ProjectData):
    """
    Processes and adjusts a solution based on precedence constraints.

    This function adjusts the solution by ensuring that jobs with precedence constraints
    are correctly ordered and that the start times of jobs are normalized by the minimum
    start time of the first jobs.

    Args:
        solution (dict): A dictionary where keys are job identifiers (e.g., "job_1") and values
                        are the start times of the jobs.
        pData (ProjectData): The project data containing job precedence relations.

    Returns:
        dict: A sorted and adjusted solution with normalized start times.
    """
    has_preced = set()

    for job in pData.precedence_relations:
        for pId in job.successors:
            has_preced.add(f"job_{pId}")

    min_offset = min(solution[key] for key in solution if key not in has_preced)

    for key in solution:
        solution[key] -= min_offset

    solution = dict(sorted(solution.items(), key=lambda x: int(x[0].split("_")[1])))
    return solution
