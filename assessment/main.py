import os
import csp_solver.csp_solver
from data_types import parser
from constraint import Problem
from csp_solver import csp_solver

# Load set the file path, use the input to define the name
# file_path = input("Enter the path path") or "p01_dataset_8.txt";
file_path = "assessment/p01_dataset_8.txt"

with open(file_path, "r") as file:
    proj_data = parser.parse_data(file)

    problem = csp_solver.define_problem(proj_data)

    solution = problem.getSolution()
    if solution:
        print(solution)