import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def sleep_data_visualization(sleep_df : pd.DataFrame):
	# Distribution of SleepTime
	plt.figure(figsize=(10, 6))
	sns.histplot(sleep_df['SleepTime'], bins=20, kde=True)
	plt.title('Distribution of Sleep Time')
	plt.xlabel('Sleep Time (hours)')
	plt.ylabel('Frequency')
	plt.show()