import time
from constraint import Problem

from data_types import parser
from csp_solver import csp_solver

start_time = time.time()

# Load set the 5file path, use the input to define the name
# file_path = input("Enter the path path") or "p01_dataset_8.txt";
file_path = "assessment/p01_dataset_10.txt"

with open(file_path, "r") as file:
    proj_data = parser.parse_data(file)

    problem = csp_solver.define_problem(proj_data)

    solution = problem.getSolution()
    if solution:
        solution = parser.process_solution(solution, proj_data);
        print(solution);

end_time = time.time()
print(f"Execution time: {(end_time - start_time):.4f} seconds")