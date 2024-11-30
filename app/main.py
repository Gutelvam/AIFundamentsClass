import time
import logging

from ortools.sat.python import cp_model

from data_parsing import parse_file, ProjectData
from csp_solvers import SolverType, process_solution

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def main():
    start_time = time.time()

    solver_type: SolverType = SolverType.OR_TOOLS
    file_path = "data/p01_dataset_10.txt"

    with open(file_path, "r") as file:
        proj_data: ProjectData = parse_file(file)
        solution = {}

        match solver_type:
            case SolverType.PYTHON_CONSTRAINT:
                from csp_solvers import python_constraint

                problem = python_constraint.define_problem(proj_data)
                solution = problem.getSolution()
                if solution:
                    solution = process_solution(solution=solution, pData=proj_data)
                    logging.info(
                        f" Processing time: {(time.time() - get_solution_time):.4f} seconds"
                    )

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
