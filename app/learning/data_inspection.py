import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_data_and_inspect(csv_path: str)-> pd.DataFrame:
	print(f"Loading data from ({csv_path})\n")

	df = pd.read_csv(csv_path)
	
	# Check the shape of the dataset (number of rows and columns)
	print(f"-- Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns\n")
	
	# Get general info about the dataset, including data types and non-null counts
	print(f"\nDataset Info\n {df.info()}\n")
	
	# Check for missing values
	print(f"Missing values in dataset\n {df.isnull().sum()}\n")

	# Display the first 5 rows of the dataset
	print(f"Head data:\n{df.head()}\n")

	# Describe the numeric columns for basic statistics
	print(f"Descriptive Statistics\n{df.describe()}\n")

	return df