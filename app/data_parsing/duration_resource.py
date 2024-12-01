class DurationResource:
    """
    Represents a job's duration and resource requirements.

    Attributes:
        job_number (int): The unique identifier for the job.
        mode (int): The mode of operation for the job.
        duration (int): The time required to complete the job.
        resources (dict[str, int]): A dictionary mapping resource names to the quantities required.
    """

    def __init__(self, job_number, mode, duration, resources):
        self.job_number = job_number
        self.mode = mode
        self.duration = duration
        self.resources: dict[str, int] = resources
