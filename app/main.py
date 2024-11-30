import time
import logging

from data_parsing import parse_file, ProjectData
from csp_solvers import python_constraint
from csp_solvers import process_solution

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def main():
    start_time = time.time()
    file_path = "data/p01_dataset_10.txt"

    try:

        with open(file_path, "r") as file:
            proj_data: ProjectData = parse_file(file)
            problem = python_constraint.define_problem(proj_data)
            solution = problem.getSolution()

            get_solution_time = time.time()
            logging.info(
                f" Solution found : {(get_solution_time - start_time):.4f} seconds"
            )
            if solution:

                solution = process_solution(solution=solution, pData=proj_data)
                logging.info(
                    f" Processing time: {(time.time() - get_solution_time):.4f} seconds"
                )
                logging.info(f" {solution}")
    except:
        logging.error("File not found: %s", file_path)

    end_time = time.time()
    logging.info(f" Execution time: {(end_time - start_time):.4f} seconds")


if __name__ == "__main__":
    main()
