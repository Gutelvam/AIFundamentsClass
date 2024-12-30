import time
import logging

from learning import *

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def main():
	start_time = time.time()

	sleep_df = load_data_and_inspect("data/learning/sleep_time_prediction/sleeptime_prediction_dataset.csv")
	sleep_data_visualization(sleep_df)
	
	end_time = time.time()
	logging.info(f"Execution time: {(end_time - start_time):.4f} seconds")


if __name__ == "__main__":
	main()