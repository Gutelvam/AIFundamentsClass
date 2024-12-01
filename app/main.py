"""
Script for solving constraint satisfaction problems (CSPs) using different solver types.

This script reads project data from a file, parses it, and solves the CSP using either 
Python's constraint library or OR-Tools, depending on the specified solver type. It logs 
the solution and execution time.

Modules:
    - time: Used for tracking execution time.
    - logging: Logs execution details and solutions.
    - ortools.sat.python.cp_model: Used for solving CSPs with Google's OR-Tools.
    - data_parsing: Custom module for parsing project data from files.
    - csp_solvers: Custom module for defining and solving CSPs using different approaches.

Functions:
    - main(): Main function to handle file parsing, problem definition, solving, and logging.

Solver Types:
    - PYTHON_CONSTRAINT: Solves the problem using Python's constraint library.
    - OR_TOOLS: Solves the problem using Google's OR-Tools library.

Usage:
    - Ensure the `data_parsing` and `csp_solvers` modules are correctly implemented and available.
    - Update the `file_path` variable to point to the dataset file.
    - Run the script as a standalone program.
"""

import time
import logging

from ortools.sat.python import cp_model

from data_parsing import parse_file, ProjectData
from csp_solvers import SolverType, process_solution

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def main():
    """
    Main function to solve the scheduling problem using the specified solver.

    It loads project data from a file, defines the scheduling problem, and solves it using either the 
    Python-Constraint solver or the OR-Tools solver based on the specified solver type. The solution 
    is then logged, along with the time taken to find the solution and the total execution time.

    The function performs the following steps:
    1. Loads project data from a specified file.
    2. Chooses the solver type (either PYTHON_CONSTRAINT or OR_TOOLS).
    3. Defines the problem using the chosen solver.
    4. Solves the problem and extracts the solution.
    5. Logs the time taken to find the solution and the execution time.
    """

    start_time = time.time()

    solver_type: SolverType = SolverType.OR_TOOLS
    file_path = "data/p01_dataset_8.txt"

    with open(file_path, "r") as file:
        proj_data: ProjectData = parse_file(file)
        solution = {}

        match solver_type:
            case SolverType.PYTHON_CONSTRAINT:
                from csp_solvers import python_constraint

                problem = python_constraint.define_problem(proj_data)
                solution = problem.getSolution()

            case SolverType.OR_TOOLS:
                from csp_solvers import ortools

                model, start_times = ortools.define_problem(proj_data)
                solver = cp_model.CpSolver()

                status = solver.Solve(model)
                if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
                    solution = ortools.extract_solution(solver, start_times, proj_data)

        get_solution_time = time.time()
        logging.info(
            f" Solution found : {(get_solution_time - start_time):.4f} seconds"
        )

        if solution:
            logging.info(f" {solution}")

    end_time = time.time()
    logging.info(f" Execution time: {(end_time - start_time):.4f} seconds")


if __name__ == "__main__":
    main()
