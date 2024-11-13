import os
from data_types import parser, parse_types, project_data
from constraint import Problem

# Load set the file path, use the input to define the name
# file_path = input("Enter the path path") or "p01_dataset_8.txt";
file_path = "assessment/p01_dataset_8.txt";
print (os.getcwd())

with open(file_path, 'r') as file:
	proj_data = parser.parse_data(file)
	print(proj_data);

